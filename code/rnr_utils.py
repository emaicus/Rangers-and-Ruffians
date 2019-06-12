import json
import sys
import os
from collections import OrderedDict
from collections import Counter
import yaml
import random
import math
import traceback
import copy
import re
from collections import OrderedDict 
import time
from shutil import copyfile


CODE_DIRECTORY = os.path.dirname(__file__)
BASE_DIRECTORY = os.path.split(CODE_DIRECTORY)[0]
INSTALL_DIRECTORY = os.path.join(BASE_DIRECTORY, 'INSTALLED_DATA')
DATA_DIRECTORY = os.path.join(BASE_DIRECTORY, 'data')

GLOBAL_ABILITY_DICT = dict()
GLOBAL_CLASS_DATA = dict()
GLOBAL_CLASS_DATA_BY_TYPE = dict()
GLOBAL_RACE_DATA = dict()
GLOBAL_SPELL_BOOKS = dict()
GLOBAL_COMPENDIUM_OF_SPELLS = dict()

magical_classes = {
  'bard' : ["the_bard's_songbook",],
  'cleric' : ['the_book_of_healing',],
  'paladin' : ['the_book_of_healing',],
  'wizard' : ['the_novice_spellbook', "the_wizard's_addendum"],
  'sorcerer' : ['the_novice_spellbook', "the_sorcerer's_scrolls"],
  'druid' : ['the_novice_spellbook', "the_druid's_guidebook"],
  'necromancer' : ['the_macabre_manual',],
  'monk' : ['the_book_of_chi',],
  'battle_mage' : ['the_novice_spellbook',] 
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
        print('Asked for bad stat {0}'.format(stat_name))
        return None

    def base_serialize(self, verbose=False):
      serial = dict()
      serial["stats"] = self.stats
      serial["name"] = self.name.replace(' ', '_')
      serial["abilities"] = filterAbilities(self.abilities, verbose)
      serial["description"] = self.description
      serial['quote'] = self.quote
      serial['quote_author'] = self.quote_author
      return serial

    def base_markdownify(self, image_path, custom_chunk="",handbook=None):
      load_Rangers_And_Ruffians_Data()

      ret = ""
      lowername = self.name.lower().replace(' ', '_')
      description = self.description
      abilities = self.abilities

      ret = "# {0} \n".format(self.name.replace('_',' '))
      ret += '<div></div>\n<div></div>\n\n'
      
      if image_path != "":
        ret += "<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2/site/static/images/{0}?raw=true' style='width:350px' />\n\n".format(image_path)
        #ret += '![{0}]({1}?raw=true "{2}") \n\n'.format(self.name, image_path, self.name)
     
      if custom_chunk != "":
        ret += custom_chunk  
      if not handbook is None:
        for section in handbook["sections"]:
          ret += '### {0}\n'.format(section["title"])
          for subsection in section["subsections"]:
            if 'title' in subsection and subsection["title"] != '':
              ret += '#### {0}\n'.format(subsection["title"])
            ret += subsection["text"]
            ret += '\n\n'


      ret += '___\n'
      ret += '>## {0}\n'.format(self.name.replace('_',' '))
      ret += '> <div></div>\n'
      ret += '>\n'
      ret += '>*{0}*\n'.format(description)
      ret += '>___\n'
      ret += '>|VIT|STR|DEX|INT|INF|CHR|PER|LUK|\n'
      ret += '>|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n'
      ret += '|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|\n'.format(self.vitality,self.strength, self.dexterity, self.intelligence, self.inner_fire, self.charisma, self.perception, self.luck)
      ret += '>___\n'
      ret += '>#### Abilities:\n'
      abilities = filterAbilities(self.abilities)
      for key in ('rule', 'spellbook', 'choice','general', 'starting_item', 'advantage', 'combat'):
        if not key in abilities:
          continue
        ret += ">##### {0}:   \n".format(mapAbilityType(key))
        for ability in abilities[key]:
          ret += "> * ***{0}:*** {1}  \n".format(ability[0], ability[1])
        ret +='> <div></div>\n>\n'
      #ret += '```\n```\n'

      ret += "\\page\n"
      return ret

    def __str__(self):
      ret_list = []
      for stat in standard_stat_order():
        line = '{0} : {1}'.format(abbreviate_stat(stat), self.get_stat(stat))
        ret_list.append(line)
      ret_list.append('')
      return '\n'.join(ret_list)

    def tabbed_string(self, prefix='\t'):
      double_prefix = prefix+'\t'
      ret_list = list()
      ret_list.append('{0}{1}'.format(prefix, self.name))
      for stat in standard_stat_order():
        line = '{0}{1} : {2}'.format(double_prefix, abbreviate_stat(stat), self.get_stat(stat))
        ret_list.append(line)
      ret_list.append('')
      return '\n'.join(ret_list)

class rnr_class(rnr_entity):
    def __init__(self, name, level=0, subclass=""):

      class_data = get_rnr_class_data_with_name(name)
      if class_data == None:
        raise Exception('ERROR: Could not load class {0}'.format(name))
      stats = class_data['base_stats']
      abilities = class_data['base_abilities']

      spell_learning_dict = OrderedDict()
      self.spells_known = None

      self.handbook = class_data.get('handbook', None)
      for step in range(0,level+1):
        level_string = 'level_{0}'.format(step)
        if not level_string in class_data['levels']:
          print('ERROR: could not load level {0} in class {1}'.format(step, name))
          continue
        level_details = class_data['levels'][level_string]
        
        level_stats = level_details.get('stats', {})
        stats = combine_stats(stats, level_stats)
        abilities = abilities + level_details.get('abilities', [])
        if 'subclass_{0}_abilities'.format(subclass) in level_details:
          abilities = abilities + level_details['subclass_{0}_abilities'.format(subclass)]

        for ability in abilities:
          if bool(re.search('Level .* Spells', ability)) or ability in ["Fighting Techniques", "Master Fighting Techniques", "Legendary Fighting Techniques"]:
            if not ability in spell_learning_dict:
              spell_learning_dict[ability] = 0

        for key in spell_learning_dict.keys():
          spell_learning_dict[key] += 1

      if len(spell_learning_dict.keys()) > 0:
        spells_string = "As a level {0} {1}, you know ".format(level, name)
        length = len(spell_learning_dict.keys())
        i = 0
        for key, val in spell_learning_dict.items():
          i+=1
          if i == 1:
            spells_string = '{0} {1} {2}'.format(spells_string, val, key.lower())
          elif i == length:
            spells_string = '{0}, and {1} {2}.'.format(spells_string, val, key.lower())
          else:
            spells_string = '{0}, {1} {2}'.format(spells_string, val, key.lower())

        self.spells_known = ("Spells Known", spells_string)

      self.level = level
      self.subclass = subclass if subclass != "" else None
      super().__init__(name, abilities, stats, class_data['description'], '', '')

    def get_health(self):
      summed_level = sum(range(self.level+1))
      modifier = self.vitality * (self.level + 1)
      return 10 + summed_level + modifier

    def markdownify(self, male=False):
      gender_string = 'male' if male else 'female'
      if os.path.exists('../site/static/images/class/{0}/{1}.jpg'.format(gender_string,self.name.lower())):
        image_path = 'class/{0}/{1}.jpg'.format(gender_string,self.name.lower())
      else:
        image_path = 'class/{0}.jpg'.format(self.name.lower())

      return self.base_markdownify(image_path, handbook=self.handbook) + self.markdownify_level_sheet()

    def markdownify_level_sheet(self):
      ret = ""
      all_data = get_rnr_class_data_with_name(self.name)
      level_data = all_data['levels']
      for i in range(0,11):
        level = 'level_{0}'.format(i)
        ret += '### {0}\n\n'.format(level.replace('_',' '))
        ret += "<div style='margin-top:10px'></div>\n\n"
        if 'stats' in level_data[level]:
          ret += '#### Stats Bonuses  \n'
          ret += '* '
          for stat,val in level_data[level]['stats'].items():
            ret+= '**{0}:** {1} '.format(stat.replace('_',' ').title(), val)
          ret += '\n\n  \n'
        if 'abilities' in level_data[level]:
          ret += '#### New Abilities\n'
          ret += "<div style='margin-top:10px'></div>\n\n"
          level_abilities = filterAbilities(level_data[level]['abilities'])
          for key in ('rule', 'spellbook', 'action', 'choice','general', 'starting_item', 'advantage', 'combat'):
            if not key in level_abilities:
              continue
            ret += "##### {0}:   \n".format(mapAbilityType(key))
            for ability in level_abilities[key]:
              ret += "* ***{0}:*** {1}  \n".format(ability[0], ability[1])
            ret +='\n\n'
        for key in level_data[level].keys():
          if 'subclass' in key:
            ret += '#### {0} Abilities\n'.format(key.split('_')[1].title())
            ret += "<div style='margin-top:10px'></div>\n\n"
            sub_ability = filterAbilities(level_data[level][key])
            for key in ('rule', 'spellbook', 'action', 'choice','general', 'starting_item', 'advantage', 'combat'):
              if not key in sub_ability:
                continue
              ret += "##### {0}:   \n".format(mapAbilityType(key))
              for ability in sub_ability[key]:
                ret += "* ***{0}:*** {1}  \n".format(ability[0], ability[1])
              ret +='\n\n'
        #ret += '```\n```\n'

      ret += "\\page\n"
      return ret

    def serialize(self, male=False, verbose=False):
      serial = dict(self.base_serialize(verbose))
      gender_string = 'male' if male else 'female'
      if os.path.exists('static/images/class/{0}/{1}.jpg'.format(gender_string,self.name.lower())):
        serial["path_to_image"] = '/static/images/class/{0}/{1}.jpg'.format(gender_string,self.name.lower())
        art_request = '{0}_{1}'.format(gender_string, self.name.lower())
      else:
        serial["path_to_image"] = "/static/images/class/{0}.jpg".format(self.name.lower())
        art_request = self.name.lower()

      with open('../data/art.json','r') as art_json:
        art = json.load(art_json)

      serial['rights'] = art.get(art_request,None)

      all_data = get_rnr_class_data_with_name(self.name)
      serial['levels'] = all_data['levels']

      for level in serial['levels'].keys():
        if not 'abilities' in serial['levels'][level] or serial['levels'][level]['abilities'] is None:
          serial['levels'][level]['abilities'] = dict()
        else:
          serial['levels'][level]['abilities'] = filterAbilities(serial['levels'][level]['abilities'])
        for key in serial['levels'][level].keys():
          if 'subclass' in key:
            serial['levels'][level][key] = filterAbilities(serial['levels'][level][key])
      return serial

class rnr_race(rnr_entity):
  #Base constructor
  def __init__(self, name, subrace, abilities, stats, description, quote, quote_author, handbook):
    self.race_name = name
    self.subrace_name = subrace
    self.quote = quote
    self.quote_author = quote_author
    self.handbook = handbook
    super().__init__(name, abilities, stats, description, quote, quote_author)
    
  #simple constructor
  @classmethod
  def basic_constructor(cls, name, subrace):
    race_data = get_rnr_subrace_data(name, subrace)

    if race_data == None:
      raise Exception('ERROR: Could not load race {0} {1}'.format(name, subrace))
    return cls(name, subrace, race_data['abilities'], race_data['stats'], race_data['description'],
               race_data['quote'], race_data['author'], race_data.get('handbook', None))


  def markdownify(self,male=False):
    custom_chunk = '>{0}\n>\n>—{1}\n\n'.format(self.quote, self.quote_author)


    gender = "male" if male else "female"
    return self.base_markdownify("race/{0}/{1}.jpg".format(gender, self.subrace_name.replace(' ','_').lower()), custom_chunk=custom_chunk,handbook=self.handbook)

  def serialize(self, male=False, verbose=False):
    serial = self.base_serialize(verbose)
    gender = "male" if male else "female"

    #Fall back to race image if no subrace image exists.
    if os.path.exists("/static/images/race/{0}/{1}.jpg".format(gender, self.subrace_name.replace(' ','_').lower())):
      img_name = self.subrace_name.replace(' ','_').lower()
    else:
      img_name = self.race_name.replace(' ','_').lower()

    serial["path_to_image"] = "/static/images/race/{0}/{1}.jpg".format(gender, img_name)
    

    with open('../data/art.json','r') as art_json:
        art = json.load(art_json)

    serial['rights'] = art.get('{1}_{0}'.format(gender, self.name.lower().replace(' ', '_')), None)

    return serial

class rnr_character(rnr_entity):
  def __init__(self, character_name, race_name, subrace, class_name, level, male=False, subclass = '', character_origin='', character_weakness='',  character_quote='', character_quote_author=''):
    rnr_race_obj = rnr_race.basic_constructor(race_name, subrace)
    rnr_class_obj = rnr_class(class_name, level, subclass)
    
    abilities = rnr_race_obj.abilities + rnr_class_obj.abilities
    stats = combine_stats(rnr_class_obj.stats, rnr_race_obj.stats)

    final_character_name = "{0} {1}".format(rnr_race_obj.name, rnr_class_obj.name)
    if character_name.strip() != '':
      final_character_name = "{0}: {1}".format(character_name, final_character_name)
      
    super().__init__(final_character_name, abilities, stats, character_origin, character_quote, character_quote_author, character_weakness) 
    
    self.gender = 'male' if male==True else 'female'
    self.origin = character_origin
    self.weakness = character_weakness
    self.race = rnr_race_obj.race_name.replace(' ', '_')
    self.subrace = rnr_race_obj.subrace_name.replace(' ', '_')
    self.rnr_class = rnr_class_obj.name.replace(' ', '_')
    self.rnr_race_obj = rnr_race_obj
    self.rnr_class_obj = rnr_class_obj
    self.level = level
    self.subclass = subclass.replace(' ', '_')
    self.character_name = character_name.replace(' ', '_')

  def markdownify(self):
    ret += self.base_markdownify()
    return ret

  def serialize(self, verbose=False):
    serial = self.base_serialize(verbose)
    serial["origin"] = self.origin
    serial['race'] = self.race.lower()
    serial['class'] = self.rnr_class.lower()
    serial['health'] = self.get_health()
    serial['subrace'] = self.subrace
    serial['character_name'] = self.character_name
    serial['subclass'] = self.rnr_class_obj.subclass
    serial['gender'] = self.gender
    if not self.rnr_class_obj.spells_known is None:
      serial["abilities"]["choice"].append(self.rnr_class_obj.spells_known)
    return serial

  def get_health(self):
    summed_level = sum(range(self.level+1))
    modifier = self.vitality * (self.level + 1)
    return 10 + summed_level + modifier

class rnr_ability:
  def __init__(self, name, description, ability_type):
    self.name = name
    self.description = description
    self.type = ability_type


####################################################################################
#
# MARKDOWN AND FILE OUTPUT
#
####################################################################################

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

def markdown_spellbooks():
  ret = '# Spells  \n'
  spellbooks = get_all_spellbooks()
  for spellbook, chapters in spellbooks.items():
    ret += '## {0}  \n'.format(spellbook.replace('_',' '))
    for chapter, spell_list in chapters.items():
      ret += '### {0}  \n'.format(chapter.replace('_',' '))
      for spell, spell_data in spell_list.items():
        if not 'charisma_cost' in spell_data:
          if 'cost' in spell_data:
            ret += '* **{0}:** (Cost: {1}) {2}  \n'.format(spell.replace('_',' '), spell_data['cost'], spell_data['description'])
          else:
            ret += '* **{0}:** {1}  \n'.format(spell, spell_data['description'])
        else:
          ret += '* **{0}:** (Cost: {1}, Charisma Cost: {2}) {3}  \n'.format(spell, spell_data['cost'],spell_data['charisma_cost'], spell_data['description'])
    ret += "\\page\n"
  return ret


####################################################################################
#
# DATA WRANGLING
#
####################################################################################

#called by load_rangers_and_ruffians_data to install rangers to this directory.
def INSTALL_RANGERS_AND_RUFFIANS():
  if not os.path.exists(INSTALL_DIRECTORY):
    os.mkdir(INSTALL_DIRECTORY)

  timestamp_json_path = os.path.join(INSTALL_DIRECTORY, 'timestamps.json')
  
  try:
    with open(timestamp_json_path, 'r') as infile:
      timestamps = json.load(infile)
  except:
    print('Timestamp json did not exist. Creating one.')
    timestamps = dict()

  if not os.path.exists(DATA_DIRECTORY):
    print("ERROR! COULD NOT FIND THE DATA DIRECTORY {0}".format(DATA_DIRECTORY))
    sys.exit(1)

  modified = False
  for filename in os.listdir(DATA_DIRECTORY):
    source = os.path.join(DATA_DIRECTORY, filename)
    json_filename = '{0}.json'.format(filename.split('.')[0])
    destination = os.path.join(INSTALL_DIRECTORY, json_filename)
    if not '.yml' in filename:
      continue
    mod_time = os.path.getmtime(source)
    if not filename in timestamps:  
      print('No record of {0}. Installing'.format(filename))
      convert_yaml_file_to_json_file(source, destination)
      timestamps[filename] = mod_time
      modified = True
    elif mod_time != timestamps[filename]:
      print('{0} has been updated. Installing most recent version'.format(filename))
      convert_yaml_file_to_json_file(source, destination)
      timestamps[filename] = mod_time
      modified = True
  
  if modified:
    with open(timestamp_json_path, 'w') as outfile:
      json.dump(timestamps, outfile)


def load_Rangers_And_Ruffians_Data():
  global GLOBAL_ABILITY_DICT, GLOBAL_SPELL_BOOKS, GLOBAL_RACE_DATA, GLOBAL_CLASS_DATA, GLOBAL_CLASS_DATA_BY_TYPE, GLOBAL_COMPENDIUM_OF_SPELLS
  if len(GLOBAL_ABILITY_DICT.keys()) != 0:
    return

  start = time.time()

  INSTALL_RANGERS_AND_RUFFIANS()


  ability_path = os.path.join(INSTALL_DIRECTORY, 'abilities.json')
  class_path = os.path.join(INSTALL_DIRECTORY, 'classes.json')
  race_path = os.path.join(INSTALL_DIRECTORY, 'races.json')
  spell_path = os.path.join(INSTALL_DIRECTORY, 'merged_spells.json')
  
  with open(spell_path) as data_file:
    GLOBAL_SPELL_BOOKS = json.load(data_file)

  for spellbook, chapters in GLOBAL_SPELL_BOOKS.items():
    for level, spells in chapters.items():
      if spells == None:
        continue
      for spell, details in spells.items():
        GLOBAL_COMPENDIUM_OF_SPELLS[spell] = dict()
        GLOBAL_COMPENDIUM_OF_SPELLS[spell]['level'] = level
        GLOBAL_COMPENDIUM_OF_SPELLS[spell]['details'] = details

  with open(race_path) as data_file:
    GLOBAL_RACE_DATA = json.load(data_file)

  with open(class_path) as data_file:
    GLOBAL_CLASS_DATA_BY_TYPE = json.load(data_file)

  GLOBAL_CLASS_DATA_BY_TYPE.pop('CUT', None)

  for class_type, info in GLOBAL_CLASS_DATA_BY_TYPE.items():
    GLOBAL_CLASS_DATA.update(info)

  with open(ability_path) as data_file:
    GLOBAL_ABILITY_DICT = json.load(data_file)

  finish = time.time()
  #print('LOAD TIME: {0}(s)'.format(finish - start))

def filterAbilities(abilities, verbose=False):
  filt = "description" if verbose else "brief"
  global GLOBAL_ABILITY_DICT
  filtered_abilities = dict()
  for ability in abilities:
    ability_type = GLOBAL_ABILITY_DICT[ability]["type"]
    if not ability_type in filtered_abilities:
      filtered_abilities[ability_type] = list()
    filtered_abilities[ability_type].append([ability,GLOBAL_ABILITY_DICT[ability][filt]])
  return filtered_abilities

def abbreviate_stat(stat, upper=False):
  stat = stat.lower()
  if stat == 'dexterity':
    ret = 'dex'
  elif stat == 'strength':
    ret = 'str'
  elif stat == 'intelligence':
    ret = 'int'
  elif stat == 'inner fire' or stat == 'inner_fire':
    ret = 'inf'
  elif stat == 'vitality':
    ret = 'vit'
  elif stat == 'perception':
    ret = 'per'
  elif stat == 'charisma':
    ret = 'chr'
  elif stat == 'luck':
    ret = 'luk'
  else:
    print('ERROR: BAD STAT {0}'.format(stat))
    return None
  return ret.upper() if upper else ret

def standard_stat_order():
  return ['Strength', 'Dexterity', 'Intelligence', 'Inner_Fire', 'Charisma', 'Perception', 'Vitality', 'Luck']

def mapAbilityType(abilitiy_type):
  if abilitiy_type == "combat":
    return "Combat Abilities"
  elif abilitiy_type == "advantage":
    return "Advantages"
  elif abilitiy_type == "starting_item":
    return "Starting Items"
  elif abilitiy_type == "choice":
    return "Choices"
  elif abilitiy_type == 'rule':
    return "Rule"
  elif abilitiy_type == 'spellbook':
    return "Spellbook"
  elif abilitiy_type == 'action':
    return "Action" 
  else:
    return "General Abilities"

def combine_stats(stat_1, stat_2):
  new_stats = dict()
  for key, value in stat_1.items():
    new_stats[key] = value
    if key in stat_2.keys():
      new_stats[key] += stat_2[key]
  return new_stats

def convert_json_file_to_yml_file(input_file, output_file):
  try:
    with open(input_file) as data_file:
      d = json.load(data_file)
    with open(output_file, 'w') as outfile:
      yaml.dump(d, outfile, default_flow_style=False)
  except Exception as e:
    print("ERROR: could not save {0} to {1} as a yml file".format(input_file, output_file))

def convert_yaml_file_to_json_file(input_file, output_file):
  try:
    with open(input_file) as data_file:
      d = yaml.load(data_file)
    with open(output_file, 'w') as outfile:
      json.dump(d, outfile)
  except Exception as e:
    print("ERROR: could not save {0} to {1} as a yml file".format(input_file, output_file))

def mergeAbilities(dictionary, abilities):
  for key, values in dictionary.items():
    for i in range(len(values["abilities"])):
      ability = values["abilities"][i]
      values["abilities"][i] += ": " + abilities[ability]["description"]
    dictionary[key] = values
  return dictionary

def get_all_spellbooks():
  global GLOBAL_SPELL_BOOKS
  load_Rangers_And_Ruffians_Data()
  return copy.deepcopy(GLOBAL_SPELL_BOOKS)

def find_spell_by_name(spell):
  global GLOBAL_COMPENDIUM_OF_SPELLS
  load_Rangers_And_Ruffians_Data()
  if spell in GLOBAL_COMPENDIUM_OF_SPELLS:
    return copy.deepcopy(GLOBAL_COMPENDIUM_OF_SPELLS[spell]['level']), copy.deepcopy(GLOBAL_COMPENDIUM_OF_SPELLS[spell]['details'])
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

def get_rnr_class_data_with_name(name):
  global GLOBAL_CLASS_DATA

  load_Rangers_And_Ruffians_Data()
  if name.title() in GLOBAL_CLASS_DATA:
    return copy.deepcopy(GLOBAL_CLASS_DATA[name.title()])
  return None

def get_rnr_race_data(name):
  global GLOBAL_RACE_DATA

  load_Rangers_And_Ruffians_Data()
  if name.title() in GLOBAL_RACE_DATA:
    return copy.deepcopy(GLOBAL_RACE_DATA[name.title()])
  return None

def get_race_given_subrace(subrace):
  global GLOBAL_RACE_DATA

  load_Rangers_And_Ruffians_Data()
  for race, data in GLOBAL_RACE_DATA.items():
    if subrace.replace('_',' ').title() in data['subraces'].keys():
      return race
  return None

def get_subraces_for_race(race):
  global GLOBAL_RACE_DATA

  load_Rangers_And_Ruffians_Data()
  if race in GLOBAL_RACE_DATA:
    return list(GLOBAL_RACE_DATA[race].keys())
  return None

def get_rnr_subrace_data(name, subrace):
  global GLOBAL_RACE_DATA

  load_Rangers_And_Ruffians_Data()
  if name.replace('_',' ').title() in GLOBAL_RACE_DATA:
    if subrace.replace('_',' ').title() in GLOBAL_RACE_DATA[name.replace('_',' ').title()]['subraces']:
      return copy.deepcopy(GLOBAL_RACE_DATA[name.replace('_',' ').title()]['subraces'][subrace.replace('_',' ').title()])
  return None

def get_all_class_names(underscore=True):
  global GLOBAL_CLASS_DATA
  underscore_char = '_' if underscore else ' '

  load_Rangers_And_Ruffians_Data()
  class_names = list(GLOBAL_CLASS_DATA.keys())
  class_names = [c.replace(' ', underscore_char) for c in class_names]
  return class_names

def get_all_race_names(underscore=True):
  global GLOBAL_RACE_DATA
  load_Rangers_And_Ruffians_Data()
  underscore_char = '_' if underscore else ' '
  race_names = list()
  for race in GLOBAL_RACE_DATA.keys():
    for subrace in GLOBAL_RACE_DATA[race]['subraces']:
      race_names.append((race.replace(' ', underscore_char), subrace.replace(' ', underscore_char)))
  return race_names

def get_all_subrace_names(underscore=True):
  load_Rangers_And_Ruffians_Data()
  global GLOBAL_RACE_DATA
  underscore_char = '_' if underscore else ' '

  subrace_names = list()
  for race in GLOBAL_RACE_DATA.keys():
    for subrace in GLOBAL_RACE_DATA[race]['subraces']:
      subrace_names.append(subrace.replace(' ', underscore_char))
  return subrace_names

def get_all_stat_names():
  return ['Charisma','Dexterity','Strength','Inner_Fire','Intelligence','Luck','Perception','Vitality']

def get_all_rnr_abilities():
  global GLOBAL_ABILITY_DICT
  return copy.deepcopy(GLOBAL_ABILITY_DICT)

def get_rnr_class_dict():
  global GLOBAL_CLASS_DATA
  return copy.deepcopy(GLOBAL_CLASS_DATA)

def get_rnr_class_data_by_type():
  global GLOBAL_CLASS_DATA_BY_TYPE
  return copy.deepcopy(GLOBAL_CLASS_DATA_BY_TYPE)

def get_rnr_race_dict():
  global GLOBAL_RACE_DATA
  return copy.deepcopy(GLOBAL_RACE_DATA)

#returns a set of all subclass options a class has by a level
def subclasses_at_level(class_name, target_level):
  class_data = get_rnr_class_data_with_name(class_name)
  subclass_names = set()
  for level in range(0,target_level+1):
    level_string = 'level_{0}'.format(level)
    level_details = class_data['levels'][level_string]
    for key in level_details.keys():
      if 'subclass' in key:
        subclass_names.add(key.split('_')[1])
  return subclass_names

####################################################################################
#
# CLI Functions
#
####################################################################################

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

####################################################################################
#
# OBJECT LOADING FUNCTIONS
#
####################################################################################

def load_all_race_objects():
  global GLOBAL_RACE_DATA
  races = list()
  for race, data in GLOBAL_RACE_DATA.items():
    if 'subraces' in data:
      for subrace in data['subraces'].keys():
        try:
          new_race = rnr_race.basic_constructor(race, subrace)
        except: 
          traceback.print_exc()
          continue
        races.append(new_race)
  return races

#TODO doesn't take subclass into account.
def load_all_class_objects(level=0):
  rnr_classes = list()
  class_names = get_all_class_names()
  for class_name in class_names:
    try:
      new_class = rnr_class(class_name, level)
    except: 
      continue
    rnr_classes.append(new_class)
  return rnr_classes

def load_all_class_objects_by_type(level=0):
  global GLOBAL_CLASS_DATA_BY_TYPE
  ret = dict()
  for c_type, c_info in GLOBAL_CLASS_DATA_BY_TYPE.items():
    ret[c_type] = list()
    for name in c_info.keys():
      try:
        new_class = rnr_class(name, level)
      except: 
        continue
      ret[c_type].append(new_class)
  return ret

def load_all_characters(level=0):
  rnr_races = get_all_race_names()
  rnr_classes = get_all_class_names()

  lis = list()
  for race_name, subrace_name in rnr_races:
    for class_name in rnr_classes:
      character = rnr_character('', race_name, subrace_name, class_name, level)
      lis.append(character)
  return lis

'''
Races should be a list of tuples of the form (race, subrace)
'''
def load_combos_given_list(races, classes, level):
  characters = list()
  for race, subrace in races:
    for rnr_class in classes:
      try:
        character = rnr_character('', race_name, subrace, class_name, level)
      except:
        continue
      characters.append(character)
  return characters



    