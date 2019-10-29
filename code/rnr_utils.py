import json
import sys
import os
from collections import OrderedDict
import yaml
import traceback
import copy
import re
import time
from tqdm import tqdm
import random

CODE_DIRECTORY = os.path.dirname(__file__)
BASE_DIRECTORY = os.path.split(CODE_DIRECTORY)[0]
INSTALL_DIRECTORY = os.path.join(BASE_DIRECTORY, 'INSTALLED_DATA')
DATA_DIRECTORY = os.path.join(BASE_DIRECTORY, 'data')

GLOBAL_ART_DICTIONARY = dict()
GLOBAL_DESCRIPTIONS_DATABASE = dict()
GLOBAL_ABILITY_DICT = dict()
GLOBAL_CLASS_DATA = dict()
GLOBAL_CLASS_DATA_BY_TYPE = dict()
GLOBAL_RACE_DATA = dict()
GLOBAL_SPELL_BOOKS = dict()
GLOBAL_COMPENDIUM_OF_SPELLS = dict()

GLOBAL_MAGIC_CLASSES = dict()

GLOBAL_INITIAL_SPELL_ABILITIES = dict()

GLOBAL_SPELL_LEVEL_ABILITIES = dict()


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
      self.description = description
      self.quote = quote
      self.quote_author = quote_author

      self.effective_stats = dict()
      for key in self.stats.keys():
        self.effective_stats[key] = self.get_effective_stat(key)

    def pretty_print(self):
      print(self.name)
      print("chr: {0}".format(self.charisma))
      print("dex: {0}".format(self.dexterity))
      print("str: {0}".format(self.strength))
      print("inf: {0}".format(self.inner_fire))
      print("int: {0}".format(self.intelligence))
      print("luc: {0}".format(self.luck))
      print("per: {0}".format(self.perception))

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
      else:
        print('Asked for bad stat {0}'.format(stat_name))
        return None

    def get_effective_stat(self, stat_name):
      stat = self.get_stat(stat_name)
      if stat == None:
        return None
      # Remember if we should negate the stat at the end
      neg = True if stat < 0 else False
      # Absolute value to simplify code and help with rounding
      stat = abs(stat)
      # The first 3 in either direction count, then it takes 2
      neg_three = stat - 3
      val = stat if stat <= 3 else 3 + neg_three // 2
      # Add the negation back in
      return -val if neg else val 

    def base_serialize(self, verbose=False):
      serial = dict()
      serial["stats"] = self.stats
      serial["effective_stats"] = self.effective_stats
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
      ret += '>|STR|DEX|INT|INF|CHR|PER|LUK|\n'
      ret += '>|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n'
      ret += '|{0}|{1}|{2}|{3}|{4}|{5}|{6}|\n'.format(self.strength, self.dexterity, self.intelligence, self.inner_fire, self.charisma, self.perception, self.luck)
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
      ret_list = ['{0}'.format(self.name),]
      for stat in standard_stat_order():
        line = '  {0} : {1}'.format(abbreviate_stat(stat), self.get_stat(stat))
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
      self.health_die_pieces = class_data['health_die_pieces']
      self.handbook = class_data.get('handbook', None)

      # Gather up the abilities for all levels we've earned
      abilities = class_data.get('base_abilities', list())
      for step in range(0,level+1):
        level_string = 'level_{0}'.format(step)
        if not level_string in class_data['levels']:
          continue
        level_details = class_data['levels'][level_string]
        
        abilities = abilities + level_details.get('abilities', [])
        if not subclass is None and 'subclass_{0}_abilities'.format(subclass) in level_details:
          abilities = abilities + level_details['subclass_{0}_abilities'.format(subclass)]

      self.level = level
      self.subclass = subclass if subclass != "" else None
      super().__init__(name, abilities, stats, class_data['description'], '', '')
      self.spells_known = self.get_spell_counts()


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

      serial['rights'] = GLOBAL_ART_DICTIONARY.get(art_request,None)

      all_data = get_rnr_class_data_with_name(self.name)
      serial['levels'] = all_data['levels']
      serial['health_die_pieces'] = self.health_die_pieces

      for level in serial['levels'].keys():
        if not 'abilities' in serial['levels'][level] or serial['levels'][level]['abilities'] is None:
          serial['levels'][level]['abilities'] = dict()
        else:
          serial['levels'][level]['abilities'] = filterAbilities(serial['levels'][level]['abilities'])
        for key in serial['levels'][level].keys():
          if 'subclass' in key:
            serial['levels'][level][key] = filterAbilities(serial['levels'][level][key])
      return serial

    def get_spell_counts(self):
      global GLOBAL_SPELL_LEVEL_ABILITIES, GLOBAL_INITIAL_SPELL_ABILITIES

      class_data = get_rnr_class_data_with_name(self.name)
      if class_data == None:
        raise Exception('ERROR: Could not load class {0}'.format(self.name))
      abilities = class_data.get('base_abilities', list())

      spell_counts = OrderedDict()
      one_timers = set()

      for step in range(0,self.level+1):
        level_string = 'level_{0}'.format(step)
        if not level_string in class_data['levels']:
          print('ERROR: could not load level {0} in class {1}'.format(step, self.name))
          continue
        level_details = class_data['levels'][level_string]
        
        abilities = abilities + level_details.get('abilities', [])
        if not self.subclass is None and 'subclass_{0}_abilities'.format(self.subclass) in level_details:
          abilities = abilities + level_details['subclass_{0}_abilities'.format(self.subclass)]

        for ability in abilities:
          if ability in GLOBAL_SPELL_LEVEL_ABILITIES:
            if not GLOBAL_SPELL_LEVEL_ABILITIES[ability] in spell_counts:
              spell_counts[GLOBAL_SPELL_LEVEL_ABILITIES[ability]] = 0
          elif ability in GLOBAL_INITIAL_SPELL_ABILITIES and ability not in one_timers:
            one_timers.add(ability)
            for key, val in GLOBAL_INITIAL_SPELL_ABILITIES[ability].items():
              if not key in spell_counts:
                spell_counts[key] = 0
              spell_counts[key] += val

        for key in spell_counts.keys():
          spell_counts[key] += 1
      return spell_counts

    def get_spellbook_string(self):
      s = 'As a level {0} {1} you known'.format(self.level, self.name)
      i = 0
      for key, val in self.spells_known.items():
        if i != 0:
          if i != len(self.spells_known.keys()) -1:
            s += ','
          else:
            s += ', and'
        s = '{0} {1} {2}'.format(s, val, get_formal_spell_level_name(key))
        i += 1
      return s + '.'

class rnr_race(rnr_entity):
  #Base constructor
  def __init__(self, name, subrace, abilities, stats, description, quote, quote_author, handbook, health_die_pieces):
    self.race_name = name
    self.subrace_name = subrace
    self.quote = quote
    self.quote_author = quote_author
    self.handbook = handbook
    self.health_die_pieces =  health_die_pieces

    super().__init__(subrace, abilities, stats, description, quote, quote_author)
    
  #simple constructor
  @classmethod
  def basic_constructor(cls, name, subrace):
    race_data = get_rnr_subrace_data(name, subrace)

    if race_data == None:
      raise Exception('ERROR: Could not load race {0} {1}'.format(name, subrace))
    return cls(name, subrace, race_data['abilities'], race_data['stats'], race_data['description'],
               race_data['quote'], race_data['author'], race_data.get('handbook', None), race_data['health_die_pieces'])


  def markdownify(self,male=False):
    custom_chunk = '>{0}\n>\n>—{1}\n\n'.format(self.quote, self.quote_author)


    gender = "male" if male else "female"
    return self.base_markdownify("race/{0}/{1}.jpg".format(gender, self.subrace_name.replace(' ','_').lower()), custom_chunk=custom_chunk,handbook=self.handbook)

  def serialize(self, male=False, verbose=False):
    serial = self.base_serialize(verbose)
    gender = "male" if male else "female"

    #Fall back to race image if no subrace image exists.
    if os.path.exists("static/images/race/{0}/{1}.jpg".format(gender, self.subrace_name.replace(' ','_').lower())):
      img_name = self.subrace_name.replace(' ','_').lower()
    else:
      print('could not find {0}'.format("static/images/race/{0}/{1}.jpg".format(gender, self.subrace_name.replace(' ','_').lower())))
      img_name = self.race_name.replace(' ','_').lower()

    serial["path_to_image"] = "static/images/race/{0}/{1}.jpg".format(gender, img_name)
    print('path to image is {0}'.format(serial['path_to_image']))
    serial['health_die_pieces'] = self.health_die_pieces
    serial['rights'] = GLOBAL_ART_DICTIONARY.get('{1}_{0}'.format(gender, img_name), None)

    return serial

class rnr_character(rnr_entity):
  def __init__(self, character_name, race_name, subrace, class_name, level, male=False, subclass = None, character_origin='', character_weakness='',  character_quote='', character_quote_author=''):
    rnr_race_obj = rnr_race.basic_constructor(race_name, subrace)
    rnr_class_obj = rnr_class(class_name, level, subclass)
    
    abilities = rnr_race_obj.abilities + rnr_class_obj.abilities
    stats = combine_stats(rnr_class_obj.stats, rnr_race_obj.stats)

    final_character_name = "{0} {1}".format(rnr_race_obj.name, rnr_class_obj.name)
    if character_name.strip() != '':
      final_character_name = "{0}: {1}".format(character_name, final_character_name)
      
    self.health_dice = rnr_race_obj.health_die_pieces + rnr_class_obj.health_die_pieces

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
    self.subclass = subclass.replace(' ', '_') if not subclass is None else ''
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
    serial['health_dice'] = self.health_dice
    serial['subrace'] = self.subrace
    serial['character_name'] = self.character_name
    serial['subclass'] = self.rnr_class_obj.subclass
    serial['gender'] = self.gender
    serial['origin'] = self.origin
    serial['level'] = self.level
    # if not self.rnr_class_obj.spells_known is None and not len(self.rnr_class_obj.spells_known) == 0:
    #   if "choice" not in serial["abilities"]:
    #     serial["abilities"]["choice"] = list()
    #   spellstr = self.rnr_class_obj.get_spellbook_string()
    #   print("HERE")
    #   print(spellstr)
    #   serial["abilities"]["choice"].append(spellstr)
    return serial

  def get_health(self):
    summed_level = sum(range(self.level+1))
    base = self.health_dice * 2
    bonus = (self.health_dice // 2) * self.level
    return base + summed_level + bonus

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

  # A little clunky, but it allows the pretty progress bar
  reinstall = list()
  for filename in os.listdir(DATA_DIRECTORY):
    source = os.path.join(DATA_DIRECTORY, filename)
    if not '.yml' in filename:
      continue
    mod_time = os.path.getmtime(source)
    if not filename in timestamps:  
      reinstall.append((filename, 'installing {0}'.format(filename), mod_time))
    elif mod_time != timestamps[filename]:
      reinstall.append((filename, 'updating {0}'.format(filename), mod_time))

  if len(reinstall) > 0:
    pbar = tqdm(reinstall)
    for filename, description, mod_time in pbar:
      pbar.set_description(description)
      source = os.path.join(DATA_DIRECTORY, filename)
      json_filename = '{0}.json'.format(filename.split('.')[0])
      destination = os.path.join(INSTALL_DIRECTORY, json_filename)
      try:
        convert_yaml_file_to_json_file(source, destination)
      except Exception as e:
        print("ERROR: Could not install {0} to {1}".format(source, destination))
        raise
      timestamps[filename] = mod_time

    with open(timestamp_json_path, 'w') as outfile:
      json.dump(timestamps, outfile)
    pbar.close()


def load_Rangers_And_Ruffians_Data():
  global GLOBAL_ABILITY_DICT, GLOBAL_SPELL_BOOKS, GLOBAL_RACE_DATA, GLOBAL_CLASS_DATA, GLOBAL_CLASS_DATA_BY_TYPE, GLOBAL_COMPENDIUM_OF_SPELLS, GLOBAL_DESCRIPTIONS_DATABASE, GLOBAL_ART_DICTIONARY, GLOBAL_MAGIC_CLASSES, GLOBAL_INITIAL_SPELL_ABILITIES, GLOBAL_SPELL_LEVEL_ABILITIES
  if len(GLOBAL_ABILITY_DICT.keys()) != 0:
    return

  start = time.time()

  try:
    INSTALL_RANGERS_AND_RUFFIANS()
  except Exception as e:
    print("Critical Error while loading Rangers and Ruffians Data. Aborting")
    sys.exit(1)

  ability_path = os.path.join(INSTALL_DIRECTORY, 'abilities.json')
  class_path = os.path.join(INSTALL_DIRECTORY, 'classes.json')
  race_path = os.path.join(INSTALL_DIRECTORY, 'races.json')
  spell_path = os.path.join(INSTALL_DIRECTORY, 'spells.json')
  description_path = os.path.join(INSTALL_DIRECTORY, 'description_database.json')
  art_path = os.path.join(INSTALL_DIRECTORY, 'art.json')

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

  with open(description_path) as data_file:
    GLOBAL_DESCRIPTIONS_DATABASE = json.load(data_file)

  with open(art_path) as data_file:
    GLOBAL_ART_DICTIONARY = json.load(data_file)

  GLOBAL_MAGIC_CLASSES = {
    'bard': ["the_bard's_songbook", ],
    'cleric': ['the_book_of_healing', ],
    'paladin': ['the_book_of_healing', ],
    'wizard': ['the_novice_spellbook', "the_wizard's_addendum"],
    'sorcerer': ['the_novice_spellbook', "the_sorcerer's_scrolls"],
    'druid': ['the_novice_spellbook', "the_druid's_guidebook"],
    'necromancer': ['the_macabre_manual', ],
    'monk': ['the_book_of_chi', ],
    'battle_mage': ['the_novice_spellbook', ]
  }

  GLOBAL_INITIAL_SPELL_ABILITIES = {
    'Minor Spell Choice' : { 'Level_0': 1},
    'Spell Choice' : {'Level_0': 2},
    'Starting Fighting Techniques' : {'Basic_Techniques' : 2}
  }

  GLOBAL_SPELL_LEVEL_ABILITIES   = {
    'Level Zero Spells'   : 'Level_0', 
    'Level One Spells'    : 'Level_1',
    'Level Two Spells'    : 'Level_2', 
    'Level Three Spells'  : 'Level_3',
    'Level Four Spells'   : 'Level_4',
    'Level Five Spells'   : 'Level_5',
    'Fighting Techniques' : 'Basic_Techniques',
    'Master Fighting Techniques' : 'Master_Techniques',
    'Legendary Fighting Techniques' : 'Legendary Techniques'
  }

  finish = time.time()
  #print('LOAD TIME: {0}(s)'.format(finish - start))

def get_formal_spell_level_name(programatic_name):
  global GLOBAL_SPELL_LEVEL_ABILITIES
  for key, val in GLOBAL_SPELL_LEVEL_ABILITIES.items():
    if val == programatic_name:
      return key
  return None

def filterAbilities(abilities, verbose=False):
  filt = "description" if verbose else "brief"
  global GLOBAL_ABILITY_DICT
  filtered_abilities = dict()
  for ability in abilities:
    ability_type = GLOBAL_ABILITY_DICT[ability]["type"]
    if not ability_type in filtered_abilities:
      filtered_abilities[ability_type] = list()
    if 'cost' in GLOBAL_ABILITY_DICT[ability]:
      desc = f'Cost {GLOBAL_ABILITY_DICT[ability]["cost"]}, {GLOBAL_ABILITY_DICT[ability][filt]}'
    else:
      desc = GLOBAL_ABILITY_DICT[ability][filt]
    filtered_abilities[ability_type].append([ability, desc])
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
  return list(['Strength', 'Dexterity', 'Intelligence', 'Inner_Fire', 'Charisma', 'Perception', 'Luck'])

def roll_dice(number=1,sides=6,advantage=False,disadvantage=False):
  total = 0
  for roll in range(number):
    first_roll = random.randint(1, sides)
    second_roll = random.randint(1,sides)
    if advantage and not disadvantage:
      total += max(first_roll, second_roll)
    elif disadvantage and not advantage:
      total += min(first_roll, second_roll)
    else:
      total += first_roll
  return total

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
    raise Exception("ERROR: could not save {0} to {1} as a yml file\n{2}".format(input_file, output_file,traceback.format_exc()))

def convert_yaml_file_to_json_file(input_file, output_file):
  try:
    with open(input_file) as data_file:
      d = yaml.load(data_file)
    with open(output_file, 'w') as outfile:
      json.dump(d, outfile)
  except Exception as e:
    raise Exception("ERROR: could not save {0} to {1} as a yml file\n{2}".format(input_file, output_file,traceback.format_exc()))

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

# If rnr_class is provided, return a spellbook for that class
def join_spellbooks(rnr_class=None):
  spell_books = get_all_spellbooks()
  if not rnr_class is None:
    if not rnr_class.lower() in GLOBAL_MAGIC_CLASSES.keys():
      return None

  book_list = list()

  if rnr_class is None:
    for key, val in GLOBAL_MAGIC_CLASSES.items():
      for book in val:
        if not book in book_list:
          book_list.append(book)
    big_book_name = "All Spells"
  else:
    for book_name in GLOBAL_MAGIC_CLASSES[rnr_class]:
      book_list.append(book_name)
    big_book_name = ' and '.join(book_list)

  spell_data = dict()
  spell_data = dict()
  for book_name in book_list:
    for chapter, pages in spell_books[book_name].items():
      if not chapter in spell_data:
        spell_data[chapter] = dict()
      for spell_name, spell_info in pages.items():
        if not spell_name in spell_data[chapter]:
          spell_data[chapter][spell_name] = spell_info
  return (big_book_name, spell_data)

def get_random_spellbook(rnr_class, counts):
  if rnr_class is None or rnr_class not in GLOBAL_MAGIC_CLASSES:
    return dict()

  _, possible_spells = join_spellbooks(rnr_class)
  random_spellbook = dict()
  for key, val in counts.items():
    random_spellbook[key] = dict()
    for s in random.sample(list(possible_spells[key].keys()), val):
      random_spellbook[key][s] = possible_spells[key][s]
  return random_spellbook




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
  if subrace == None:
    return None

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
  return ['Charisma','Dexterity','Strength','Inner_Fire','Intelligence','Luck','Perception']

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
      traceback.print_exc()
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
        character = rnr_character('', race, subrace, rnr_class, level)
      except:
        continue
      characters.append(character)
  return characters



    