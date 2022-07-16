# import imp
from urllib import response
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from .models import Post
import requests
import socket
import time

import blog

# from blog.python_scripts.robot_arm_client import STOP
@login_required

#Get executed everytime
def home(request):
    return render(request, 'blog/home.html')

#Gets executed when Run button is clicked
def runbutton1(request):
    #exec(open("/home/nips/newproject/django_project/blog/python_scripts/sshconnectiontest1.py").read())  
    #exec(open("/home/nips/newproject/django_project/blog/python_scripts/robot_arm_client.py").read())
    import socket
    HOST = "10.114.10.85"  # The server's hostname or IP address
    PORT = 6000  # The port used by the server
    client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.sendall("start".encode())
    return render(request,'blog/runpage.html')

def stopbutton1(request):
    #exec(open("/home/nips/newproject/django_project/blog/python_scripts/sshconnectiontest1.py").read())  
    #exec(open("/home/nips/newproject/django_project/blog/python_scripts/start_arm.py").read())  
    import socket
    # from blog.python_scripts.robot_arm_client import STOP
    HOST = "10.114.10.85"  # The server's hostname or IP address
    PORT = 6000  # The port used by the server
    client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.sendall("stop".encode())
    return render(request,'blog/runpage.html')

def runbutton2(request):
    #exec(open("/home/nips/newproject/django_project/blog/python_scripts/sshconnectiontest2.py").read()) 
    #exec(open("/home/nips/newproject/django_project/blog/python_scripts/conveyor_client.py").read())
    import socket
    HOST = "10.114.10.86"  # The server's hostname or IP address
    PORT = 7000  # The port used by the server
    client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.sendall("0.008".encode())
    return render(request,'blog/runpage.html')

def stopbutton2(request):
    #exec(open("/home/nips/newproject/django_project/blog/python_scripts/sshconnectiontest2.py").read()) 
    #exec(open("/home/nips/newproject/django_project/blog/python_scripts/conveyor_client.py").read())
    import socket
    HOST = "10.114.10.86"  # The server's hostname or IP address
    PORT = 7000  # The port used by the server
    client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.sendall("stop".encode())
    return render(request,'blog/runpage.html')

def runbutton3(request):
    # exec(open("/home/nips/newproject/django_project/blog/python_scripts/sshconnectiontest3.py").read()) 
    # exec(open("/home/nips/newproject/django_project/blog/python_scripts/sensor_client.py").read())
    import socket
    import sys
    import mysql.connector

    # now=datetime.now()
    # # id=1
    # # formatted_date=now.strftime('%Y-%m-%d %H:%M:%S')

    HOST = "10.114.10.87"  # The server's hostname or IP address
    PORT = 8000  # The port used by the server
    client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.close((HOST, PORT))
    # We set the socket to Blocking state to receive data from server side
    client_socket.setblocking(1)

    #Feed RPM Data into MySQL
    mydb = mysql.connector.connect(
    host="localhost",
    user="nips",
    password="peach1395",
    database="ICS_Testbed"
    )

    while True:
        try:
            data=client_socket.recv(1024)
            if not data:
                continue
            rpm=data.decode()
            print("RPM: ", rpm)

            mycursor = mydb.cursor()
            # rpm_value = rpm
            sql= f"INSERT INTO `RPM_Count_Table`(`RPM_VALUE`,`TIMESTAMP`) VALUES( {rpm}, NOW());"
            mycursor.execute(sql)
            mydb.commit()

        except BlockingIOError:
            continue

        except ConnectionError:
            print("Connection error")
            client_socket.close()
            break            

        except KeyboardInterrupt:
            print("keyboard interrupt")
            client_socket.close()
            sys.exit(0)     

        
        # return render(request,'blog/runpage.html')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
