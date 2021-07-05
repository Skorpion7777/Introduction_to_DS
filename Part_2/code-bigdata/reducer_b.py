#!/usr/bin/env python
import sys
import json

current_case = None

# input comes from STDIN
for line in sys.stdin:
	# remove whitespace and parse the input (case,(timestamp, activity)) we got from mapper.py
	line_split = line.strip().split("\t")
	patient, modeltime, activity, age, servicetime = line_split[0], line_split[1], line_split[2], line_split[3], line_split[4]
	# shuflling is done by Hadoop
	if patient != current_case:
		# write result to STDOUT
		if current_case:
			print('%s\t%s' % (current_case,json.dumps(current_trace)))
		# reset current trace
		current_case = patient
		current_trace = list()
		current_trace += [activity]
	else:
		current_trace += [activity]

# output the last word
if current_case == patient:
	print('%s\t%s' % (caseid,json.dumps(current_trace)))