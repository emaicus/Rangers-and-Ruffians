#!/usr/bin/env python3 
import sys
import os
import random
import json
import operator

if __name__ == '__main__':

  races = dict()
  classes = dict()
  abilities = dict()

with open("races.json") as data_file:    
    races = json.load(data_file)

with open("classes.json") as data_file:    
    classes = json.load(data_file)

with open("abilities.json") as data_file:    
    abilities = json.load(data_file)

for key, values in races.items():
  for ability in values['abilities']:
    if not ability in abilities.keys():
      print("couldn't find {0}".format(ability))

for key, values in classes.items():
  for ability in values['abilities']:
    if not ability in abilities.keys():
      print("couldn't find {0}".format(ability))

