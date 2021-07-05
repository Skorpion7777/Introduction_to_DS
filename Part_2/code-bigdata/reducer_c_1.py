from operator import itemgetter
import sys

#initialisation
init_patient = None
init_count = 0
patient = None

for line in sys.stdin:
    line = line.strip()
    patient, servicetime = line.split('\t', 1)
    servicetime = int(servicetime)
    
    if (init_patient != patient):
        if init_patient:
            print('%s\t%s' % (init_patient, servicetime))
        
        init_patient = patient
        init_count = servicetime
    else:
        servicetime += servicetime 

#output
if init_patient == patient:
    print('%s\t%s' % (init_patient, init_count))