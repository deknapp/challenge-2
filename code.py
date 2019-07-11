import sys  

SLCSP_FILE_NAME = '../test_files/slcsp/slcsp.csv'
PLANS_FILE_NAME = '../test_files/slcsp/plans.csv'
ZIPCODE_FILE_NAME = '../test_files/slcsp/zips.csv'

# given a list of silver plans in an area, and the costs of each plan, 
# find the second lowest cost silver plan
def get_slcsp(silver_plan_to_cost_dict, plans):
  plan_cost_list = [[plan, silver_plan_to_cost_dict[plan]] for plan in plans]
  plan_cost_list = sorted(plan_cost_list, key=lambda kv: kv[1])
  if len(plan_cost_list) < 2:
    return '' 
  else:
    if len(plan_cost_list[1]) < 1:
      return ''
    return plan_cost_list[1][0]

handle = open(ZIPCODE_FILE_NAME, 'r')
lines = handle.readlines()
handle.close()
zipcode_dict = {}
for line in lines[1:]:
  split_line = line.split(',')
  zipcode_dict[split_line[0]] = split_line[4][:-1] 

handle = open(PLANS_FILE_NAME)
lines = handle.readlines()
handle.close()
silver_plan_to_cost_dict = {}
area_to_plans_dict = {}
for line in lines:
  split_line = line.split(',')
  if split_line[2] == 'Silver':
    silver_plan_to_cost_dict[split_line[0]] = split_line[3]
    area = split_line[4][:-1]
    if split_line[4] in area_to_plans_dict:
      area_to_plans_dict[area].append(split_line[0])
    else:
      area_to_plans_dict[area] = [split_line[0]]


handle = open(SLCSP_FILE_NAME, 'r')
lines = handle.readlines()
handle.close()
zipcodes = [line.split(',')[0] for line in lines][1:]
print(lines[0])
for zipcode in zipcodes:
  plan_area = zipcode_dict[zipcode]
  if plan_area in area_to_plans_dict:
    plans_in_area = area_to_plans_dict[plan_area]
    slcsp = get_slcsp(silver_plan_to_cost_dict, plans_in_area)
  print(zipcode + ',' + slcsp)
