#!/usr/bin/python

# The object of this file is to remove duplicate id_brand input from mapper.py
# and output a unique one to the reducer.py

import simplejson as json
import re
import sys

previous_id_brand = ""
previous_brand = ""
previous_date = ""
previous_count = ""
first = True
for line in sys.stdin:
	try:
		id_brand, date, count = line.split("\t")
		if (first):
			previous_id_brand = id_brand
			previous_date = date
			id, previous_brand = id_brand.split(",")
			previous_count = count
			first = False

		if id_brand != previous_id_brand:
			print previous_brand + "," + previous_date + "\t" + previous_count
			previous_id_brand = id_brand
			previous_date = date
			id, previous_brand = id_brand.split(",")
			previous_count = count

	except ValueError as e:
		continue

# Notice we have to print the last one
print previous_brand + "," + previous_date + "\t" + previous_count
