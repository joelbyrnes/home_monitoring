import os
import re
import sys
import serial
import time
from lib_cosm import CosmFeedUpdate

SERIAL_PORT = os.environ["SERIAL_PORT"]
FEED_ID = os.environ["FEED_ID"]
API_KEY = os.environ["API_KEY"]

pfu = CosmFeedUpdate(FEED_ID, API_KEY)

# eg: Node 1 Temp 24.00 C Humid 45.00 %
regex = re.compile("Node (?P<node>\d) Temp (?P<temp>[\d.]+) C Humid (?P<humid>[\d.]+) %", re.IGNORECASE)

#node_dict = {}
node_dict = {"1" : "pantry", "2": "storage"}

def parseline(line):
	r = regex.search(line)
	if r:
		d = r.groupdict()
		
		if d["node"] in node_dict:
			location = node_dict[d["node"]]

			# do some stuff; gather data, repeating as necessary for any number of datastreams
			pfu.addDatapoint(location+"_temp", d["temp"])
			pfu.addDatapoint(location+"_humid", d["humid"])

			print "node %s, location %s, temp %s, humid %s" % (d["node"], location, d["temp"], d["humid"])

			pfu.buildUpdate()
			pfu.sendUpdate()
			pfu.reset()
		else:
			print "node ID %s not known, temp %s, humid %s" % (d["node"], d["temp"], d["humid"])
	else:
		print "line not recognised: %s" % line,

def main():
	port = None
	try:
		port = serial.Serial(SERIAL_PORT, 57600, timeout=300)
		print port.portstr
		while 1:
			data = port.readline()
			#print data,
			parseline(data)
	except KeyboardInterrupt:
		print '^C received, exiting.'
		port.close()

if __name__ == '__main__':
    main()
