.. image:: https://travis-ci.org/mishravikas/HealthDB.svg?branch=master
    :target: https://travis-ci.org/mishravikas/HealthDB

.. image:: https://badges.gitter.im/mishravikas/HealthDB.png
	:target: https://gitter.im/mishravikas/HealthDB
=========
 HealthDB
=========
Django based Electronic Medical Record (EMR) and Patient Management System.

Ubuntu 14.04 Development Build Instructions::
	
	#retrieve latest apt-get list
	$sudo apt-get update

	#Install virtualenv, pip and paver
	$sudo apt-get install python-pip python-virtualenv python-paver
	
	#Fork HealthDB
	http://github.com/<your_user_name>/HealthDB

	#Clone your forked repo
	$git clone https://github.com/<your_user_name>/HealthDB.git

	#Install dependencies
	$cd HealthDB
	$paver setup

	#Start the development server
	$paver start

Mac OS X Development Build Instructions::
	
	#Install pip
	$sudo easy_install pip

	#Install virtualenv and paver
	$sudo pip install virtualenv paver
	
	#Fork HealthDB
	http://github.com/<your_user_name>/HealthDB

	#Clone your forked repo
	$git clone https://github.com/<your_user_name>/HealthDB.git

	#Install dependencies
	$cd HealthDB
	$paver setup

	#Start the development server
	$paver start

	




