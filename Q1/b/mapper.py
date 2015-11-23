#!/usr/bin/python

# This mapper only parses the required information and pass it to combiner.py

import simplejson as json
import re
import sys

for line in sys.stdin:
	try:
		data = json.loads(line)
		
		# Status related information
		status_id =  data['status']['id']
		status_userid = data['status']['user']['id']
		status_user_location = data['status']['user']['province']
		print str(status_id) + "\t" + str(status_userid) + "\t" + str(status_user_location) + "\t" + str(1)
		
		# Comments related information
		comment_id = data['id']
		comment_userid = data['user']['id']
		comment_user_location = data['user']['province']
		print str(comment_id) + "\t" + str(comment_userid) + "\t" + str(comment_user_location) + "\t" + str(1)

		# Reply_Comment related information
		if "reply_comment" in data:
			reply_comment_id = data['reply_comment']['id']
			reply_comment_userid = data['reply_comment']['user']['id']
			reply_comment_location = data['reply_comment']['user']['province']
			print str(reply_comment_id) + "\t" + str(reply_comment_userid) + "\t" + str(reply_comment_location) + "\t" + str(1)

	except ValueError as e:
		continue
