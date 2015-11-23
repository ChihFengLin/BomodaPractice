#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import heapq
import datetime as dt
import matplotlib.dates as mdates

def plot_figure(list, dates, brand):
	
	# Here is for zero padding
	y = []
	#pre_key = sorted(list)[0][0]
	#for key, value in sorted(list):
	#	num_zero = key - pre_key
	#	if num_zero >1 and num_zero <= 30:
	#		for i in xrange(1, num_zero):
	#			y.append(0)
	#	pre_key = key
	#	y.append(value)
	#x = np.arange(0,len(y),1)
	x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]
	x = sorted(x)

	for key, value in sorted(list):
		y.append(value)

	pl.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
	pl.gca().xaxis.set_major_locator(mdates.DayLocator(interval=4))
	pl.plot(x,y)
	pl.title("Total Metioned Posts Per Day: " + brand)
	pl.ylabel("Number of Posts")
	pl.gcf().autofmt_xdate()
	pl.show()




# Main
list_M = []
list_K = []
dates_M = []
dates_K = []

for line in sys.stdin:
	try:
		brand, date, count = line.split("\t")
		month, day, year = date.split()


		if (month == "Aug"):
			month = "08"
		elif (month == "Sep"):
			month = "09"
		elif (month == "Oct"):
			month = "10"
		else:
			continue
		

		if (brand == "Michael Kors"):
			heapq.heappush(list_M, (int(month+day), int(count)))
			dates_M.append(month + "/" + day + "/" + year)

		elif (brand == "Kate Spade"):
			heapq.heappush(list_K, (int(month+day), int(count)))
			dates_K.append(month + "/" + day + "/" + year)

	except ValueError as e:
		continue

# Plot figure
plot_figure(list_M, dates_M, "Michael Kors")
plot_figure(list_K, dates_K, "Kate Spade")




