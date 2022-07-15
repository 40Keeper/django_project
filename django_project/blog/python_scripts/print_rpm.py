import mysql.connector
import time

mydb = mysql.connector.connect(
    host="10.114.10.80",
    user="nips",
    password="peach1395",
    database="ICS_Testbed"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT RPM_VALUE from RPM_Count_Table")
myresult = mycursor.fetchall()

for x in myresult:
    y=int(x)
    print(y)                ## Print this value in the disabled label
    time.sleep(1)           ## Execute loop again after 1 sec
