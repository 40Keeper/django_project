# import imp
from urllib import response
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from .models import Post
import requests

@login_required

#Get executed everytime
def home(request):
    return render(request, 'blog/home.html')

#Gets executed when Run button is clicked
def runbutton1(request):
    exec(open("/home/nips/newproject/django_project/blog/python_scripts/testing.py").read())  
    return render(request,'blog/runpage.html')

def runbutton2(request):
    exec(open("/home/nips/newproject/django_project/blog/python_scripts/testing.py").read())
    return render(request,'blog/runpage.html')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
