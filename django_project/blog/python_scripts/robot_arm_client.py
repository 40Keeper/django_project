# echo-client.py

import socket
import time

HOST = "10.114.10.85"  # The server's hostname or IP address
PORT = 6000  # The port used by the server

START="start"
STOP="stop"

client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
while True:
    command=input("Enter the command: ")
    client_socket.sendall(command.encode())
    if command==STOP:
        break
