# echo-client.py

import socket
import time

HOST = "10.114.10.86"  # The server's hostname or IP address
PORT = 7000  # The port used by the server

START="start"
STOP="stop"
SPEED="speed"
client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.setblocking(0)

while True:  
    command=input("Enter conveyor delay: ")
    client_socket.sendall(command.encode())
    if command==STOP:
        break
    
        
# command1=[SPEED,0.009]
# command1=str(command1)
# client_socket.send(command1.encode())
# time.sleep(10)
# client_socket.send(STOP.encode())

