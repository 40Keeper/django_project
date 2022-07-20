# **ICS SECURITY TESTBED**

## **WEB INTERFACE**
---

Please make sure you are accessing the programs from a user having temporary root access. For the existing user,
```
Username: nips
Password: peach1395
```
### **Commands to Run the Web Interface**

Change to the directory **newproject** under home
```bash
    cd ~
    cd newproject
```
![alt text](https://github.com/40Keeper/django_project/blob/master/README_Images/Pic1.png)


Activate the **virtual environment** with the help of source command. ***Make sure to do this every time, as without activating the virtual environment, Django will not work.***
```bash
    source my_env/bin/activate
```
![alt text](https://github.com/40Keeper/django_project/blob/master/README_Images/Pic2.png)


From **newproject**, go to the directory containing the Django Project
```bash
    cd django_project
```

To **run the django_server**, execute the following command in **django_project** directory 
```bash
    python manage.py runserver
```
Terminal will print a few lines of output ending with **"Quit the server with CONTROL-C"**. 

![alt text](https://github.com/40Keeper/django_project/blob/master/README_Images/Pic3.png)


***Keep this terminal running and DO NOT close it.***

___
## Login Details

You will be automatically redirected to a Log In page

![alt text](https://github.com/40Keeper/django_project/blob/master/README_Images/LoginPage.png)


Log In into the interface with the help of user credentials as provided above.


___
## Connecting server to the network

* Connect the Host computer of Web Interface to the network switch physically via Ethernet cable.

![alt text](https://github.com/40Keeper/django_project/blob/master/README_Images/Pic4.png)


* Open "Wired Settings"
![alt text](https://github.com/40Keeper/django_project/blob/master/README_Images/Pic5.png)


* Open the "Wired" dialog box from the gear icon.

![alt text](https://github.com/40Keeper/django_project/blob/master/README_Images/Pic6.png)


* Go to IPv4
* Select "Manual"
* Enter the Address as 10.114.10.80
* Enter the Netmask as 255.255.255.0

![alt text](https://github.com/40Keeper/django_project/blob/master/README_Images/Pic7.png)


* Apply changes and close
* Turn your Wired network connection OFF and ON.

## To access the internet
* If you wish to access the internet, then connect the ethernet cable to a server with Internet access.
* Go to "Wired Setttings > IPv4" and select the option "Automatic (DHCP)"
* Turn your Wired network connection OFF and ON.
___

## Launching project on a browser


Go to your favourite browser and after executing the previous command, type the following in the SEARCH BAR and hit ENTER.
```
127.0.0.1:8000
```
Alternatively, you can also type the following:
```
localhost:8000
```

You have now entered the Web Interface Page. If the page prompts you to **log in**, then you have executed everything correctly!

___

## **INSTRUCTIONS TO RUN THE SETUP**

Make sure that you have logged in.

"Add image of web interface"

After logging in, you will be directed to the web interface.

### STEP-1: To run the Robot Arm Server files- 
1. Open a new terminal
1. ```ssh pi@10.114.10.85```

    [password: ```raspberry```]
1. Once you see "```pi@robotarm```" on the terminal, you have now entered the Raspberry Pi.
1. ```cd python ```
1. ```python robot_arm_server.py```

![alt text](https://github.com/40Keeper/django_project/blob/master/README_Images/Pic8.png)


ROBOT ARM SERVER IS NOW RUNNING!


### STEP-2: To run the Conveyor Belt Server files- 
1. Open a new terminal
1. ```ssh pi@10.114.10.86```

    [password: ```raspberry```]
1. Once you see "```pi@conveyor```" on the terminal, you have now entered the Raspberry Pi.
1. ```cd python ```
1. ```python conveyor_server.py```

![alt text](https://github.com/40Keeper/django_project/blob/master/README_Images/Pic9.png)


CONVEYOR BELT SERVER IS NOW RUNNING!

### STEP-3: To run the RPM Sensor Server files- 
1. Open a new terminal
1. ```ssh pi@10.114.10.87```

    [password: ```raspberry```]
1. Once you see "```pi@hallsensor```" on the terminal, you have now entered the Raspberry Pi.
1. ```cd python ```
1. ```python sensor_server.py```

![alt text](https://github.com/40Keeper/django_project/blob/master/README_Images/Pic10.png)


RPM SENSOR SERVER IS NOW RUNNING!
___

## Execute the Client Scripts from Web Interface
The client scripts have been stored on the Host computer of the Web Server, and will be executed by hitting the "Run" buttons on the interface. 

* Under the "Robotic Arm Command", on hitting the "Run" button, Robotic Arm will start working.
![alt text](https://github.com/40Keeper/django_project/blob/master/README_Images/Pic11.png)


* Under the "Conveyor Belt Command", on hitting the "Run" button, Conveyor Belt will start working.
* You may choose Delay for the belt from the given options in the drop down menu. If you select a different value of Delay and execute the program again, the conveyor should move with a different speed.
![alt text](https://github.com/40Keeper/django_project/blob/master/README_Images/Pic12.png)


* Under the "Speed Sensor Output", on hitting the "Run" button, the RPM Sensor starts counting.
![alt text](https://github.com/40Keeper/django_project/blob/master/README_Images/Pic13.png)

*  The function triggerred by hitting "Run" button wil dynamically update the RPM data at every rotation of conveyor motor into a MySQL Table.
*  In order to access the SQL Table, entr the following URL in a new browser page and hit ENTER.
```
localhost/phpmyadmin
```
* Log In into PHPMyAdmin with the same credentials as above.
* Go to ICS_Testbed > RPM_Count_Table
* REFRESH the page to see latest entries of RPM Value from the sensor.
* NOTE:- Set the "Sort by key" option tp "PRIMARY (DESC)" to see the latest entries at the top of the page.
![alt text](https://github.com/40Keeper/django_project/blob/master/README_Images/SQL.png)


