import json
import sys
import os

def readInJson(json_file):
  data = dict()
  with open(json_file) as data_file:
    data = json.load(data_file)
  return data

def mergeAbilities(dictionary, abilities):
  for key, values in dictionary.items():
    for i in range(len(values["abilities"])):
      ability = values["abilities"][i]
      values["abilities"][i] += ": " + abilities[ability]["description"]
      # print(values[abilities][i])
    dictionary[key] = values
  return dictionary

def makeCombinations(races, classes):
  race_class_combos = dict()
  for race, race_stats in races.items():
    for class_name, class_stats in classes.items():
      name = "{0}_{1}".format(race, class_name)
      race_class_stats = dict()
      for stat, value in race_stats["stats"].items():
        race_class_stats[stat] = value + class_stats["stats"][stat]
      race_class_abilities = race_stats["abilities"] + class_stats["abilities"]
      
      race_class_combos[name] = dict()
      race_class_combos[name]["stats"] = race_class_stats
      race_class_combos[name]["abilities"] = race_class_abilities
  return race_class_combos

# def getSort()


def main():
  #for now, these are the default names for these files. 
  class_json = "classes.json"
  race_json  = "races.json"
  abilities_json = "abilities.json"

  #load in each json
  abilities = readInJson(abilities_json)
  races = readInJson(race_json)
  classes = readInJson(class_json)

  #by default, races and classes only have ability names, not descriptions.
  # this merges in the descriptions.
  races = mergeAbilities(races, abilities)
  classes = mergeAbilities(classes, abilities)

  all_race_class_combos = makeCombinations(races, classes)
  # print(all_race_class_combos["Human_Barbarian"]['stats']['Strength'])
  
  for key, val in all_race_class_combos.items():
    if "Gnome" in key:
      print(key)
      for stat, value in val["stats"].items():
        print("\t{0}: {1}".format(stat, value))


  # for val in sorted(all_race_class_combos, key=lambda k: all_race_class_combos[k]['stats']["Charisma"]):
  #   print(val)
  #   for stat, value in all_race_class_combos[val]["stats"].items():
  #     print("\t{0}: {1}".format(stat, value))


if __name__ == "__main__":
    main()