#!/usr/bin/python


import simplejson as json
import re
import sys


for line in sys.stdin:
	try:
		data = json.loads(line)
		status_date = data['status']['created_at'].split()
		comment_date = data['created_at'].split()
		
		# If the id of status in different files are the same, it can only be counted as once
		status_time = status_date[3].split(":") 
		print str(data['status']['id']) + "," + str(status_time[0]) + "\t" + str(1)

		# Check comment text. Be careful for the same comment id.
		comment_time = comment_date[3].split(":")
		print str(data['id']) + "," + str(comment_time[0]) + "\t" + str(1) 
		
		# Check the reply_comment. Be careful for the same reply_comment id.
		if "reply_comment" in data:
			reply_comment_date = data['reply_comment']['created_at']
			reply_comment_time = reply_comment_date[3].split(":")
			print str(data['reply_comment']['id']) + "," + str(reply_comment_time[0]) + "\t" + str(1)

	except ValueError as e:
		continue