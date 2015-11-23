#!/usr/bin/python

# The object of this file is to merge the same location_id and accumulate the count number

import simplejson as json
import re
import sys
import heapq

def dict_nlargest(d,n):
    return heapq.nlargest(n ,d, key = lambda k: d[k])

previous_location_id = ""
total_count = 0
first = True
top_list = {}
temp_top_list = {}

for line in sys.stdin:
	try:
		userid, location_id, count = line.split("\t")
		if (first):
			previous_location_id = location_id
			first = False
		
		total_count += int(count)

		if location_id != previous_location_id:
			top_list.update({previous_location_id:total_count})
			if (len(top_list) > 10):
				print 1
				top_ten = dict_nlargest(top_list,10)
				for key in top_ten:
					temp_top_list[key] = top_list[key]

    			top_list = temp_top_list
    			temp_top_list.clear()

			#print previous_location_id + "\t" + str(total_count)
			previous_location_id = location_id
			total_count = int(count)


	except ValueError as e:
		continue

# Print the last one
#print previous_location_id + "\t" + str(total_count)


top_list[previous_location_id] = total_count

if (len(top_list) > 10):
    for key, value in sorted(top_list.iteritems(), key=lambda (k,v): (v,k)):
   	    print "%s: %s" % (key, value)
