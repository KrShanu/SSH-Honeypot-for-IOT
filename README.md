How deploy SSH Honeypot for IoT devices with MQTT protocol
It is always advised to deploy Honeypot in a virtual environment, so that host machine can be secured.
Step1: Download the SSH honeypot in Host Machine, in your desired directory.
	$git clone https://github.com/shbhmsingh72/SSH-Honeypot.git
	Requirement:
	MySql
	$apt-get install mysql-server
	Python2
	$apt-get install python
	Openssh-server
	$apt-get install openssh-server
	Python-pip
	$apt install python-pip
	
Step2: Download Docker
	$apt-get install docker.io
Step3: (a) Download broker in Docker
	$ docker pull kmamit/mqtt:0.4
	(This is pre-configured) 
OR	
You can download broker manually in Docker and get it setup
	Create an Ubuntu images in docker
	Help:- https://www.linux.com/blog/learn/intro-to-linux/2018/1/how-create-docker-image
	
$git clone https://github.com/shbhmsingh72/hbmqtt.git
	( requirment : python3, pip, libraries paramiko, asyncio, hmqtt )
	$apt-get install python3
	$apt-get install python3-pip
	$pip3 install paramiko
$pip3 install asyncio
$pip3 install hmqtt
	$docker commit CONTAINER_ID broker
	
(b) Now the image is create, let’s setup broker in Docker
 $ docker images
	Copy image id
	$ docker run [id ] &
	$ docker ps // list all available (running) dockers containers ids

$Docker inspect <docker container ID>  // getting info about docker (IP)
	copy new running id of image
	$ docker exec -it [id] /bin/bash
	(c) configuring broker
	 $cd root/
	$vim broker-start.py
	Change IP to host machine or where you want save log files.
	 	
	
Step4: Download IoT Simulator in Host Machine (MySQL is required)
	$git clone https://github.com/shbhmsingh72/IoT-Simulator.git
	In Iot Simulator you have to run
	Open terminal
	$cd /…/IoT-Simulator/conf
	$vim client.conf
	Provide Docker IP
	$vim db.conf
	Provide MySql user name and password
	 
	Change MYSQL_USER and MYSQL_PASSWORD of your Mysql
Advice: it better to create new user in mysql because by default in mysql root user is configured as “Auth-Socket” for authentication, which may create trouble in connecting mysql. Change this setting to “Native-Password” or simply create new user which have default native-password as setting 
	$cd /…/IoT-Simulator/bin
	$chmod +x runbroker.sh
	$chmod +x runsimulator.sh
$./runbocker.sh 
$./runsimulator.sh
When you will run simulator and browser will pop-up 
Here you can add as many as Iot device upto thousand devices.
Step5:	In SSH Honeypot
	Open server folder
	$cd /…/SSH-Honeypot/server
	$vim SshServer.py
	Change IP to broker IP
	 
	$run main.py in SSH Honeypot
	You can configure honeypot.cfg for ip and other settings
$vim honeypot.cfg

Step6: In Docker 
	$cd root/
	$run brocker-start.py in broker
	
	you can connect honeypot using
$ssh honeypot at root@0.0.0.0 -p 2222                  (default)
Default password is “root”, i.e. password of of your broker.
	Two logs file will be generated in log folder with ip and passwords



