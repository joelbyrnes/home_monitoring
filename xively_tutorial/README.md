Xively tutorial for Raspberry Pi
================================

$ sudo apt-get install python-setuptools
$ sudo easy_install pip
$ sudo pip install virtualenv
$ virtualenv .envs/venv
$ source .envs/venv/bin/activate
$ pip install xively-python
# or $ pip install --pre xively-python

# create a device and feed on xively, set it private, note the Feed ID and Dev API key

FEED_ID=12345 API_KEY=9MzbRooFNPJIy3zxVNRPUPll4JGSAKxsMmg4STZHbzNKTT0g DEBUG=true python xively_tutorial.py

suggest putting this in a run.sh file
