#!/usr/bin/python

# The object of this file is to merge the same brand and accumulate the count number

import simplejson as json
import re
import sys


total_count = 0
previous_brand = ""
first = True
for line in sys.stdin:
	try:
		brand, count = line.split("\t")
		if (first):
			previous_brand = brand
			first = False
		
		total_count += int(count)

		if brand != previous_brand:
			print previous_brand + "\t" + str(total_count)
			previous_brand = brand
			total_count = int(count)


	except ValueError as e:
		continue

# Print the last one
print previous_brand + "\t" + str(total_count)