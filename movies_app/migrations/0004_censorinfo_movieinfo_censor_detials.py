# Generated by Django 5.0.4 on 2024-05-13 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0003_movieinfo_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='CensorInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=10, null=True)),
                ('cirtfied_by', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='censor_detials',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movie', to='movies_app.censorinfo'),
        ),
    ]
