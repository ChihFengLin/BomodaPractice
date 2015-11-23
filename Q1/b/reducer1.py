#!/usr/bin/python

# The object of this file is to merge the same userid/location_id and accumulate the count number

import simplejson as json
import re
import sys

previous_userid = ""
total_count = 0
first = True
for line in sys.stdin:
	try:
		userid, location_id, count = line.split("\t")
		if (first):
			previous_userid = userid
			first = False
		
		total_count += int(count)

		if userid != previous_userid:
			print previous_userid + "\t" + str(total_count)
			previous_userid = userid
			total_count = int(count)


	except ValueError as e:
		continue

# Print the last one
print previous_userid + "\t" + str(total_count)