#!/usr/bin/python

import simplejson as json
import re
import sys


total_count = 0
previous_time = ""
maxtime_count = 0
maxtime = ""


first = True
for line in sys.stdin:
	try:
		time, count = line.split("\t")
		if (first):
			previous_time = time
			first = False
		
		total_count += int(count)

		if time != previous_time:
			if total_count > maxtime_count:
				maxtime_count = total_count
				maxtime = "From " + str(int(time)) + " to " + str(int(time)+1)
			previous_time = time
			total_count = int(count)


	except ValueError as e:
		continue

# Print the last one
if total_count > maxtime_count:
	maxtime_count = total_count
	maxtime = "From " + str(int(time)) + " to " + str(int(time)+1)

print maxtime + " is the peak hour with " + str(maxtime_count) + " posts."


