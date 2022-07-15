# echo-client.py
import mysql.connector
import socket
import time
import sys
from datetime import datetime
now=datetime.now()
id=1
formatted_date=now.strftime('%Y-%m-%d %H:%M:%S')

HOST = "10.114.10.87"  # The server's hostname or IP address
PORT = 8000  # The port used by the server

# mydb = mysql.connector.connect(
#     host="10.114.10.80",
#     user="nips",
#     password="peach1395",
#     database="ICS_Testbed"
# )

# mycursor = mydb.cursor()


client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
# We set the socket to Blocking state to receive data from server side
client_socket.setblocking(1)

while True:  
    try:
        
        data=client_socket.recv(1024)
        if not data:
            continue
        rpm=data.decode()
        print("RPM: ", rpm)
        # sql= "INSERT INTO RPM_Count_Table (id, formatted_date, rpm) values (%s, %s, %s)"
        # mycursor.executemany(sql, id, formatted_date, rpm)
        # mydb.commit()
    
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

