from django.shortcuts import render
from . models import MovieInfo

from .forms import MovieForm

from django.contrib.auth.decorators import login_required

# Create your views here.


# @login_required(login_url='login')
def create(request):

    # frm = MovieForm()

    if request.POST:  # shortest code
        frm=MovieForm(request.POST,request.FILES)
        if frm.is_valid:
            frm.save()
    else:
        frm=MovieForm()

        # or option

        # title=request.POST.get('title')
        # year=request.POST.get('year')
        # desc=request.POST.get('description')

        # movie_obj=MovieInfo(title=title,year=year,description=desc)
        # movie_obj.save() #object calling from cls MovieInfo

    return render(request,'create.html',{'frm':frm})



# decorators using changing the behaviour of functions
@login_required(login_url='login')
def list(request):

    # for edit clicking btn
    recent_visits=request.session.get('recent_visits',[])

    # cookies, session handling

    print(request.session)
    count=request.session.get('count',0)

    # print(request.COOKIES)
    count=int(count)
    count=count+1
    # storing session 
    request.session['count']=count

    # for edit clicking btn template view
    recent_movie_set=MovieInfo.objects.filter(pk__in=recent_visits)


    # movie_set = MovieInfo.objects.all()
    # print(movie_set)

    # or

    # movie_set = MovieInfo.objects.filter(year=2023,title='jailer')
    movie_set = MovieInfo.objects.all()
    print(movie_set)

    response=render(request,'list.html',{'recent_movies':recent_movie_set,'movies':movie_set,'visits':count})

    # seting cookies
    # response.set_cookie('visits',count)
    return response




@login_required(login_url='login')
def edit(request,pk):
    instance_to_be_edited=MovieInfo.objects.get(pk=pk)

    if request.POST:
        frm=MovieForm(request.POST,instance=instance_to_be_edited)
        if frm.is_valid():
            instance_to_be_edited.save()
    else:
        recent_visits=request.session.get('recent_visits',[])
        recent_visits.insert(0,pk)
        request.session['recent_visits']=recent_visits

        frm=MovieForm(instance=instance_to_be_edited) 

                        # o r OPTION
    # if request.POST:
    #     title=request.POST.get('title')
    #     year=request.POST.get('year')
    #     description=request.POST.get('description')
    #     instance_to_be_edited.title=title
    #     instance_to_be_edited.year=year
    #     instance_to_be_edited.description=description
    #     instance_to_be_edited.save()


    # frm=MovieForm(instance=instance_to_be_edited)

    return render(request,'create.html',{'frm':frm})




@login_required(login_url='login')
def delete(request,pk):

    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()  
    movie_set = MovieInfo.objects.all()

    return render(request,'list.html',{'movies':movie_set})