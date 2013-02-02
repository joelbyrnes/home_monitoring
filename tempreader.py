import re
import sys
import serial
import time
from lib_cosm import CosmFeedUpdate

SERIAL_PORT = "/dev/tty.usbserial-A600dVGp"

regex = re.compile("Node (?P<node>\d) Temp (?P<temp>[\d.]+) C", re.IGNORECASE)

pfu = CosmFeedUpdate("101079","-T7sOofXIdqrFYVHMvVzZCler-eSAKxURlV4RHc5UTExVT0g")

node_dict = {"1" : "pantry", "2": "wine_rack"}

def parseline(line):
	r = regex.search(line)
	if r:
		d = r.groupdict()
		
		if d["node"] in node_dict:
			location = node_dict[d["node"]]

			# do some stuff; gather data, repeating as necessary for any number of datastreams
			pfu.addDatapoint(location, d["temp"])

			print "node %s, location %s, temp %s" % (d["node"], location, d["temp"])

			pfu.buildUpdate()
			pfu.sendUpdate()
			pfu.reset()
		else:
			print "node ID %s not known, temp %s" % (d["node"], d["temp"])
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
