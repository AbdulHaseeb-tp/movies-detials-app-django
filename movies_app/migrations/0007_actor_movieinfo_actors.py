# Generated by Django 5.0.4 on 2024-05-17 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0006_movieinfo_directed_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='actors',
            field=models.ManyToManyField(related_name='acted_movies', to='movies_app.actor'),
        ),
    ]
