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
		repost_text = data['text'].lower()
		repost_date = data['created_at'].split()
		
		# If the id of status in different files are the same, it can only be counted as once
		repost_date = repost_date[1] + " " + repost_date[2] + " " + repost_date[5]  
		if brand1.lower() in repost_text or "mk" in repost_text or "michaelkors" in repost_text:
			print str(data['id']) + "," + brand1 + "\t" + repost_date + "\t" + str(1)
		
		if brand2.lower() in repost_text or "ks" in repost_text or "katespade" in repost_text:
			print str(data['id']) + "," + brand2 + "\t" + repost_date + "\t" + str(1)

		
		# Check the retweeted_text. Be careful for the same retweeted_text id.
		if "retweeted_status" in data:
			retweeted_text = data['retweeted_status']['text'].lower()
			retweeted__date = data['retweeted_status']['created_at']
			retweeted__date = retweeted__date[1] + " " + retweeted__date[2] + " " + retweeted__date[5] 
			if brand1.lower() in retweeted_text or "mk" in retweeted_text or "michaelkors" in retweeted_text:
				print str(data['reply_comment']['id']) + "," + brand1 + "\t" + retweeted__date + "\t" + str(1)
			if brand2.lower() in retweeted_text or "ks" in retweeted_text or "katespade" in retweeted_text:
				print str(data['reply_comment']['id']) + "," + brand2 + "\t"+ retweeted__date + "\t" + str(1)


	except ValueError as e:
		continue