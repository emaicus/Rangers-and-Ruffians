#!/usr/bin/env python3 
import sys
import os
import random
import json
import operator

def main():

  races = classes = dict()
  with open("races.json") as data_file:    
    races = json.load(data_file)
  with open("classes.json") as data_file:    
    classes = json.load(data_file)
  combos = list();
  for race in races["standard_races"]:
    for rangers_class in classes["standard_classes"]:
      combo = {
        "name" : race["name"] + " " + rangers_class["names"][0],
        "stats" : {
          "Dexterity"     : race["stats"]["Dexterity"]    + rangers_class["stats"]["Dexterity"],
          "Strength"      : race["stats"]["Strength"]     + rangers_class["stats"]["Strength"],
          "Vitality"      : race["stats"]["Vitality"]     + rangers_class["stats"]["Vitality"],
          "Intelligence"  : race["stats"]["Intelligence"] + rangers_class["stats"]["Intelligence"],
          "Inner_Fire"    : race["stats"]["Inner_Fire"]   + rangers_class["stats"]["Inner_Fire"],
          "Charisma"      : race["stats"]["Charisma"]     + rangers_class["stats"]["Charisma"],
          "Luck"          : race["stats"]["Luck"]         + rangers_class["stats"]["Luck"],
          "Perception"    : race["stats"]["Perception"]   + rangers_class["stats"]["Perception"],
        },
        "abilities" : race["abilities"] + rangers_class["abilities"]
      }
      combos.append(combo)

  answer = "continue"
  while answer != "quit":
    answer = input("What do you want to know about? (stats, quit)\n")
    if answer == "stats":
      answer = input("Worst or best?\n")
      best = True
      if answer == "worst":
        best = False
      stat = input("Which stat do you want to know about?")

      try:
        combos = sorted(combos, key=lambda k: k['stats'][stat])
        if best:
          print("Best 10 for " + stat +":")
          vals = combos[-11:-1]
          for arg in reversed(vals):
            print(arg["name"] + ": " + str(arg['stats'][stat]))
        else:
          print("Worst 10 for " + stat +":")
          for arg in combos[0:10]:
            print(arg["name"] + ": " + str(arg['stats'][stat]))
      except Exception as e:
        print("ERROR:" +  str(e))


if __name__ == '__main__':
  main()
