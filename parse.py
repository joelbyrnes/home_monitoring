import re
import sys
from lib_cosm import CosmFeedUpdate

pfu = CosmFeedUpdate("101079","-T7sOofXIdqrFYVHMvVzZCler-eSAKxURlV4RHc5UTExVT0g")

regex = re.compile("Node (?P<node>\d) Temp (?P<temp>[\d.]+) C", re.IGNORECASE)

node_dict = {"1" : "pantry"}

for line in sys.stdin:
	#print line,
	r = regex.search(line)
	if r:
		d = r.groupdict()
		
		if d["node"] in node_dict:
			location = node_dict[d["node"]]

			# do some stuff; gather data, repeating as necessary for any number of datastreams
			pfu.addDatapoint(location, d["temp"])

			print "node %s, location %s, temp %s" % (d["node"], location, d["temp"])

			# finish up and submit the data
			pfu.buildUpdate()
			#pfu.sendUpdate()

			# TODO perhaps this should be automatic in send
			pfu.reset()
		else:
			print "node ID %s not known" % d["node"]
