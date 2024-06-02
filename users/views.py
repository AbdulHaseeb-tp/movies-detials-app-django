from django.shortcuts import render,redirect

from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def login(request):
    error_message=None
    if request.POST:
        # getting username and passwords 
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)#check user is in backend db 
        if user:
            auth_login(request,user)#session created in server..
            return redirect('list')
        else:
            error_message='invalid credintials'   
    return render(request,'users/login.html',{'error_message':error_message})



def logout(request):
    auth_logout(request)#Remove the authenticated user's ID from the request and flush their session data.
    return redirect('login')


def signup(request):
    user=None
    error_message=None
    if request.POST:
        # getting username and passwords 
        username=request.POST['username']
        password=request.POST['password']
        # print(username,password)
        # in casE of exception condi come try And Except use
        try:
            user=User.objects.create_user(username=username,password=password)
        except Exception  as e:
            error_message=str(e)
    return render(request,'users/create.html',{'user':user,'error_message':error_message})