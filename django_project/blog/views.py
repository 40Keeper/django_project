from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import socket
import sys
import mysql.connector

# MAKE CONNECTION WITH ROBOT ARM
ROBOT_HOST = "10.114.10.85"     # The server's hostname or IP address
ROBOT_PORT = 6000               # The port used by the server

# MAKE CONNECTION WITH CONVEYOR
CONVEY_HOST = "10.114.10.86"    # The server's hostname or IP address
CONVEY_PORT = 7000              # The port used by the server

# MAKE CONNECTION WITH SENSOR
SENSOR_HOST = "10.114.10.87"    # The server's hostname or IP address
SENSOR_PORT = 8000              # The port used by the server


@login_required

# Get executed everytime
def home(request):
    return render(request, 'blog/home.html')

# ROBOT ARM - RUN BUTTON
def runbutton1(request):
    global robot_client_socket
    robot_client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    robot_client_socket.connect((ROBOT_HOST, ROBOT_PORT))
    robot_client_socket.sendall("start".encode())
    print("Robot Arm Starting")
    return render(request,'blog/runpage.html')

# ROBOT ARM STOP BUTTON
def stopbutton1(request):
    global robot_client_socket
    robot_client_socket.sendall("stop".encode())
    # print("Robot arm stopping")
    return render(request,'blog/runpage.html')

# CONVEYOR BELT RUN BUTTON
def runbutton2(request):
    global convey_client_socket
    convey_client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    convey_client_socket.connect((CONVEY_HOST, CONVEY_PORT))
    convey_client_socket.sendall("0.008".encode())
    return render(request,'blog/runpage.html')

# CONVEYOR BELT STOP BUTTON
def stopbutton2(request):
    global convey_client_socket
    convey_client_socket.sendall("stop".encode())
    return render(request,'blog/runpage.html')

# RPM SENSOR RUN BUTTON
def runbutton3(request):
    global sensor_client_socket
    sensor_client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sensor_client_socket.connect((SENSOR_HOST, SENSOR_PORT))

    # We set the socket to Blocking state to receive data from server side
    sensor_client_socket.setblocking(1)

    #Feed RPM Data into MySQL
    mydb = mysql.connector.connect(
    host="localhost",
    user="nips",
    password="peach1395",
    database="ICS_Testbed"
    )

    while True:
        try:
            data=sensor_client_socket.recv(1024)
            if not data:
                continue
            rpm=data.decode()
            print("RPM: ", rpm)

            # Store "rpm" value in MySQL database
            mycursor = mydb.cursor()
            sql= f"INSERT INTO `RPM_Count_Table`(`RPM_VALUE`,`TIMESTAMP`) VALUES( {rpm}, NOW());"
            mycursor.execute(sql)
            mydb.commit()

        except BlockingIOError:
            continue

        except ConnectionError:
            print("Connection error")
            sensor_client_socket.close()
            break            

        except KeyboardInterrupt:
            print("keyboard interrupt")
            sensor_client_socket.close()
            sys.exit(0)     

        # return render(request,'blog/runpage.h tml')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
