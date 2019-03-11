#!/usr/bin/env python3 
import sys
import os
import random
import json
import operator
import rnr_utils


#A quick script to check for inconsistent ability names.
if __name__ == '__main__':
  rnr_utils.load_Rangers_And_Ruffians_Data()
  races = rnr_utils.race_data
  classes = rnr_utils.class_data
  abilities = rnr_utils.ability_dict

  print("The following abilities referenced by class or race.json cannot be found in abilities.json:")
  for key, values in races.items():
    for ability in values['abilities']:
      if not ability in abilities.keys():
        print("\tcouldn't find {0}".format(ability))

  for key, values in classes.items():
    for ability in values['abilities']:
      if not ability in abilities.keys():
        print("\tcouldn't find {0}".format(ability))

  print()
  print("The following abilities are unused by any race or class:")

  for ability in abilities.keys():
    found = False
    for key, values in races.items():
      if ability in values['abilities']:
        found = True
        break
    if not found:
      for key, values in classes.items():
        if ability in values['abilities']:
          found = True
          break
    if not found:
      print("\t{0} is used by no class or race".format(ability))

  print()
  changed = False
  for ability in abilities:
    if not "type" in abilities[ability]:
      abilities[ability]["type"] = "combat"
      print("{0} did not have a type.".format(ability))
      changed = True

  if changed:
    print('ERROR!')
    with open("json_files/abilities.json", 'w') as data_file:    
      json.dump(abilities, data_file, indent=4)

  print()
  print("The following ability types are in error:")
  for ability in abilities:
    if not abilities[ability]["type"] in ('combat', 'general', 'starting_item', 'choice', 'advantage', 'spellbook','rule','action'):
      print("\t{0} had type {1}".format(ability, abilities[ability]["type"]))

