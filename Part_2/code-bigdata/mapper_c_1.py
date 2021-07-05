import sys

for line in sys.stdin:
    line_split = line.strip().split("\t")

    #extraction of data
    patient = line_split[0]
    serv_time= line_split[4]

    #output
    print('%s\t%s' % (patient, serv_time))