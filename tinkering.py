import json
import sys

def class_md_out(theFile, ability_dict):
  if theFile == "":
    sys.exit(0)
  with open(theFile) as class_file:    
    data = json.load(class_file)
    outfile = open("classes.md", 'w')
    standard_classes = data["standard_classes"]
    
    for rangers_class in standard_classes:
      name = rangers_class["names"][0]
      description = rangers_class["description"]
      if 'standings' in rangers_class:
        standings = rangers_class["standings"]
      else:
        standings = name + "s come in so many shapes, sizes, and belief sets that there is no set standing for them."
      abilities = rangers_class["abilities"]
      stats = rangers_class["stats"]
      outfile.write("### " + name + "  \n")
      print(name) 
      outfile.write(description + "  \n")
      print(description)
      outfile.write("**Standings:** " + standings + "  \n")
      print(standings)
      outfile.write("##### Abilities: " + "  \n")
      for ability in abilities:
        ability = getDescription(ability, ability_dict)
        outfile.write("  * " + ability + "  \n")
        print(ability)
      outfile.write("\n##### Stats:  " + "  \n")
      for stat in stats:
        outfile.write("  * " +  stat + ": " + str(stats[stat]) + "  \n")
        print(stat + " " + str(stats[stat]))
      outfile.write("   \n")
    outfile.close()
      
def getDescription(abilityName, dict):
  found = False
  description = ""
  abilities = dict['standard_abilities']
  for item in abilities:
    if abilityName in item["names"]:
      found = True
      description = item["description"]
      break

  if not found: 
    print("Couldn't find the " + str(abilityName) + " ability.")
    sys.exit(1)
  return abilityName + ": " + description

def main():
  if len(sys.argv) < 4:
    print("ERROR: include the name of the races.json, classes.json, and abilities.json files.")
    sys.exit(0)

  with open(sys.argv[3]) as data_file:
    ability_dict = json.load(data_file)

  with open(sys.argv[1]) as data_file:
    data = json.load(data_file)
    outfile = open("races.md", 'w')
    standard_races = data["standard_races"]
    for race in standard_races:
      name = race["name"]
      description = race["description"]
      standings = race["standings"]
      abilities = race["abilities"]
      stats = race["stats"]
      outfile.write("### " + name + "  \n")
      print(name)
      outfile.write(description + "  \n")
      print(description)
      outfile.write("**Standings:** " + standings + "  \n")
      print(standings)
      outfile.write("##### Abilities: " + "  \n")
      for ability in abilities:
        ability = getDescription(ability, ability_dict)
        outfile.write("  * " + ability + "  \n")
        print(ability)
      outfile.write("\n##### Stats:  " + "  \n")
      for stat in stats:
        outfile.write("  * " +  stat + ": " + str(stats[stat]) + "  \n")
        print(stat + " " + str(stats[stat]))
      outfile.write("\n")
  outfile.close()
  class_md_out(sys.argv[2], ability_dict)

if __name__ == "__main__":
    main()
