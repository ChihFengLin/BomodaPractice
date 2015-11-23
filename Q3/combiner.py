#!/usr/bin/python

# The object of this file is to remove duplicate id_brand input from mapper.py
# and output a unique one to the reducer.py

import simplejson as json
import re
import sys

previous_id_brand = ""
previous_brand = ""
previous_count = ""
previous_text = ""
first = True
for line in sys.stdin:
	try:
		id_brand, text, count = line.split("\t")
		if (first):
			previous_id_brand = id_brand
			id, previous_brand = id_brand.split(",")
			previous_count = count
			previous_text = text
			first = False

		if id_brand != previous_id_brand:
			print previous_brand + "\t" + previous_text + "\t" + previous_count
			previous_id_brand = id_brand
			id, previous_brand = id_brand.split(",")
			previous_count = count
			previous_text = text

	except ValueError as e:
		continue

# Notice we have to print the last one
print previous_brand + "\t" + previous_text + "\t" + previous_count