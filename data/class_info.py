import json
import sys
import os
from collections import OrderedDict
from collections import Counter
import yaml
import random
import math

def sum_stats(one, two):
  result = dict()
  for key, val in one.items():
    if key in two:
      result[key] = val + two[key]
    else:
      result[key] = val

  for key, val in two.items():
    if key in one:
      continue
    else:
      result[key] = val

  return result

if __name__ == '__main__':
  with open('final_class_tiered_working.yml','r') as data_file:
    data = yaml.load(data_file)

  easy_info = dict()

  for class_type, classes in data.items():
    if class_type.lower() == 'cut':
      continue
    print(class_type)
    easy_info[class_type] = dict()
    
    for rnr_class, class_data in classes.items():
      easy_info[class_type][rnr_class] = dict()
      easy_info[class_type][rnr_class]['tier_0'] = class_data['stats']
      easy_info[class_type][rnr_class]['tier_1'] = sum_stats(class_data['stats'], class_data['tier_1']['stats'])

  with open('class_compare.yml', 'w') as outfile:
    yaml.dump(easy_info, outfile, default_flow_style=False)
