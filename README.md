home_monitoring
===============   

Receives messages of the form:
Node 1 Temp 24.00 C Humid 35.00 % 
And posts them to Cosm (now Xively) under "legacy feeds" 

The feed names are configured in tempreader.py with location names, so the IDs map to places like "pantry". The data name is appended to the end like "pantry_temp". 


Setup and run
============= 

Python packages needed (on Raspberry Pi, which already has Python 2.7):

  sudo apt-get install python-serial python-mechanize

Other useful packages for python: 
  sudo apt-get install python-setuptools && sudo easy_install pip

Copy the file settings.env.default to settings.env and fill in your Xively settings and serial port
On R.Pi the first USB serial interface is usually /dev/ttyUSB0

Then run it:
  ./tempreader.sh


Service
=======

Once the above works, you can make it a startup service on Debian/Raspbian:

Symlink to tempreader-daemon.sh:
  sudo ln -s <your path>/tempreader-daemon.sh /etc/init.d/tempreader

Tell it to run the daemon script on boot:
  sudo update-rc.d tempreader defaults

To remove the script startup:
  sudo update-rc.d -f tempreader remove

And remove the link from init.d too if you want.  


To do
=====

* some kind of alert when no updates are received - email user?
* figure out how to post to xively's new feeds
* LSB header in daemon script 
* add battery monitoring to nodes and monitor it
