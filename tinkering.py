import json
import sys
import os

def class_md_out(theFile, ability_dict):
  if theFile == "":
    sys.exit(0)
  with open(theFile) as class_file:    
    data = json.load(class_file)
    outfile = open("classes.md", 'w')
    standard_classes = data
    
    for name, details in standard_classes.items():
      lowername = name.lower()
      #relative path for now
      lowername = lowername.replace(' ', '_')
      path_to_image = "images/class/{0}.jpg".format(lowername)
      description = details["description"]
      if 'standings' in details:
        standings = details["standings"]
      else:
        standings = name + "s come in so many shapes, sizes, and belief sets that there is no set standing for them."
      abilities = details["abilities"]
      stats = details["stats"]
      outfile.write("# " + name + "  \n\n")
      outfile.write('![{0}]({1}?raw=true "{2}") \n'.format(name, path_to_image, name))
      print(name) 
      outfile.write(description + "  \n")
      print(description)
      outfile.write("**Standings:** " + standings + "  \n")
      print(standings)
      outfile.write("##### Abilities: " + "  \n")
      for ability in abilities:
        description = ability_dict[ability]["description"]
        outfile.write("  * **{0}**: {1}  \n".format(ability, description))
        print(ability, ": ", description)
      outfile.write("\n##### Stats:  " + "  \n")
      for stat in stats:
        outfile.write("  * " +  stat + ": " + str(stats[stat]) + "  \n")
        print(stat + " " + str(stats[stat]))
      outfile.write("   \n")
    outfile.close()

def main():
  if len(sys.argv) < 4:
    print("ERROR: include the name of the races.json, classes.json, and abilities.json files.")
    sys.exit(0)

  with open(sys.argv[3]) as data_file:
    ability_dict = json.load(data_file)

  with open(sys.argv[1]) as data_file:
    data = json.load(data_file)
    for gender in ("male", "female"):
      outfile = open("{0}_races.md".format(gender), 'w')
      standard_races = data
      for name, details in standard_races.items():

        lowername = name.lower()
        #relative path for now
        path_to_image = "images/race/{0}/{1}.jpg".format(gender, lowername)
        print(path_to_image)


        description = details["description"]
        standings = details["standings"]
        abilities = details["abilities"]
        stats = details["stats"]
        outfile.write("# " + name + "  \n")
        outfile.write('![{0}]({1}?raw=true "{2}") \n\n'.format(name, path_to_image, name))
        print(name)
        outfile.write(description + "  \n")
        print(description)
        outfile.write("**Standings:** " + standings + "  \n")
        print(standings)
        outfile.write("##### Abilities: " + "  \n")
        for ability in abilities:
          description = ability_dict[ability]["description"]
          outfile.write("  * **{0}**: {1}  \n".format(ability, description))
          print(ability, ": ", description)
        outfile.write("\n##### Stats:  " + "  \n")
        for stat in stats:
          outfile.write("  * " +  stat + ": " + str(stats[stat]) + "  \n")
          print(stat + " " + str(stats[stat]))
        outfile.write("\n")
    outfile.close()
    class_md_out(sys.argv[2], ability_dict)

if __name__ == "__main__":
    main()
