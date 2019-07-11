import sys  

SLCSP_FILE_NAME = '../test_files/slcsp/slcsp.csv'
PLANS_FILE_NAME = '../test_files/slcsp/plans.csv'
ZIPCODE_FILE_NAME = '../test_files/slcsp/zips.csv'

handle = open(SLCSP_FILE_NAME, 'r')
lines = handle.readlines()
zipcodes = [line.split(',')[0] for line in lines][1:]
handle.close()

handle = open(ZIPCODE_FILE_NAME, 'r')
lines = handle.readlines()
zipcode_dict = {}
for line in lines[1:]:
  split_line = line.split(',')
  zipcode_dict[split_line[0]] = split_line[4]  

print(zipcode_dict)

handle = open(PLANS_FILE_NAME)
lines = handle.readlines()
silver_plan_to_cost_dict = {}
area_to_plans_dict = {}
for line in lines:
  split_line = line.split(',')
  if split_line[2] == 'Silver':
    silver_plan_to_cost_dict[split_line[0]] = split_line[3]
    if len(area_to_plans_dict[split_line[4]]) > 0:
      area_to_plans_dict[split_line[4]].append(split_line[0])
    else:
      area_to_plans_dict[split_line[4]] = [split_line[0]]



