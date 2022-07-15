# import imp
from urllib import response
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from .models import Post
import requests
import socket
import time
@login_required

#Get executed everytime
def home(request):
    return render(request, 'blog/home.html')

#Gets executed when Run button is clicked
def runbutton1(request):
    #exec(open("/home/nips/newproject/django_project/blog/python_scripts/sshconnectiontest1.py").read())  
    #exec(open("/home/nips/newproject/django_project/blog/python_scripts/robot_arm_client.py").read())
    HOST = "10.114.10.85"  # The server's hostname or IP address
    PORT = 6000  # The port used by the server
    import requests
    import socket
    import time
    client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.sendall("start".encode())
    return render(request,'blog/runpage.html')

def startbutton(request):
    #exec(open("/home/nips/newproject/django_project/blog/python_scripts/sshconnectiontest1.py").read())  
    exec(open("/home/nips/newproject/django_project/blog/python_scripts/start_arm.py").read())  
    return render(request,'blog/runpage.html')

def runbutton2(request):
    #exec(open("/home/nips/newproject/django_project/blog/python_scripts/sshconnectiontest2.py").read()) 
    exec(open("/home/nips/newproject/django_project/blog/python_scripts/conveyor_client.py").read())
    return render(request,'blog/runpage.html')

def runbutton3(request):
    #exec(open("/home/nips/newproject/django_project/blog/python_scripts/sshconnectiontest3.py").read()) 
    exec(open("/home/nips/newproject/django_project/blog/python_scripts/sensor_client.py").read())
    return render(request,'blog/runpage.html')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
