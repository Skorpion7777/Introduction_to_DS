#!/usr/bin/env python

import sys

# input comes from STDIN
for line in sys.stdin:
	# remove whitespace and split row into values
    line_split = line.strip().split("\t")
    # assign case, activity, timestamp
    patient = line_split[0]
    modeltime = line_split[1]
    activity = line_split[2]
    age = line_split[3]
    servicetime = line_split[4]


    # write the results to STDOUT;
    # key: case, value: (timestamp,activity)
    print('%s\t%s\t%s\t%s\t%s' % (patient, modeltime, activity, age, servicetime))