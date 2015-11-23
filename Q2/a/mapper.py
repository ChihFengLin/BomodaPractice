#!/usr/bin/python

# Consider three kinds of brand name variation
# 1. Lower case
# 2. Shortened name
# 3. Brand name without space

import simplejson as json
import re
import sys

brand1 = "Michael Kors"
brand2 = "Kate Spade"
for line in sys.stdin:
	try:
		data = json.loads(line)
		status_text = data['status']['text'].lower()
		comment = data['text'].lower()
		status_date = data['status']['created_at'].split()
		comment_date = data['created_at'].split()
		
		# If the id of status in different files are the same, it can only be counted as once
		status_date = status_date[1] + " " + status_date[2] + " " + status_date[5]  
		if brand1.lower() in status_text or "mk" in status_text or "michaelkors" in status_text:
			print str(data['status']['id']) + "," + brand1 + "\t" + status_date + "\t" + str(1)
		
		if brand2.lower() in status_text or "ks" in status_text or "katespade" in status_text:
			print str(data['status']['id']) + "," + brand2 + "\t" + status_date + "\t" + str(1)

		# Check comment text. Be careful for the same comment id.
		comment_date = comment_date[1] + " " + comment_date[2] + " " + comment_date[5]  
		if brand1.lower() in comment or "mk" in comment or "michaelkors" in comment:
			print str(data['id']) + "," + brand1 + "\t" + comment_date + "\t" + str(1)
		if brand2.lower() in comment or "ks" in comment or "katespade" in comment:
			print str(data['id']) + "," + brand2 + "\t" + comment_date + "\t" + str(1) 
		
		# Check the reply_comment. Be careful for the same reply_comment id.
		if "reply_comment" in data:
			reply_comment = data['reply_comment']['text'].lower()
			reply_comment_date = data['reply_comment']['created_at']
			reply_comment_date = reply_comment_date[1] + " " + reply_comment_date[2] + " " + reply_comment_date[5] 
			if brand1.lower() in reply_comment or "mk" in reply_comment or "michaelkors" in reply_comment:
				print str(data['reply_comment']['id']) + "," + brand1 + "\t" + reply_comment_date + "\t" + str(1)
			if brand2.lower() in reply_comment or "ks" in reply_comment or "katespade" in reply_comment:
				print str(data['reply_comment']['id']) + "," + brand2 + "\t"+ reply_comment_date + "\t" + str(1)


	except ValueError as e:
		continue