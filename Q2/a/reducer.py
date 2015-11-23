#!/usr/bin/python

import simplejson as json
import re
import sys


total_count = 0
previous_brand_date = ""
maxTable = {"Michael Kors":0, "Kate Spade":0}
maxdate_M = ""
maxdate_K = ""

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
			if (brand == "Michael Kors"):
				if (total_count > maxTable[brand]):
					maxTable.update({brand:total_count})
					maxdate_M = date
			elif (brand == "Kate Spade"):
				if (total_count > maxTable[brand]):
					maxTable.update({brand:total_count})
					maxdate_K = date
			previous_brand_date = brand_date
			total_count = int(count)


	except ValueError as e:
		continue

# Print the last one
brand, date = previous_brand_date.split(",")
if (brand == "Michael Kors"):
	if (total_count > maxTable[brand]):
		maxTable.update({brand:total_count})
		maxdate_M = date
elif (brand == "Kate Spade"):
	if (total_count > maxTable[brand]):
		maxTable.update({brand:total_count})
		maxdate_K = date

print "Michael Kors" + "\t" +  maxdate_M + "\t" + str(maxTable["Michael Kors"])
print "Kate Spade" + "\t" +  maxdate_K + "\t" + str(maxTable["Kate Spade"])

