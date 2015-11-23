#!/usr/bin/python

# The object of this file is to merge the same location_id and accumulate the count number

import simplejson as json
import re
import sys
import heapq


previous_location_id = ""
total_count = 0
first = True
top_list = []


for line in sys.stdin:
	try:
		userid, location_id, count = line.split("\t")
		if (first):
			previous_location_id = location_id
			first = False
		
		total_count += int(count)

		if location_id != previous_location_id:
			heapq.heappush(top_list, (total_count, previous_location_id))
			if (len(top_list) > 10):
				heapq.heappop(top_list)

			previous_location_id = location_id
			total_count = int(count)


	except ValueError as e:
		continue

# Print the last one
heapq.heappush(top_list, (total_count, previous_location_id))
if (len(top_list) > 10):
	heapq.heappop(top_list)

print "Top 10 locations within whole posts (counts, provinceID):"
print top_list
