#!/usr/bin/python

# The object of this file is to merge the same userid/location_id and accumulate the count number

import simplejson as json
import re
import sys
import heapq

previous_userid = ""
total_count = 0
first = True
top_list = []

for line in sys.stdin:
	try:
		userid, location_id, count = line.split("\t")
		if (first):
			previous_userid = userid
			first = False
		
		total_count += int(count)

		if userid != previous_userid:
			heapq.heappush(top_list, (total_count, previous_userid))
			if (len(top_list) > 10):
				heapq.heappop(top_list)
			previous_userid = userid
			total_count = int(count)


	except ValueError as e:
		continue

# Print the last one
heapq.heappush(top_list, (total_count, previous_userid))
if (len(top_list) > 10):
	heapq.heappop(top_list)

print "Top 10 userID within whole posts (counts, userID):"
print top_list