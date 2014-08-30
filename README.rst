[![Build Status](https://travis-ci.org/mishravikas/HealthDB.svg?branch=master)](https://travis-ci.org/mishravikas/HealthDB)
=========
 HealthDB
=========
Django based Patient Management System.

Ubuntu 14.04 Development Build Instructions::
	
	#retrieve latest apt-get list
	$sudo apt-get update

	#Install virtualenv and pip
	$sudo apt-get install python-pip python-virtualenv
	
	#Fork HealthDB
	http://github.com/<your_user_name>/HealthDB

	#Clone your forked repo
	$git clone https://github.com/<your_user_name>/HealthDB.git

	#Install dependencies using pip
	$cd HealthDB
	$pip install -r requirements.txt

	#Start the development server
	$cd HealthDB
	$./manage.py runserver

	




