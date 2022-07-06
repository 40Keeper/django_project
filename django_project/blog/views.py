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
def runbutton(request):
    exec(open("/home/nips/newproject/django_project/blog/python_scripts/testing.py").read())     #WHY CAN'T I SEE THIS BEING EXECUTED IN THE TERMINAL??????
    return render(request,'blog/runpage.html')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
