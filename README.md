home_monitoring
===============   

Receives messages of the form:
Node 1 Temp 24.00 C Humid 35.00 % 
And posts them to Cosm (now Xively) under "legacy feeds" 

The feed names are configured in tempreader.py with location names, so the IDs map to places like "pantry". The data name is appended to the end like "pantry_temp". 


Setup and run
============= 

# python packages needed (on Raspberry Pi, which already has Python 2.7):

sudo apt-get install python-serial python-mechanize

# other useful packages for python: 
sudo apt-get install python-setuptools && sudo easy_install pip

# On R.Pi an FTDI USB serial interface is probably /dev/ttyUSB0, so edit tempreader.py and change the device there.  

# Then just run it:
python tempreader.py 


To do
=====

* re-create linux init.d script, log to checkout dir
* some kind of alert when no updates are received - email user?
* figure out how to post to xively's new feeds 
