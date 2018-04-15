import json
import sys
import textwrap

def listKeyAndDescription(dictionary):
  num = 0
  print()
  for key in dictionary.keys():
    name = key
    description = dictionary[key]["description"]
    name_and_desc = "{0}. {1}: {2}".format(num, name, description)
    print(textwrap.fill(name_and_desc, 80))
    print()
    num+=1

def getInput(question, answers):
  answer = ""
  while answer not in answers:
    answer = input(question)
  return answer

def raceSelect(races):
  answer = ""
  while answer not in races.keys():
    print("please select a race")
    listKeyAndDescription(races)
    answer = input("")
  return answer

def printAbilities(abilities, ability_dict):
  num = 0
  for ability in abilities:
    if not ability in ability_dict:
      print("ERROR: COULD NOT FIND {0}. Please tell an admin.".format(ability))
      continue
    str = "{0}. {1}: {2}".format(num, ability, ability_dict[ability]['description'])
    print(textwrap.fill(str, 80))
    print()
    num += 1

def raceMoreInfo(races, answer, ability_dict):
  print()
  print("You chose {0}".format(answer))
  print(races[answer]['description'])
  print()
  print("Abilities:")
  printAbilities(races[answer]['abilities'], ability_dict)
  print()
  print("Stats:")
  for stat, value in races[answer]['stats'].items():
    print("{0}: {1}".format(stat, value))
  print()
  answer = getInput("Do you want to play as a {0}?".format(answer), ["Yes", "No"])
  return answer

def classSelect(classes):
  answer = ""
  while answer not in classes.keys():
    print("please select a class")
    listKeyAndDescription(classes)
    answer = input("")
  return answer

def classMoreInfo(classes, answer, ability_dict):
  print()
  print(answer)
  print(classes[answer]['description'])
  print()
  print("Abilities:")
  printAbilities(classes[answer]['abilities'], ability_dict)
  print()
  print("Stats:")
  for stat, value in classes[answer]['stats'].items():
    print("{0}: {1}".format(stat, value))
  print()
  answer = getInput("Do you want to play as a {0}?".format(answer), ["Yes", "No"])
  return answer

if __name__ == "__main__":
  races = dict()
  classes = dict()
  abilities = dict()

  with open("races.json") as data_file:
    races = json.load(data_file)
  with open("classes.json") as data_file:
    classes = json.load(data_file)
  with open("abilities.json") as data_file:
    abilities = json.load(data_file)

  chosen_race = ""
  while chosen_race == "":
    chosen_race = raceSelect(races)
    answer = raceMoreInfo(races, chosen_race, abilities)
    if answer == "No":
      chosen_race = ""

  chosen_class = ""
  while chosen_class == "":
    chosen_class = classSelect(classes)
    answer = classMoreInfo(classes, chosen_class, abilities)
    if answer == "No":
      chosen_class = ""

  print("You chose to play as a {0} {1}".format(chosen_race, chosen_class))


