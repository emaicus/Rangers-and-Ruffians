import json
import sys
import os
import yattag

def filterAbilities(abilities, ability_dict):
  filtered_abilities = dict()
  for ability in abilities:
    ability_type = ability_dict[ability]["type"]
    if not ability_type in filtered_abilities:
      filtered_abilities[ability_type] = list()
    filtered_abilities[ability_type].append(ability)
  return filtered_abilities

def standard_md_out(data, ability_dict, image_path, outfile_name):
  with open(outfile_name, 'w') as outfile:    
    for name, details in data.items():
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
      outfile.write("# " + name + "  \n")
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
        outfile.write("##### {0} Abilities:   \n".format(key))
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
  ability_path = "json_files/abilities.json"
  class_path = "json_files/classes.json"
  race_path = "json_files/races.json"
  
  with open(ability_path) as data_file:
    ability_dict = json.load(data_file)

  with open(class_path) as data_file:
    class_data = json.load(data_file)

  with open(race_path) as data_file:
    race_data = json.load(data_file)
  
  return ability_dict, class_data, race_data

def main():
  ability_dict, class_data, race_data = loadData()
  standard_md_out(class_data, ability_dict, "images/class", "classes.md")
  standard_md_out(race_data, ability_dict, "images/race/female", "female_races.md")
  standard_md_out(race_data, ability_dict, "images/race/male", "male_races.md")

if __name__ == "__main__":
    main()
