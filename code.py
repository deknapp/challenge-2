import sys  

SLCSP_FILE_NAME = '../test_files/slcsp/slcsp.csv'
PLANS_FILE_NAME = '../test_files/slcsp/plans.csv'
ZIPCODE_FILE_NAME = '../test_files/slcsp/zips.csv'

handle = open(SLCSP_FILE_NAME, 'r')
lines = handle.readlines()
zipcodes = [line.split(',')[0] for line in lines][1:]


