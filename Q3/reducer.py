#!/usr/bin/python

import simplejson as json
import re
import sys
import heapq

total_count = 0
previous_brand_word = ""
first = True
top_list_M = []
top_list_K = []

for line in sys.stdin:
	try:
		brand_word, count = line.split("\t")
		if (first):
			previous_brand_word = brand_word
			first = False
		
		total_count += int(count)

		if brand_word != previous_brand_word:
			brand, word = brand_word.split(",")
			if (brand == "Michael Kors"):
				heapq.heappush(top_list_M, (total_count, word.decode('utf-8')))
				if len(top_list_M) > 10:
					heapq.heappop(top_list_M)
			elif (brand == "Kate Spade"):
				heapq.heappush(top_list_K, (total_count, word.decode('utf-8')))
				if len(top_list_K) > 10:
					heapq.heappop(top_list_K)
			#print previous_brand_word + "\t" + str(total_count)
			previous_brand_word = brand_word
			total_count = int(count)


	except ValueError as e:
		continue

# Print the last one
#print previous_brand_word + "\t" + str(total_count)
brand, word = brand_word.split(",")
if (brand == "Michael Kors"):
	heapq.heappush(top_list_M, (total_count, word.decode('utf-8')))
	if len(top_list_M) > 10:
		heapq.heappop(top_list_M)
elif (brand == "Kate Spade"):
	heapq.heappush(top_list_K, (total_count, word.decode('utf-8')))
	if len(top_list_K) > 10:
		heapq.heappop(top_list_K)

print "Top 10 words associated with Michael Kors:"
print top_list_M
print "Top 10 words associated with Kate Spade:"
print top_list_K
