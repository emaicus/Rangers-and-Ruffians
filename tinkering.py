import json
import sys

def class_md_out(theFile):
  if theFile == "":
    sys.exit(0)
  with open(sys.argv[1]) as class_file:    
    data = json.load(class_file)
    outfile = open("races.md", 'w')
    standard_classes = data["standard_classes"]
    for class in standard_classes:
      

def main():
  if len(sys.argv) < 2:
    print("ERROR: include the name of the races.json file.")
    sys.exit(0)
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
      outfile.write("#### " + name + "  \n")
      print(name) 
      outfile.write(description + "  \n")
      print(description)
      outfile.write("**Standings:** " + standings + "  \n")
      print(standings)
      outfile.write("##### Abilities: " + "  \n")
      for ability in abilities:
        outfile.write("  * " + ability + "  \n")
        print(ability)
      outfile.write("\n##### Stats:  " + "  \n")
      for stat in stats:
        outfile.write("  * " +  stat + ": " + stats[stat] + "  \n")
        print(stat + " " + stats[stat])
      outfile.close()

if __name__ == "__main__":
    main()