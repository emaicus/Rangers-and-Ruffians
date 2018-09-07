import json
import sys
import os
from collections import OrderedDict
import yaml



with open('../json_files/abilities.json') as data_file:
    ability_dict = json.load(data_file)


with open('new_yamls/abilities.yml', 'w') as outfile:
    yaml.dump(ability_dict, outfile, default_flow_style=False)