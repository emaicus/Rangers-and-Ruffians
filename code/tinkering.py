import json
import sys
import os
from collections import OrderedDict
import yaml

def filterAbilities(abilities, ability_dict):
  filtered_abilities = dict()
  for ability in abilities:
    print(ability)
    print(ability_dict[ability])
    ability_type = ability_dict[ability]["type"]
    if not ability_type in filtered_abilities:
      filtered_abilities[ability_type] = list()
    filtered_abilities[ability_type].append(ability)
  return filtered_abilities

def mapAbilityType(abilitiy_type):
  if abilitiy_type == "combat":
    return "Combat Abilities"
  elif abilitiy_type == "advantage":
    return "Advantages"
  elif abilitiy_type == "starting_item":
    return "Starting Items"
  elif abilitiy_type == "choice":
    return "Choices"
  else:
    return "General Abilities"


  'combat', 'advantage', 'starting_item', 'choice','general'

def classHelper(data, ability_dict, image_path, outfile_name):
  first = True
  for class_type, details in sorted(data.items()):
    if class_type == 'CUT':
      continue
    mode = 'w' if first else 'a'
    first = False
    with open(outfile_name, mode) as outfile:
      outfile.write("# {0} \n".format(class_type.capitalize()))
    standard_md_out(details, ability_dict, image_path, outfile_name, '##')



def raceHelper(data, ability_dict, image_path, outfile_name):
  with open(outfile_name, 'w') as outfile:
    pass
  standard_md_out(data, ability_dict, image_path, outfile_name, '#')

def standard_md_out(data, ability_dict, image_path, outfile_name, emphasis):
  with open(outfile_name, 'a') as outfile:    
    for name, details in sorted(data.items()):
      print(name)
      print(json.dumps(details, indent=4))
      lowername = name.lower()
      #relative path for now
      lowername = lowername.replace(' ', '_')
      path_to_image = "{0}/{1}.jpg".format(image_path, lowername)
      description = details["description"]
      if 'standings' in details:
        standings = details["standings"]
      else:
        standings = name + "s come in so many shapes, sizes, and belief sets that there is no set standing for them."
      abilities = details["abilities"]
      stats = details["stats"]
      outfile.write("{0} {1} \n".format(emphasis, name))
      outfile.write('![{0}]({1}?raw=true "{2}") \n\n'.format(name, path_to_image, name))
      print(name) 
      outfile.write(description + "  \n")
      print(description)
      outfile.write("**Standings:** " + standings + "  \n")
      print(standings)
      outfile.write("#### Abilities:   \n")
      abilities = filterAbilities(abilities, ability_dict)
      for key in ('combat', 'advantage', 'starting_item', 'choice','general'):
        if not key in abilities:
          continue
        outfile.write("##### {0}:   \n".format(mapAbilityType(key)))
        for ability in abilities[key]:
          description = ability_dict[ability]["description"]
          outfile.write("  * **{0}**: {1}  \n".format(ability, description))
          print(ability, ": ", description)
        outfile.write("    \n")
      outfile.write("\n##### Stats:  " + "  \n")
      for stat in stats:
        outfile.write("  * " +  stat + ": " + str(stats[stat]) + "  \n")
        print(stat + " " + str(stats[stat]))
      outfile.write("   \n")

def loadData():
  ability_path = "yamls/abilities.yml"
  class_path = "yamls/classes.yml"
  race_path = "yamls/races.yml"
  
  with open(race_path) as data_file:
    race_data = yaml.load(data_file)

  with open(class_path) as data_file:
    class_data = yaml.load(data_file)

  with open(ability_path) as data_file:
    ability_dict = yaml.load(data_file)
  
  return ability_dict, class_data, race_data

def main():
  ability_dict, class_data, race_data = loadData()
  classHelper(class_data, ability_dict, "images/class", "classes.md")
  raceHelper(race_data, ability_dict, "images/race/female", "female_races.md")
  raceHelper(race_data, ability_dict, "images/race/male", "male_races.md")

if __name__ == "__main__":
    main()
