#!/usr/bin/python

# The object of this file is to remove duplicate id input 
#(including status_id, comment_id, reply_comment_id) from mapper.py
# and output a unique one to the reducer.py

import simplejson as json
import re
import sys

previous_text_id = ""
previous_user_id = ""
previous_location_id = ""
first = True

for line in sys.stdin:
	try:
		text_id, user_id, location_id, count = line.split("\t")
		if (first):
			previous_text_id = text_id
			previous_user_id = user_id
			previous_location_id = location_id
			first = False

		if text_id != previous_text_id:
			print previous_user_id+ "\t" + previous_location_id + "\t" + str(1)
			previous_text_id = text_id
			previous_user_id = user_id
			previous_location_id = location_id

	except ValueError as e:
		continue

# Notice we have to print the last one
print previous_user_id + "\t" + previous_location_id + "\t" + str(1)