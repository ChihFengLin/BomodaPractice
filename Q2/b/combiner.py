#!/usr/bin/python

# The object of this file is to remove duplicate id_time input from mapper.py
# and output a unique one to the reducer.py

import simplejson as json
import re
import sys

previous_id_time = ""
previous_time = ""
previous_count = ""
first = True
for line in sys.stdin:
	try:
		id_time, count = line.split("\t")
		if (first):
			previous_id_time = id_time
			id, previous_time = id_time.split(",")
			previous_count = count
			first = False

		if id_time != previous_id_time:
			print previous_time + "\t" + previous_count
			previous_id_time = id_time
			id, previous_time = id_time.split(",")
			previous_count = count

	except ValueError as e:
		continue

# Notice we have to print the last one
print previous_time + "\t" + previous_count