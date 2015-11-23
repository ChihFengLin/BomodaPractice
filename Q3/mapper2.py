#!/usr/bin/python

import simplejson as json
import re
import sys
import jieba

for line in sys.stdin:
	try:
		brand, text, count = line.split("\t")
		chinese_list = jieba.cut(text)

		for word in chinese_list:
			print brand + "," + word.encode("utf8") + "\t" + str(count)
		
	except ValueError as e:
		continue