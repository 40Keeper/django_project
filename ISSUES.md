# ISSUES IN INTERFACE

## BACKEND
1. Server enters an infinite while loop when hitting the "Run" button for "Speed Sensor Output". This functionality can not be avoided as this is the only was how I can get the server to continuously update data in the MySQL databse. If we give a return function to the while loop, it will store RPM data in the Database only once, which is undesirable. This issue can be fixed either by using multiple threads, or by adding a separate Javascript functionality to the system.
2. Variable from the DropDown menu of the "Conveyor Belt Commands" unable to fetch variable from blog/templates/blog/home.html to blog/views.py for continuous speed variation during execution. 
    Refer:-
    * https://stackoverflow.com/a/11586830
4. Instantaneous display of RPM count from database to interface on the label "RPM Count:".

## FRONTEND
1. Improve CSS and fix alignment to maximize space utilization on the web interface.
2. On hitting the "Run" button on the "Conveyor Belt Commands", the video should start playing on loop. When conveyor is stopped, video should stop with the thumbnail with "OFF" written on it getting displayed.
3. Toggle button under "Raspberry Pi Commands" has no functionality as of now.
4. Do we need to add a command line interface to the web interface?? What is its use??

## UPLOAD ON SERVER
1. Web Interface needs to be migrated from Django development environment to an Apache2 server for production deployment. This migration is recommended to be done only after all backed is properly configured.
  Refer the following links for guidance--
  * https://simpleisbetterthancomplex.com/tutorial/2021/06/27/how-to-start-a-production-ready-django-project.html
  * https://www.youtube.com/results?search_query=django+production+deployment
