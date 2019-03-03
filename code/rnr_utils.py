import json
import sys
import os
from collections import OrderedDict
from collections import Counter
import yaml
import random
import math

ability_dict = dict()
class_data = dict()
class_data_by_type = dict()
race_data = dict()
spell_books = dict()
compendium_of_spells = dict()

casting_classes = {
  'bard' : ["the_bard's_songbook",],
  'cleric' : ['the_book_of_healing',],
  'paladin' : ['the_book_of_healing',],
  'wizard' : ['the_novice_spellbook', "the_wizard's_addendum"],
  'sorcerer' : ['the_novice_spellbook', "the_sorcerer's_scrolls"],
  'druid' : ['the_novice_spellbook', "the_druid's_guidebook"],
  'necromancer' : ['the_macabre_manual',],
  'battle mage' : ['the_novice_spellbook',] 
}

tier_dict = {
  0:"new",
  1:"heroic",
  2:"legendary"
}

tier_to_number = {
  "new" : 0,
  "heroic" : 1,
  "legendary" : 2 
}

class rnr_entity:
    def __init__(self, name, abilities, stats, description,quote='', quote_author='',standings = ''):
      self.name = name
      #come back and see to this
      self.abilities = abilities
      self.stats = dict(stats)
      self.charisma = stats["Charisma"]
      self.dexterity = stats['Dexterity']
      self.strength = stats["Strength"]
      self.inner_fire = stats['Inner_Fire']
      self.intelligence = stats['Intelligence']
      self.luck = stats['Luck']
      self.perception = stats['Perception']
      self.vitality = stats['Vitality']
      self.description = description
      self.quote = quote
      self.quote_author = quote_author

    def pretty_print(self):
      print(self.name)
      print("chr: {0}".format(self.charisma))
      print("dex: {0}".format(self.dexterity))
      print("str: {0}".format(self.strength))
      print("inf: {0}".format(self.inner_fire))
      print("int: {0}".format(self.intelligence))
      print("luc: {0}".format(self.luck))
      print("per: {0}".format(self.perception))
      print("vit: {0}".format(self.vitality))

    def get_stat(self, stat_name,tier=1):
      stat_name = stat_name.lower()
      if stat_name == "charisma":
        return self.charisma if tier != 0 else math.ceil(self.charisma /2)
      elif stat_name == "dexterity":
        return self.dexterity if tier != 0 else math.ceil(self.dexterity /2)
      elif stat_name == "strength":
        return self.strength if tier != 0 else math.ceil(self.strength /2)
      elif stat_name == "inner_fire":
        return self.inner_fire if tier != 0 else math.ceil(self.inner_fire /2)
      elif stat_name == "intelligence":
        return self.intelligence if tier != 0 else math.ceil(self.intelligence /2) 
      elif stat_name == "luck":
        return self.luck
      elif stat_name == "perception":
        return self.perception
      elif stat_name == "vitality":
        return self.vitality
      else:
        print('Asked for bad stat {0}'.format(stat_name))
        return None

    def set_stat(self, stat_name, val):
      stat_name = stat_name.lower()
      if stat_name == "charisma":
        self.charisma = val
        self.stats['charisma'] = val
      elif stat_name == "dexterity":
        self.dexterity = val
        self.stats['dexterity'] = val
      elif stat_name == "strength":
        self.strength = val
        self.stats['strength'] = val
      elif stat_name == "inner_fire":
        self.inner_fire = val
        self.stats['inner_fire'] = val
      elif stat_name == "intelligence":
        self.intelligence = val
        self.stats['intelligence'] = val
      elif stat_name == "luck":
        self.luck = val
        self.stats['luck'] = val
      elif stat_name == "perception":
        self.perception = val
        self.stats['perception'] = val
      elif stat_name == "vitality":
        self.vitality = val
        self.stats['vitality'] = val

    def base_serialize(self):
      serial = dict()
      serial["stats"] = self.stats
      serial["name"] = self.name
      serial["abilities"] = filterAbilities(self.abilities, ability_dict)
      serial["description"] = self.description
      serial['quote'] = self.quote
      serial['quote_author'] = self.quote_author
      return serial

    def base_markdownify(self, image_path, emphasis):
      load_Rangers_And_Ruffians_Data()

      ret = ""
      lowername = self.name.lower()
      #relative path for now
      lowername = lowername.replace(' ', '_')
      if image_path != "":
        path_to_image = "{0}/{1}.jpg".format(image_path.replace(' ', '_'), lowername)
      else:
        path_to_image = ""
      description = self.description
      abilities = self.abilities

      ret = "{0} {1} \n".format(emphasis, self.name)
      if path_to_image != "":
        ret += '![{0}]({1}?raw=true "{2}") \n\n'.format(self.name, path_to_image, self.name)
      if description != "":
        ret += description + "  \n"
      # if standings != "":
      #   ret += "**Standings:** " + self.standings + "  \n\n"
      
      ret += "#### Abilities:   \n"
      abilities = filterAbilities(self.abilities, ability_dict)
      for key in ('combat', 'advantage', 'starting_item', 'choice','general'):
        if not key in abilities:
          continue
        ret += "##### {0}:   \n".format(mapAbilityType(key))
        for ability in abilities[key]:
          ret += "  * **{0}**: {1}  \n".format(ability[0], ability[1])
        ret += "    \n"
      ret += "\n##### Stats:  " + "  \n"
      for stat in self.stats:
        ret += "  * " +  stat + ": " + str(self.stats[stat]) + "  \n"
      ret += "   \n"
      return ret

    def __str__(self):
      ret_lis = [self.name,
      "chr : {0}".format(self.charisma), 
      "dex : {0}".format(self.dexterity),
      "str : {0}".format(self.strength),
      "inf : {0}".format(self.inner_fire),
      "int : {0}".format(self.intelligence),
      "lck : {0}".format(self.luck),
      "per : {0}".format(self.perception),
      "vit : {0}".format(self.vitality),
      '' ]
      ret = '\n'.join(ret_lis)
      return ret

    def get_health(self, tier=1):
      if tier==0:
        return 30 + self.vitality * 2
      elif tier==1:
        return 75 + self.vitality * 5
      elif tier==2:
        return 120 + self.vitality * 10
      else:
        return 75 + self.vitality * 5

    def tabbed_string(self, prefix='\t',tier=1):
      double_prefix = prefix+'\t'
      ret_lis = [
      prefix+self.name,
      double_prefix+"chr : {0}".format(self.get_stat('charisma',tier=tier)), 
      double_prefix+"dex : {0}".format(self.get_stat('dexterity',tier=tier)),
      double_prefix+"str : {0}".format(self.get_stat('strength',tier=tier)),
      double_prefix+"inf : {0}".format(self.get_stat('inner_fire',tier=tier)),
      double_prefix+"int : {0}".format(self.get_stat('intelligence',tier=tier)),
      double_prefix+"lck : {0}".format(self.get_stat('luck',tier=tier)),
      double_prefix+"per : {0}".format(self.get_stat('perception',tier=tier)),
      double_prefix+"vit : {0}".format(self.get_stat('vitality',tier=tier)),
      double_prefix+"tier 0 health: {0}".format(self.get_health(tier=0)),      
      double_prefix+"tier 1 health: {0}".format(self.get_health(tier=1)),
      double_prefix+"tier 2 health: {0}".format(self.get_health(tier=2)),     
      '' ]
      ret = '\n'.join(ret_lis)
      return ret

class rnr_class(rnr_entity):
    def __init__(self, name, abilities, stats, description, quote, quote_author, tier_1_info, tier_2_info, tier=1):
      base_stats = dict(stats)
      if tier == 1 or tier == 2:
        for stat, modifier in tier_1_info['stats'].items():
          base_stats[stat] += modifier
        if tier_1_info['abilities'] != None:
          abilities = abilities + tier_1_info['abilities']

      if tier == 2:
        for stat, modifier in tier_2_info['stats'].items():
          base_stats[stat] += modifier
        if tier_2_info['abilities'] != None:
          abilities = abilities + tier_2_info['abilities']
      
      self.tier = tier 
      super().__init__(name, abilities, base_stats, description, quote, quote_author) 

    def markdownify(self, image_path):
      return self.base_markdownify(image_path, '##')

    def serialize(self, male=False):
      serial = self.base_serialize()
      serial["path_to_image"] = "/static/images/class/{0}.jpg".format(self.name.lower())

      with open('../data/art.json','r') as art_json:
        art = json.load(art_json)

      serial['rights'] = art.get(self.name.lower(),None)
      return serial

class rnr_race(rnr_entity):
  def __init__(self, name, abilities, stats, description, quote, quote_author):
      super().__init__(name, abilities, stats, description, quote, quote_author) 

  def markdownify(self, image_path):
      return self.base_markdownify(image_path, '#')

  def serialize(self, male=False):
    serial = self.base_serialize()
    gender = "male" if male else "female"
    serial["path_to_image"] = "/static/images/race/{0}/{1}.jpg".format(gender, self.name.replace(' ','_').lower())
    with open('../data/art.json','r') as art_json:
        art = json.load(art_json)

    serial['rights'] = art.get('{1}_{0}'.format(gender, self.name.lower()), None)
    return serial

class rnr_character(rnr_entity):
  def __init__(self, character_name, character_origin, character_weakness, rnr_race_obj, rnr_class_obj, character_quote='', character_quote_author='', roll_stats=False):
    abilities = rnr_race_obj.abilities + rnr_class_obj.abilities
    
    new_stats = dict()

    for key, value in rnr_race_obj.stats.items():
      new_stats[key] = value + rnr_class_obj.stats[key]

    stats = new_stats
    
    if roll_stats:
      for stat in stats.keys():
        val = random.randint(1,6) + random.randint(1,6) - 7
        stats[stat] = val
      min_stat = min(stats, key=stats.get)
      final_roll = random.randint(1,6) + random.randint(1,6) - 7
      stats[min_stat] = final_roll if final_roll > stats[min_stat] else stats[min_stat]

      max_stat = max(stats, key=stats.get)
      final_roll = random.randint(1,6) + random.randint(1,6) - 7
      stats[max_stat] = final_roll if final_roll < stats[max_stat] else stats[max_stat]

    if character_name.strip() != '':
      character_name = "{0}: {1} {2}".format(character_name, rnr_race_obj.name, rnr_class_obj.name)
    else:
      character_name = "{0} {1}".format(rnr_race_obj.name, rnr_class_obj.name)
    super().__init__(character_name, abilities, stats, character_origin, character_quote, character_quote_author, character_weakness) 
    
    self.origin = character_origin
    self.weakness = character_weakness
    self.race = rnr_race_obj.name
    self.rnr_class = rnr_class_obj.name
    self.rnr_race_obj = rnr_race_obj
    self.rnr_class_obj = rnr_class_obj

  def markdownify(self, image_path=""):
    return self.base_markdownify(image_path, '#')

  def serialize(self):
    serial = self.base_serialize()
    serial["origin"] = self.origin
    serial['race'] = self.race
    serial['class'] = self.rnr_class
    serial['health'] = self.get_health(tier=self.rnr_class_obj.tier)
    return serial

  def get_health(self, tier = None):
    if tier == None:
      print('invoking with tier {0}'.format(tier_to_number[self.rnr_class_obj.tier]))
      return super(rnr_character, self).get_health(tier=tier_to_number[self.rnr_class_obj.tier])
    else:
      return super(rnr_character, self).get_health(tier=tier)
class rnr_ability:
  def __init__(self, name, description, type):
    self.name = name
    self.description = description
    self.type = type
   
def markdown_all_classes(data, ability_dict, image_path, outfile_name):
  first = True
  for class_type, details in sorted(data.items()):
    if class_type == 'CUT':
      continue
    mode = 'w' if first else 'a'
    first = False
    with open(outfile_name, mode) as outfile:
      outfile.write("# {0} \n".format(class_type.capitalize()))
    standard_md_out(details, ability_dict, image_path, outfile_name, '##')

def mardown_all_races(data, ability_dict, image_path, outfile_name):
  with open(outfile_name, 'w') as outfile:
    pass
  standard_md_out(data, ability_dict, image_path, outfile_name, '#')

def filterAbilities(abilities, ability_dict):
  filtered_abilities = dict()
  for ability in abilities:
    ability_type = ability_dict[ability]["type"]
    if not ability_type in filtered_abilities:
      filtered_abilities[ability_type] = list()
    filtered_abilities[ability_type].append([ability,ability_dict[ability]["description"]])
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

def convert_json_file_to_yml_file(input_file, output_file):
  try:
    with open(input_file) as data_file:
        d = json.load(data_file)
    with open(output_file, 'w') as outfile:
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
    dictionary[key] = values
  return dictionary

def get_all_spellbooks():
  load_Rangers_And_Ruffians_Data()
  return spell_books

def find_spell_by_name(spell):
  load_Rangers_And_Ruffians_Data()
  if spell in compendium_of_spells:
    return compendium_of_spells[spell]['level'], compendium_of_spells[spell]['details']
  else:
    return None, None

def gather_spells(spell_data):
  load_Rangers_And_Ruffians_Data()

  player_spellbook = dict()

  tmp_spells = dict()
  for spell in spell_data:
    level, data = find_spell_by_name(spell.replace('_',' '))
    #if data is None, the spell could not be found in the spellbook.   
    if data == None:
      print("Could not find {0}".format(spell))
      continue
    #put the spell in the player's spellbook.
    if not level in player_spellbook:
      player_spellbook[level] = dict()
    player_spellbook[level][spell] = data
  return player_spellbook


def load_Rangers_And_Ruffians_Data():
  global spell_books, ability_dict, race_data, class_data, class_data_by_type, spells

  if len(ability_dict.keys()) != 0:
    return

  ability_path = "../data/abilities.yml"
  class_path = "../data/final_class_tiered_working.yml"
  race_path = "../data/races.yml"
  spell_path = "../data/spells.yml"
  
  with open(spell_path) as data_file:
    spell_books = yaml.load(data_file)

  for spellbook, chapters in spell_books.items():
    for level, spells in chapters.items():
      for spell, details in spells.items():
        compendium_of_spells[spell] = dict()
        compendium_of_spells[spell]['level'] = level
        compendium_of_spells[spell]['details'] = details

  with open(race_path) as data_file:
    race_data = yaml.load(data_file)

  with open(class_path) as data_file:
    class_data_by_type = yaml.load(data_file)

  class_data_by_type.pop('CUT', None)

  for class_type, info in class_data_by_type.items():
    class_data.update(info)

  with open(ability_path) as data_file:
    ability_dict = yaml.load(data_file)


def get_all_class_names():
  load_Rangers_And_Ruffians_Data()
  return list(class_data.keys())

def get_all_race_names():
  load_Rangers_And_Ruffians_Data()
  return list(race_data.keys())

def get_all_stat_names():
  return ['Charisma','Dexterity','Strength','Inner_Fire','Intelligence','Luck','Perception','Vitality']


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

def load_all_race_objects(inflate_choice_stats=False):
  load_Rangers_And_Ruffians_Data()
  races = list()
  for race, info in race_data.items():
    #class_name, abilities, stats, description, standings
    if inflate_choice_stats and ('Choice Stat' in info['abilities'] or 'Greater Choice Stat' in info['abilities']):
      mod = 1 if 'Choice Stat' in info['abilities'] else 2
      for stat in ['Strength', 'Dexterity']:
        info['stats'][stat] += mod
        race_obj = rnr_race('{0} {1}'.format(stat, race), info['abilities'], info['stats'], info['description'], info['quote'], info['author'])
        races.append(race_obj)
        info['stats'][stat] -= mod
    else:
      race_obj = rnr_race(race, info['abilities'], info['stats'], info['description'], info['quote'], info['author'])
      races.append(race_obj)
  return races

def load_all_class_objects(inflate_choice_stats=False,tier=1):
  load_Rangers_And_Ruffians_Data() 
  rnr_classes = list()
  for c, info in class_data.items():
    #class_name, abilities, stats, description, standings
    if inflate_choice_stats and ('Choice Stat' in info['abilities'] or 'Greater Choice Stat' in info['abilities']):
      mod = 1 if 'Choice Stat' in info['abilities'] else 2
      for stat in ['Strength', 'Dexterity']:
        info['stats'][stat] += mod
        class_obj = rnr_class('{0} {1}'.format(stat, c), info['abilities'], info['stats'], info['description'], '','',info['heroic'],info['legendary'],tier=tier)
        rnr_classes.append(class_obj)
        info['stats'][stat] -= mod
    else:
      class_obj = rnr_class(c, info['abilities'], info['stats'], info['description'], '','',info['heroic'],info['legendary'],tier=tier)
      rnr_classes.append(class_obj)
  return rnr_classes

def load_all_class_objects_by_type(tier=1):
  ret = dict()
  for c_type, c_info in class_data_by_type.items():
    ret[c_type] = list()
    for c, info in c_info.items():
      #class_name, abilities, stats, description, standings
      class_obj = rnr_class(c, info['abilities'], info['stats'], info['description'], info['quote'], info['author'],info['heroic'],info['legendary'],tier=tier)
      ret[c_type].append(class_obj)
  return ret

def load_all_race_class_combos(inflate_choice_stats=False,tier=1):
  rnr_races = load_all_race_objects(inflate_choice_stats=inflate_choice_stats)
  rnr_classes = load_all_class_objects(inflate_choice_stats=inflate_choice_stats,tier=tier)

  lis = list()
  for race in rnr_races:
    for r_class in rnr_classes:
      character = rnr_character('', '', '', race, r_class)
      lis.append(character)
  return lis

def load_race(name):
  name = name.title()
  load_Rangers_And_Ruffians_Data()
  race = race_data[name]
  return rnr_race(name, race['abilities'], race['stats'], race['description'],race['quote'],race['author'])

def load_class(name,tier=1):
  name = name.title()
  r_class = find_class_info(name)
  return rnr_class(name, r_class['abilities'], r_class['stats'], r_class['description'],'','',r_class['heroic'], r_class['legendary'],tier=tier)

def load_race_class_with_names(race_name, class_name, name="", origin="", roll_stats=False, tier=1):
  if tier in [0,1,2]:
    tier = tier_dict[tier]

  race_name = race_name.title()
  class_name = class_name.title()
  race_obj = load_race(race_name)
  class_obj = load_class(class_name,tier=tier)

  return rnr_character(name, origin, '', race_obj, class_obj, roll_stats=roll_stats)

def load_race_class_with_objects(race_obj, class_obj, name="",origin=""):
  return rnr_character(name, origin, '', race_obj, class_obj)

def find_class_info(name):
  load_Rangers_And_Ruffians_Data()
  return class_data.get(name, None)

def load_combos_given_list(races, classes, tier=1):
  combos = list()
  for race in races:
    for rnr_class in classes:
      combos.append(load_race_class_with_names(race,rnr_class,tier=tier))
  return combos



    