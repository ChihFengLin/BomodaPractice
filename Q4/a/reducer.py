#!/usr/bin/python

import simplejson as json
import re
import sys


total_count = 0
previous_brand_date = ""

first = True
for line in sys.stdin:
	try:
		brand_date, count = line.split("\t")
		if (first):
			previous_brand_date = brand_date
			first = False
		
		total_count += int(count)

		if brand_date != previous_brand_date:
			brand, date = previous_brand_date.split(",")
			print brand + "\t" + date + "\t" + str(total_count)
			previous_brand_date = brand_date
			total_count = int(count)


	except ValueError as e:
		continue

# Print the last one
brand, date = previous_brand_date.split(",")
print brand + "\t" + date + "\t" + str(total_count)


