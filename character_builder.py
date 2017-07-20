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
    answer = input("What do you want to know about? (stats, quit, summary, new character)\n")
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
    elif answer == "summary":
      print("We are goint to rank from worst to best in these categories: Tank, Mage")
      
      print("Sorting tanks")
      combos = sorted(combos, key=lambda k: k['stats']["Strength"] + k['stats']["Vitality"])
      with open("tankFile.txt", "w") as out:
        for combo in combos:
          out.write(combo["name"] + " Str:" + str(combo['stats']["Strength"]) + " Vit: " + str(combo['stats']["Vitality"]) + '\n')
      
      print("Sorting Mages")
      combos = sorted(combos, key=lambda k: k['stats']["Intelligence"] + k['stats']["Inner_Fire"])
      with open("Magefile.txt", "w") as out:
        for combo in combos:
          out.write(combo["name"] + " Int:" + str(combo['stats']["Intelligence"]) + " IF: " + str(combo['stats']["Inner_Fire"]) + '\n')
      
      print("Sorting Dex")
      combos = sorted(combos, key=lambda k: k['stats']["Dexterity"] + (k['stats']["Vitality"]/2))
      with open("dexFile.txt", "w") as out:
        for combo in combos:
         out.write(combo["name"] + " Dex:" + str(combo['stats']["Dexterity"]) + " Vit: " + str(combo['stats']["Vitality"]) +'\n')


if __name__ == '__main__':
  main()
