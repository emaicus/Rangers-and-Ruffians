import json
import sys
import os
from collections import OrderedDict
import yaml

ability_dict = dict()
class_data = dict()
race_data = dict()

class rnr_class:
    def __init__(self, class_name, abilities, stats, description, standings):
      self.name = class_name
      #come back and see to this
      self.abilities = abilities
      self.charisma = stats["Charisma"]
      self.dexterity = stats['Dexterity']
      self.strength = stats["Strength"]
      self.inner_fire = stats['Inner_Fire']
      self.intelligence = stats['Intelligence']
      self.luck = stats['Luck']
      self.perception = stats['Perception']
      self.vitality = stats['Vitality']
      self.description = description
      self.standings = standings

    def pretty_print(self):
      print(self.name)
      print("CHR : {0}".format(self.charisma))
      print("DEX : {0}".format(self.dexterity))
      print("STR : {0}".format(self.strength))
      print("INF : {0}".format(self.inner_fire))
      print("INT : {0}".format(self.intelligence))
      print("LCK : {0}".format(self.luck))
      print("PER : {0}".format(self.perception))
      print("VIT : {0}".format(self.vitality))

    def get_stat(self, stat_name):
      stat_name = stat_name.lower()
      if stat_name == "charisma":
        return self.charisma
      elif stat_name == "dexterity":
        return self.dexterity
      elif stat_name == "strength":
        return self.strength
      elif stat_name == "inner_fire":
        return self.inner_fire
      elif stat_name == "intelligence":
        return self.intelligence
      elif stat_name == "luck":
        return self.luck
      elif stat_name == "perception":
        return self.perception
      elif stat_name == "vitality":
        return self.vitality
      else:
        return None

class rnr_race:
  def __init__(self, race_name, abilities, stats, description, standings):
    self.name = race_name
    #come back and see to this
    self.abilities = abilities
    self.charisma = stats["Charisma"]
    self.dexterity = stats['Dexterity']
    self.strength = stats["Strength"]
    self.inner_fire = stats['Inner_Fire']
    self.intelligence = stats['Intelligence']
    self.luck = stats['Luck']
    self.perception = stats['Perception']
    self.vitality = stats['Vitality']
    self.description = description
    self.standings = standings
 
  def pretty_print(self):
    print(self.name)
    print("CHR : {0}".format(self.charisma))
    print("DEX : {0}".format(self.dexterity))
    print("STR : {0}".format(self.strength))
    print("INF : {0}".format(self.inner_fire))
    print("INT : {0}".format(self.intelligence))
    print("LCK : {0}".format(self.luck))
    print("PER : {0}".format(self.perception))
    print("VIT : {0}".format(self.vitality))
  
  def get_stat(self, stat_name):
    stat_name = stat_name.lower()
    if stat_name == "charisma":
      return self.charisma
    elif stat_name == "dexterity":
      return self.dexterity
    elif stat_name == "strength":
      return self.strength
    elif stat_name == "inner_fire":
      return self.inner_fire
    elif stat_name == "intelligence":
      return self.intelligence
    elif stat_name == "luck":
      return self.luck
    elif stat_name == "perception":
      return self.perception
    elif stat_name == "vitality":
      return self.vitality
    else:
      return None

class rnr_character:
  def __init__(self, character_name, character_origin, character_weakness, rnr_race_obj, rnr_class_obj):
    self.name = character_name
    self.origin = character_origin
    self.weakness = character_weakness
    self.abilities = rnr_race_obj.abilities + rnr_class_obj.abilities
    self.race = rnr_race_obj.name
    self.rnr_class = rnr_class_obj.name
    self.charisma = rnr_race_obj.charisma + rnr_class_obj.charisma
    self.dexterity = rnr_race_obj.dexterity + rnr_class_obj.dexterity
    self.strength = rnr_race_obj.strength + rnr_class_obj.strength
    self.inner_fire = rnr_race_obj.inner_fire + rnr_class_obj.inner_fire
    self.intelligence = rnr_race_obj.intelligence + rnr_class_obj.intelligence
    self.luck = rnr_race_obj.luck + rnr_class_obj.luck
    self.perception = rnr_race_obj.perception + rnr_class_obj.perception
    self.vitality = rnr_race_obj.vitality + rnr_class_obj.vitality

    self.rnr_race_obj = rnr_race_obj
    self.rnr_class_obj = rnr_class_obj
    
  def pretty_print(self):
    print(self.name)
    print(self.origin)
    print(self.weakness)
    print(self.race)
    print(self.rnr_class)
    print("CHR : {0}".format(self.charisma))
    print("DEX : {0}".format(self.dexterity))
    print("STR : {0}".format(self.strength))
    print("INF : {0}".format(self.inner_fire))
    print("INT : {0}".format(self.intelligence))
    print("LCK : {0}".format(self.luck))
    print("PER : {0}".format(self.perception))
    print("VIT : {0}".format(self.vitality))

  def get_stat(self, stat_name):
    stat_name = stat_name.lower()
    if stat_name == "charisma":
      return self.charisma
    elif stat_name == "dexterity":
      return self.dexterity
    elif stat_name == "strength":
      return self.strength
    elif stat_name == "inner_fire":
      return self.inner_fire
    elif stat_name == "intelligence":
      return self.intelligence
    elif stat_name == "luck":
      return self.luck
    elif stat_name == "perception":
      return self.perception
    elif stat_name == "vitality":
      return self.vitality
    else:
      return None

def convert_json_file_to_yml_file(input_file, output_file):
  try:
    with open(input_file) as data_file:
        d = json.load(data_file)
    with open('output_file', 'w') as outfile:
        yaml.dump(d, outfile, default_flow_style=False)
  except Exception as e:
    print("ERROR: could not save {0} to {1} as a yml file".format(input_file, output_file))

def printLogo():
  print()
  print("__________ ")
  print("\\______   \\_____    ____    ____   ___________  ______ ")
  print(" |       _/\\__  \\  /    \\  / ___\\_/ __ \\_  __ \\/  ___/  ")
  print(" |    |   \\ / __ \\|   |  \\/ /_/  >  ___/|  | \\/\\___ \\   ")
  print(" |____|_  /(____  /___|  /\\___  / \\___  >__|  /____  >  ")
  print("        \\/      \\/     \\//_____/      \\/           \\/    ")
  print("                   .___                                ")
  print("_____    ____    __| _/                                ")
  print("\\__  \\  /    \\  / __ |                                 ")
  print(" / __ \\|   |  \\/ /_/ |                                 ")
  print("(____  /___|  /\\____ |                                 ")
  print("     \\/     \\/      \\/                                 ")
  print("__________        _____  _____.__                      ")
  print("\\______   \\__ ___/ ____\\/ ____\\__|____    ____   ______")
  print(" |       _/  |  \\   __\\\\   __\\|  \\__  \\  /    \\ /  ___/")
  print(" |    |   \\  |  /|  |   |  |  |  |/ __ \\|   |  \\___ \\ ")
  print(" |____|_  /____/ |__|   |__|  |__(____  /___|  /____  >")
  print("        \\/                            \\/     \\/     \\/ ")
  print()

#Rewrite
def mergeAbilities(dictionary, abilities):
  for key, values in dictionary.items():
    for i in range(len(values["abilities"])):
      ability = values["abilities"][i]
      values["abilities"][i] += ": " + abilities[ability]["description"]
      # print(values[abilities][i])
    dictionary[key] = values
  return dictionary

def load_Rangers_And_Ruffians_Data():
  global ability_dict, race_data, class_data

  if len(ability_dict.keys()) != 0:
    return

  ability_path = "../data/abilities.yml"
  class_path = "../data/classes.yml"
  race_path = "../data/races.yml"
  
  with open(race_path) as data_file:
    race_data = yaml.load(data_file)

  with open(class_path) as data_file:
    class_data = yaml.load(data_file)

  with open(ability_path) as data_file:
    ability_dict = yaml.load(data_file)

def get_all_class_names():
  load_Rangers_And_Ruffians_Data()
  lis = list()
  for class_type, details in class_data.items():
    if class_type == 'CUT':
      continue
    lis = lis + list(class_data[class_type].keys())
  return lis

def get_all_race_names():
  load_Rangers_And_Ruffians_Data()
  return list(race_data.keys())

#Given question and options, asks the question and won't return until an option is chosen.
# if boring is true, boring question is given instead.
def answerQuestion(question, options, boring_question='', boring=False):
  answer = ""
  q = boring_question if boring else question
  while not answer in options:
    answer = input(q + " ({0})\n".format(','.join(map(str, options)))).strip()
  print()

  return answer.strip()

#Given a question, asks the question. In fancy print, options should be a list of
# length 2 lists. Each list contains a longform response in position 0, and a 
# short response in position 1. 
def answerQuestionFancy(question, options, boring_question='',boring=False):
  answer = ""
  actual_options = list()
  screen_options = list()
  for option in options:
    actual_options.append(option[1])
    if not boring:
      screen_options.append("{0} ({1})".format(option[0], option[1]))
    else:
      screen_options.append(option[1])
  while not answer in actual_options:
    if boring:
      print(boring_question)
    else:
      print(question)
    print()
    answer = input("{0}\n".format('\n'.join(map(str, screen_options)))).strip()
  print()
  return answer.strip()

#Delay printing a line for delay seconds.
def delayPrint(line, delay=1):
  print(line)
  sys.stdout.flush()
  time.sleep(delay)

#A simple confirmation dialog.
def confirm(question, yes, no, boring=False):
  answer = answerQuestionFancy(question, [yes, no], boring=boring)
  return True if answer == yes[1] else False

#Given options, the user is prompted to remove options until they are finished. 
def removeOptions(options):
  answer = ""
  default = options[0]
  options.append("finished")

  while answer != "finished":
    answer = answerQuestion("All right, give me the name of one you want to remove", options,"Which do you want to remove?")
    options.remove(answer)

    if len(options) == 0:
      delayPrint("Hey there! You just removed everything! Are you messing with the program?",3)
      delayPrint("That's kind of a low thing to do!",3)
      delayPrint("How do you think that reflects on you as a person!",3)
      delayPrint("Probably pretty poorly!",3)
      delayPrint("All I wanted to do was to give you a nice way to make rangers and ruffians characters!",3)
      delayPrint("And you defied me! And you're not even sorry!",3)
      for i in range(5):
        print('.', end=" ")
        sys.stdout.flush()
        time.sleep(1)
      print()
      delayPrint("Fine. Have it your way.",5)
      options.append(default)
      answer = finished
  return options

def load_all_race_objects():
  load_Rangers_And_Ruffians_Data()
  races = list()
  for race, info in race_data.items():
    #class_name, abilities, stats, description, standings
    race_obj = rnr_class(race, info['abilities'], info['stats'], info['description'], info['standings'])
    races.append(race_obj)
  return races

def load_all_class_objects():
  load_Rangers_And_Ruffians_Data() 
  rnr_classes = list()
  for c_type, c_info in class_data.items():
    for c, info in c_info.items():
      #class_name, abilities, stats, description, standings
      class_obj = rnr_class(c, info['abilities'], info['stats'], info['description'], info['standings'])
      rnr_classes.append(class_obj)
  return rnr_classes

def load_all_race_class_combos():
  rnr_races = load_all_race_objects()
  rnr_classes = load_all_class_objects()

  lis = list()
  for race in rnr_races:
    for r_class in rnr_classes:
      character = rnr_character('', '', '', race, r_class)
      lis.append(character)
  return lis


def load_race(name):
  load_Rangers_And_Ruffians_Data()
  race = race_data[name]
  return rnr_race(name, race['abilities'], race['stats'], race['description'], race['standings'])

def load_class(name):
  r_class = find_class_info(name)
  return rnr_class(name, r_class['abilities'], r_class['stats'], r_class['description'], r_class['standings'])

def load_race_class_with_names(race_name, class_name):
  pass

def load_race_class_with_objects(race_obj, class_obj):
  pass


def find_class_info(name):
  load_Rangers_And_Ruffians_Data()
  for t in class_data.keys():
    if t == "CUT":
      continue
    for c, info in class_data[t].items():
      if c == name:
        return info
  return None





    