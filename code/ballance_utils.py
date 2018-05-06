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

def generate_all_stats(combos, races, classes, stats):
  if not os.path.exists("dump_all"):
    os.makedirs("dump_all")

  #get the data for all classes.
  with open("dump_all/class_data.txt", 'w') as outfile:
    for class_name in classes:
      outfile.write("\n\nDetails for all {0}s\n".format(class_name))
      for combo_name, val in combos.items():
        if class_name in combo_name:
          outfile.write("{0}\n".format(combo_name))
          for stat, value in val["stats"].items():
            outfile.write("\t{0}: {1}\n".format(stat, value))
  #get the data for all races.
  with open("dump_all/race.txt", 'w') as outfile:
    for race in races:
      outfile.write("\n\nDetails for all {0}s\n".format(race))
      for combo_name, val in combos.items():
        if race in combo_name:
          outfile.write("{0}\n".format(combo_name))
          for stat, value in val["stats"].items():
            outfile.write("\t{0}: {1}\n".format(stat, value)) 

  #get the data for all stats.
  for stat in stats:
    with open("dump_all/{0}.txt".format(stat), 'w') as outfile:
      for val in sorted(combos, key=lambda k: combos[k]['stats'][stat]):
        outfile.write("{0}\n".format(val))
        for name, value in combos[val]["stats"].items():
          outfile.write("\t{0}: {1}\n".format(name, value))


#Generate the race by race rankings.
def rankRaces(races, stats):
  with open("dump_all/race_rankings.txt", 'w') as outfile:
    for stat in stats:
      outfile.write("SORT BY: {0}\n".format(stat))
      for race_name in sorted(races, key=lambda k: races[k]['stats'][stat]):
        stat_value = races[race_name]["stats"][stat]
        outfile.write("\t{0}: {1}\n".format(race_name, stat_value))
      outfile.write("\n")

#Generate the race by race rankings.
def rankClasses(classes, stats):
  with open("dump_all/class_rankings.txt", 'w') as outfile:
    for stat in stats:
      outfile.write("SORT BY: {0}\n".format(stat))
      for class_name in sorted(classes, key=lambda k: classes[k]['stats'][stat]):
        stat_value = classes[class_name]["stats"][stat]
        outfile.write("\t{0}: {1}\n".format(class_name, stat_value))
      outfile.write("\n")

def main():
  #for now, these are the default names for these files. 
  class_json = "json_files/classes.json"
  race_json  = "json_files/races.json"
  abilities_json = "json_files/abilities.json"

  #load in each json
  abilities = readInJson(abilities_json)
  races = readInJson(race_json)
  classes = readInJson(class_json)

  #by default, races and classes only have ability names, not descriptions.
  # this merges in the descriptions.
  races = mergeAbilities(races, abilities)
  all_race_names = races.keys()
  classes = mergeAbilities(classes, abilities)
  all_class_names = classes.keys()
  all_stat_names = classes[next(iter(classes))]["stats"].keys()
  all_race_class_combos = makeCombinations(races, classes)
  # print(all_race_class_combos["Human_Barbarian"]['stats']['Strength'])
  
  generate_all_stats(all_race_class_combos, all_race_names, all_class_names, all_stat_names)
  rankRaces(races, all_stat_names)
  rankClasses(classes, all_stat_names)
  # for key, val in all_race_class_combos.items():
  #   if "Gnome" in key:
  #     print(key)
  #     for stat, value in val["stats"].items():
  #       print("\t{0}: {1}".format(stat, value))


  # for val in sorted(all_race_class_combos, key=lambda k: all_race_class_combos[k]['stats']["Charisma"]):
  #   print(val)
  #   for stat, value in all_race_class_combos[val]["stats"].items():
  #     print("\t{0}: {1}".format(stat, value))


if __name__ == "__main__":
    main()