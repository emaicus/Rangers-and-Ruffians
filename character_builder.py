#!/usr/bin/env python3 
import sys
import os
import random
import json
import operator

def racePicker():
  with open("races.json") as data_file:    
    races = json.load(data_file)
  print("The current races are:")
  names = list()
  for race in races["standard_races"]:
    print("\t" + race["name"])
    list.append(race["name"])
  myRace = verifyInput("Which one would you like?", names)

def helper():
  with open("races.json") as data_file:    
    races = json.load(data_file)
  playStyles = ["Tank", "Fighter", "Mage", "Support", "Ranged Fighter"]
  playStyle = verifyInput("No worries. Do you have any ideas what sort of character you want to play?", playStyles)
  print("Ok, so you want to be a " + playStyle)
  if playStyle == "Tank":
    races = sorted(races, key=lambda k: k['stats']["Strength"] + k['stats']["Vitality"])
  elif playStyle == "Fighter":
    races = sorted(races, key=lambda k: max(k['stats']["Dexterity"], k['stats']["Strength"])+ k['stats']["Vitality"])
  elif playStyle == "Mage":
    races = sorted(races, key=lambda k: k['stats']["Intelligence"] + k['stats']["Inner_Fire"])
  elif playStyle == "Support":
    playStyle = verifyInput("So are you interested in being a healer, or do you want to be more active?", ("Healer", "Fighting Support"))
    if playStyle == "healer":
      print("Good on you! Here are some options:")
      options = list()
      races = sorted(races, key=lambda k: k['stats']["Intelligence"])
      options.append(races[0])
      print(races[0]["name"] + " Have the highest intelligence (" + races[0]["stats"]["Intelligence"] +"), this will make them very technical healers. Who are good at learning new spells.")
      options.append(races[0])
      races = sorted(races, key=lambda k: k['stats']["Inner_Fire"])
      print(races[0]["name"] + " Have the highest inner fire (" + races[0]["stats"]["Inner_Fire"] +"), this will make them powerful healers who can do more with simple spells.")
      races = sorted(races, key=lambda k: k['stats']["Intelligence"] + k['stats']["Inner_Fire"])
      options.append(races[0])
      print(races[0]["name"] + " Have the best mix (Inner fire: " + races[0]["stats"]["Inner_Fire"] +", Int: "+ races[0]["stats"]["Intelligence"] + "), which will make them versatile.")
      options.append("none")
      myRace = verifyInput("Do any of those sound good to you?", options)
      if myRace == "none":
        options = list()
        print("Hmmm... so you don't like any of those, huh?")
        races = sorted(races, key=lambda k: (k['stats']["Intelligence"]*2) + (k['stats']["Inner Fire"]*2) + k['stats']["Vitality"])
        options.append(races[0])


    else:
      races = sorted(races, key=lambda k: k['stats']["Intelligence"] + k['stats']["Inner_Fire"])

def picker():
  answer = verifyInput("Great! So do you know which race you want to play as?", ["y", "n"])
  if answer == "y":
    print("OHAI")
  else:
    playStyle = verifyInput("No worries. Do you have any ideas what sort of character you want to play?", playStyles)
    print("Ok, so you want to be a " + playStyle)

def character_help():
  
  with open("classes.json") as data_file:    
    classes = json.load(data_file)

  

  print("Hi, Let's build you a character!")
  myRace = "INVALID"
  answer = verifyInput("Do you already know all or part of what you want, or would you like help?", ["I know", "Help"])
  if answer == "I know":
    print("Done")
    
def printClass(dict, race, className):
  try:
    print("Dexterity: " + str(dict[race][className]["Dexterity"]))
    print("Strength: " + str(dict[race][className]["Strength"]))
    print("Vitality: " + str(dict[race][className]["Vitality"]))
    print("Intelligence: " + str(dict[race][className]["Intelligence"]))
    print("Inner_Fire: " + str(dict[race][className]["Inner_Fire"]))
    print("Charisma: " + str(dict[race][className]["Charisma"]))
    print("Luck: " + str(dict[race][className]["Luck"]))
    print("Perception: " + str(dict[race][className]["Perception"]))
  except Exception as e:
    if not race in dict:
      print("Race not in dict")
    else:
      if not className in dict[race]:
        print("class not in dict")
    print(e)
    print("Invalid class and race.")

def main():

  races = {}
  classes = {}
  with open("races.json") as data_file:    
    races = json.load(data_file)
  with open("classes.json") as data_file:    
    classes = json.load(data_file)
  combos = list();
  dict = {}
  for race in races["standard_races"]:
    for rangers_class in classes["standard_classes"]:
      name = race["name"]
      class_name = rangers_class["names"][0]
      if not name in dict:
        dict[name] = {}
      if not class_name in dict[name]:
        dict[name][class_name] = {}

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
      dict[name][class_name]["Dexterity"] = combo["stats"]["Dexterity"]
      dict[name][class_name]["Strength"] = combo["stats"]["Strength"]
      dict[name][class_name]["Vitality"] = combo["stats"]["Vitality"]
      dict[name][class_name]["Intelligence"] = combo["stats"]["Intelligence"]
      dict[name][class_name]["Inner_Fire"] = combo["stats"]["Inner_Fire"]
      dict[name][class_name]["Charisma"] = combo["stats"]["Charisma"]
      dict[name][class_name]["Luck"] = combo["stats"]["Luck"]
      dict[name][class_name]["Perception"] = combo["stats"]["Perception"]

  answer = "continue"
  while answer != "quit":
    answer = input("What do you want to know about? (stats, quit, summary, quick stats, new character)\n")
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
    elif answer == "quick stats":
      race = input("What race do you want quick stats for?")
      class_thing = input("What class do you want quick stats for?")
      printClass(dict, race, class_thing)
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
