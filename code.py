import sys  

SLCSP_FILE_NAME = sys.argv[1]
PLANS_FILE_NAME = sys.argv[2]
ZIPCODE_FILE_NAME = sys.argv[3]

# Given a list of silver plans in an area, and the costs of each plan, 
# find the second lowest cost silver plan.
def get_slcsp(silver_plan_to_cost_dict, plans):
  plan_cost_list = [[plan, silver_plan_to_cost_dict[plan]] for plan in plans]
  plan_cost_list = sorted(plan_cost_list, key=lambda kv: kv[1])
  if len(plan_cost_list) < 2:
    return '' 
  else:
    if len(plan_cost_list[1]) < 1:
      return ''
    return plan_cost_list[1][0]

# Get a dictionary of zipcodes to their rate areas.
handle = open(ZIPCODE_FILE_NAME, 'r')
lines = handle.readlines()
handle.close()
zipcode_dict = {}
for line in lines[1:]:
  split_line = line.split(',')
  area_index = split_line[4][:-1]
  area_state = split_line[1]
  area = area_state + area_index
  zipcode_dict[split_line[0]] = area 

# For the silver plans, get a dictionary of rate area to plans in the area, 
# and a dictionary of plans to costs.
handle = open(PLANS_FILE_NAME)
lines = handle.readlines()
handle.close()
silver_plan_to_cost_dict = {}
area_to_plans_dict = {}
for line in lines:
  split_line = line.split(',')
  if split_line[2] == 'Silver':
    plan_name = split_line[0]
    silver_plan_to_cost_dict[plan_name] = split_line[3]
    area_index = split_line[4][:-1]
    area_state = split_line[1]
    area = area_state + area_index
    if area in area_to_plans_dict:
      area_to_plans_dict[area].append(plan_name)
    else:
      area_to_plans_dict[area] = [plan_name]

# Use the dictionaries acquired above to get the SLCSP for each zipcode and its rate.
handle = open(SLCSP_FILE_NAME, 'r')
lines = handle.readlines()
print(lines[0]),
handle.close()
zipcodes = [line.split(',')[0] for line in lines][1:]
for zipcode in zipcodes:
  plan_area = zipcode_dict[zipcode]
  if plan_area in area_to_plans_dict:
    plans_in_area = area_to_plans_dict[plan_area]
    slcsp = get_slcsp(silver_plan_to_cost_dict, plans_in_area)
  if slcsp == '':
    rate = ''
  else:
    rate = silver_plan_to_cost_dict[slcsp] 
  print(zipcode + ',' + rate)
