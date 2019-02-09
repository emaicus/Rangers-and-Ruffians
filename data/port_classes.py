import json
import sys
import os
from collections import OrderedDict
from collections import Counter
import yaml
import random
import math

if __name__ == '__main__':
  with open('final_classes.yml','r') as data_file:
    data = yaml.load(data_file)

  for class_type, classes in data.items():
    print(class_type)
    for rnr_class, class_data in classes.items():
      print(rnr_class)
      class_data['tier_1'] = dict()
      class_data['tier_2'] = dict()
      class_data['tier_1']['stats'] = {
                                        "Charisma":  0,
                                        "Dexterity": 0,
                                        "Inner_Fire": 0,
                                        "Intelligence": 0,
                                        "Luck": 0,
                                        "Perception": 0,
                                        "Strength": 0,
                                        "Vitality": 0
                                      }
      class_data['tier_1']['abilities'] = ['generic_ability']
      class_data['tier_2']['stats'] = {
                                        "Charisma":  0,
                                        "Dexterity": 0,
                                        "Inner_Fire": 0,
                                        "Intelligence": 0,
                                        "Luck": 0,
                                        "Perception": 0,
                                        "Strength": 0,
                                        "Vitality": 0
                                      }
      class_data['tier_2']['abilities'] = ['generic_ability']
  with open('final_class_tiered.yml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)
