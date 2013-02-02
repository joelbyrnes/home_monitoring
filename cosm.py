# http://api.cosm.com/v2/feeds/101079

# PUT /v2/feeds/YOUR_FEED_ID
# {
#  "version":"1.0.0",
#  "datastreams":[
#      {"id":"0", "current_value":"100"},
#      {"id":"two", "current_value":"500"},
#      {"id":"3.0", "current_value":"300"}
#  ]
# }

from lib_cosm import CosmFeedUpdate

pfu = CosmFeedUpdate("101079","-T7sOofXIdqrFYVHMvVzZCler-eSAKxURlV4RHc5UTExVT0g")
# do some stuff; gather data, repeating as necessary for any number of datastreams
pfu.addDatapoint("pantry", 30.01)
# finish up and submit the data
pfu.buildUpdate()
pfu.sendUpdate()
# TODO perhaps this should be automatic in send
pfu.clearData()
