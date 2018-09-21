import json
import sys
import os
import yaml
import traceback

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
    for class_type, class_type_list in classes.items():
      for class_name, class_stats in class_type_list.items():
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
  if not os.path.exists("stat_output"):
    os.makedirs("stat_output")

  #get the data for all classes.
  with open("stat_output/class_data.txt", 'w') as outfile:
    for class_name in combine_classes(classes):
      outfile.write("\n\nDetails for all {0}s\n".format(class_name))
      for combo_name, val in combos.items():
        if class_name in combo_name:
          outfile.write("{0}\n".format(combo_name))
          for stat, value in val["stats"].items():
            outfile.write("\t{0}: {1}\n".format(stat, value))
  #get the data for all races.
  with open("stat_output/race.txt", 'w') as outfile:
    for race in races:
      outfile.write("\n\nDetails for all {0}s\n".format(race))
      for combo_name, val in combos.items():
        if race in combo_name:
          outfile.write("{0}\n".format(combo_name))
          for stat, value in val["stats"].items():
            outfile.write("\t{0}: {1}\n".format(stat, value)) 

  #get the data for all stats.
  for stat in stats:
    with open("stat_output/{0}.txt".format(stat), 'w') as outfile:
      for val in sorted(combos, key=lambda k: combos[k]['stats'][stat]):
        outfile.write("{0}\n".format(val))
        for name, value in combos[val]["stats"].items():
          outfile.write("\t{0}: {1}\n".format(name, value))


#Generate the race by race rankings.
def rankRaces(races, stats):
  with open("stat_output/race_rankings.txt", 'w') as outfile:
    for stat in stats:
      outfile.write("SORT BY: {0}\n".format(stat))
      for race_name in sorted(races, key=lambda k: races[k]['stats'][stat]):
        stat_value = races[race_name]["stats"][stat]
        outfile.write("\t{0}: {1}\n".format(race_name, stat_value))
      outfile.write("\n")

def combine_classes(classes):
  new_classes = dict()

  for class_type, info in classes.items():
    new_classes.update(info)
  return new_classes

#Generate the race by race rankings.
def rankClasses(classes, stats):
  with open("stat_output/class_rankings.txt", 'w') as outfile:
    combined_classes = combine_classes(classes)
    for stat in stats:
      outfile.write("SORT BY: {0}\n".format(stat))
      for class_name in sorted(combined_classes, key=lambda k: combined_classes[k]['stats'][stat]):
        stat_value = combined_classes[class_name]["stats"][stat]
        outfile.write("\t{0}: {1}\n".format(class_name, stat_value))
      outfile.write("\n")

def rankClassType(classes, stats):
  with open("stat_output/class_type_rankings.txt", 'w') as outfile:
    for class_type, info in classes.items():
      outfile.write("{0}\n".format(class_type.upper()))
      for stat in stats:
        outfile.write("SORT BY: {0}\n".format(stat))
        for class_name in sorted(info, key=lambda k: info[k]['stats'][stat]):
          stat_value = info[class_name]["stats"][stat]
          outfile.write("\t{0}: {1}\n".format(class_name, stat_value))
        outfile.write("\n")

def loadData():
  ability_path = "../data/abilities.yml"
  class_path = "../data/classes.yml"
  race_path = "../data/races.yml"
  
  with open(race_path) as data_file:
    race_data = yaml.load(data_file)

  with open(class_path) as data_file:
    class_data = yaml.load(data_file)

  with open(ability_path) as data_file:
    ability_dict = yaml.load(data_file)
  
  return ability_dict, class_data, race_data

def main():
  try:
    abilities, classes, races = loadData()
  except Exception as e:
    print("ERROR: Could not load data.")
    traceback.print_exc()
    sys.exit(1)

  #by default, races and classes only have ability names, not descriptions.
  # this merges in the descriptions.
  races = mergeAbilities(races, abilities)
  all_race_names = races.keys()
  for class_type, info in classes.items():
    mergeAbilities(info, abilities)

  all_class_names = classes.keys()
  all_stat_names = races[next(iter(races))]["stats"].keys()
  all_race_class_combos = makeCombinations(races, classes)
  # print(all_race_class_combos["Human_Barbarian"]['stats']['Strength'])
  
  print("Generating raw combinations...")
  generate_all_stats(all_race_class_combos, all_race_names, all_class_names, all_stat_names)
  print("Generating race rankings...")
  rankRaces(races, all_stat_names)
  print("Generating class rankings...")
  rankClasses(classes, all_stat_names)
  print("Ranking classes by type...")
  rankClassType(classes, all_stat_names)
  print("Done.")
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