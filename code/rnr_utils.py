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
import string
import traceback

CODE_DIRECTORY = os.path.dirname(__file__)
BASE_DIRECTORY = os.path.split(CODE_DIRECTORY)[0]
INSTALL_DIRECTORY = os.path.join(BASE_DIRECTORY, 'INSTALLED_DATA')
DATA_DIRECTORY = os.path.join(BASE_DIRECTORY, 'data')

GLOBAL_ART_DICTIONARY = dict()
GLOBAL_DESCRIPTIONS_DATABASE = dict()
GLOBAL_ABILITY_DICT = dict()
GLOBAL_CLASS_DATA = dict()
GLOBAL_RACE_DATA = dict()
GLOBAL_SKILL_DATA = dict()
GLOBAL_SPELL_BOOKS = dict()
GLOBAL_COMPENDIUM_OF_SPELLS = dict()
GLOBAL_BOOK_OF_KNOWN_BEATS = dict()
GLOBAL_MAGIC_CLASSES = dict()
GLOBAL_PANTHEON = dict()
GLOBAL_STANDARD_ITEMS = dict()

GLOBAL_INITIAL_SPELL_ABILITIES = dict()

GLOBAL_SPELL_TIER_ABILITIES = dict()

GLOBAL_ART_PATH = os.path.join(BASE_DIRECTORY, 'site', 'images')
GLOBAL_SITE_ART_PATH = os.path.join(BASE_DIRECTORY, 'site', 'static', 'images')
VERSION_NUMBER = None

EXPERTISES = {
  'charisma' : ['Performance', 'Insight'],
  'strength' : ['Brawn', 'Endurance'],
  'dexterity': ['Sleight of Hand', 'Agility'] ,
  'perception' : ['Investigation', 'Alertness'],
  'intelligence' : ['Street Smarts', 'Book Smarts'],
  'inner_fire': ['Wisdom', 'Willpower']
}



class rnr_race():
  #Base constructor
  def __init__(self, name, subrace, abilities, description, quote, quote_author, handbook, health_die_pieces, expertise_choices):
    # What does a race have?
    # A name.
    # A subrace.
    # abilities.
    # description
    # quote
    # quote_author
    # handbook
    # health_die_pieces
    # movement?
    # Expertise choices

    # What does a class have?
    # A name
    # A subclass
    # Abilities (with dependencies?)
    # Recommended stat array
    # Expertise choices


    self.name = name
    self.subrace_name = subrace
    self.abilities = abilities
    self.description = description
    self.quote = quote
    self.quote_author = quote_author
    self.handbook = handbook
    self.health_die_pieces =  health_die_pieces
    self.expertise_choices = expertise_choices

  #simple constructor
  @classmethod
  def basic_constructor(cls, name, subrace):
    race_data = get_rnr_subrace_data(name, subrace)

    if race_data == None:
      raise Exception(f'ERROR: Could not load race {name} {subrace}')
    return cls(name, subrace, race_data['abilities'], race_data['description'], race_data.get('quote', None),
               race_data.get('author', None), race_data.get('handbook', None), race_data['health_die_pieces'],
               race_data['expertise_choices'])

  def serialize(self, male=False, verbose=False, skip_art=False):
    global GLOBAL_SITE_ART_PATH

    underscore_char = ' '
    serial = dict()
    serial['name'] = self.subrace_name.replace(' ', underscore_char)
    serial['abilities'] = filterAbilities(self.abilities, verbose)
    serial['stats'] = self.stat_recommendation
    serial['description'] = self.description
    serial['quote'] = self.quote
    serial['quote_author'] = self.quote_author

    if not skip_art:
      gender_string = 'male' if male else 'female'
      absolute_art_folder = os.path.join(GLOBAL_SITE_ART_PATH, 'race')
      relative_art_folder = os.path.join('static', 'images', 'race')
      image_path, attribution = get_gendered_art(relative_art_folder, absolute_art_folder, self.subrace_name.replace(' ','_').lower(), male)

      #Fall back to race image if no subrace image exists.
      if image_path is None:
        image_path, attribution = get_gendered_art(relative_art_folder, absolute_art_folder, self.race_name.replace(' ','_').lower(), male)

      img_name = image_path.split('/')[-1].split('.')[0]
      serial['rights'] = GLOBAL_ART_DICTIONARY.get(f'{img_name}_{gender_string}', None)
      serial["path_to_image"] = image_path

    serial['health_die_pieces'] = self.health_die_pieces
    return serial

class rnr_class():
  def __init__(self, rnr_class, subclass):

    class_data = get_subclass_data_with_name(subclass)
    if class_data is None:
        raise Exception(f'ERROR: Could not load class {rnr_class}')
    self.name = rnr_class
    self.subclass_name = subclass
    self.stat_recommendation = class_data['base_stats']
    self.expertise_choices = class_data['expertise_choices']
    self.health_die_pieces = class_data['health_die_pieces']
    self.handbook = class_data.get('handbook', None)
    self.roles = class_data['roles']

    # Gather up the abilities for all levels we've earned
    self.base_abilities = class_data.get('base_abilities', list())
    self.levels = class_data['levels']
    self.subclass = subclass
    self.class_name = rnr_class
    self.description = class_data.get('description', '')

  def get_abilities_to_level(self, level):
    abilities = self.base_abilities
    for step in range(1, level + 1):
      level_string = f'level_{step}'
      if not level_string in self.levels:
        continue
      level_details = self.levels[level_string]
      level_abilities = level_details['abilities'] if 'abilities' in level_details and level_details['abilities'] is not None else []
      abilities = abilities + level_abilities
    return abilities

  def serialize_level_up_sheet(self):
    levels = dict()
    all_data = get_subclass_data_with_name(self.subclass)
    levels = all_data['levels']

    for level in levels.keys():
      if not 'abilities' in levels[level] or levels[level]['abilities'] is None:
        levels[level]['abilities'] = dict()
      else:
        levels[level]['abilities'] = filterAbilities(levels[level]['abilities'])

    return levels

  def serialize(self, male=False, verbose=False, skip_art=False):
    global GLOBAL_SITE_ART_PATH, GLOBAL_ART_DICTIONARY

    serial = {}
    underscore_char = '_' if underscore else ' '
    serial = dict()
    serial["name"] = self.subclass_name.replace(' ', underscore_char)
    serial["abilities"] = filterAbilities(self.abilities, verbose)
    serial["stat_recommendation"] = self.stat_recommendation
    serial["description"] = self.description
    serial['quote'] = self.quote
    serial['quote_author'] = self.quote_author

    gender_string = 'male' if male else 'female'

    if not skip_art:
      absolute_art_folder = os.path.join(GLOBAL_SITE_ART_PATH, 'class')
      relative_art_folder = os.path.join('static', 'images', 'class')

      image_path, attribution = get_gendered_art(relative_art_folder, absolute_art_folder, self.subclass_name.lower(), male)

      img_name = image_path.split('/')[-1].split('.')[0]
      rights = GLOBAL_ART_DICTIONARY.get(f'{img_name}_{gender_string}', None)
      if rights is None:
        rights = GLOBAL_ART_DICTIONARY.get(f'{img_name}', None)

      serial['rights'] = rights
      serial["path_to_image"] = image_path

    serial['health_die_pieces'] = self.health_die_pieces

    serial['levels'] = self.serialize_level_up_sheet()
    return serial

  def get_stat(self, stat_name):
    stat_name = stat_name.lower().replace(' ', '_')
    if stat_name == "charisma":
      return self.stat_recommendation['Charisma']
    elif stat_name == "dexterity":
      return self.stat_recommendation['Dexterity']
    elif stat_name == "strength":
      return self.stat_recommendation['Strength']
    elif stat_name == "inner_fire":
      return self.stat_recommendation['Inner_Fire']
    elif stat_name == "intelligence":
      return self.stat_recommendation['Intelligence']
    elif stat_name == "luck":
      return self.stat_recommendation['Luck']
    elif stat_name == "perception":
      return self.stat_recommendation['Perception']
    else:
      print('Asked for bad stat {0}'.format(stat_name))
      return None

class rnr_character():
  def __init__(self, character_name, race_name, subrace, class_name, subclass, level, male=False):
    rnr_race_obj = rnr_race.basic_constructor(race_name, subrace)
    rnr_class_obj = rnr_class(class_name, subclass)

    self.abilities = rnr_race_obj.abilities + rnr_class_obj.get_abilities_to_level(level)
    stats = rnr_class_obj.stat_recommendation

    self.health_dice = rnr_race_obj.health_die_pieces + rnr_class_obj.health_die_pieces

    self.character_name = f'{race_name} {class_name}' if character_name == '' else character_name

    self.gender = 'male' if male==True else 'female'
    self.race = rnr_race_obj.name
    self.subrace = rnr_race_obj.subrace_name
    self.rnr_class = rnr_class_obj.name
    self.rnr_race_obj = rnr_race_obj
    self.rnr_class_obj = rnr_class_obj
    self.level = level
    self.subclass = subclass

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

  def new_character_sheet_serialize(self, verbose=False):
    serial = dict()
    serial['race'] = self.race
    serial['subrace'] = self.subrace
    serial['class'] = self.rnr_class
    serial['subclass'] = self.subclass
    serial['stats'] = self.stats
    serial['base_abilities'] = filterAbilities(self.abilities)
    serial['levels'] = self.rnr_class_obj.serialize_level_up_sheet()
    serial['icons'] = which_icons(self.subrace, self.subclass if self.subclass not in [None, ''] else self.rnr_class)
    serial['roles'] = self.rnr_class_obj.roles
    return serial

  def get_average_health(self):
    return get_average_health_to_level(self.health_dice, self.level)

  def get_max_health(self):
    return get_max_health_to_level(self.health_dice, self.level)


class rnr_class_wrapper():
  def __init__(self, class_name):
    subclasses = get_subclasses_for_class(class_name)
    self.class_data = get_overarching_rnr_class_data_with_name(class_name)
    self.class_name = class_name

    self.subclasses = list()
    for subclass in subclasses:
      self.subclasses.append( rnr_class(class_name, subclass) )

class rnr_race_wrapper():
  def __init__(self, race_name):
    subraces = get_subraces_for_race(race_name)
    self.race_data = get_overarching_rnr_race_data_with_name(race_name)
    self.race_name = race_name

    self.subraces = list()
    for subrace in subraces:
      self.subraces.append( rnr_race.basic_constructor(race_name, subrace) )

def which_icons(rnr_race, rnr_class):
  icons = list()

  #Everyone has health
  icons.append(('hearts.svg', 'Health'))


  # #Necromancers, Monks, and Sorcerers don't have spell_points. Cleric and paladin get special.
  # if rnr_class in rnr_utils.magical_classes and rnr_class not in ['necromancer', 'sorcerer', 'monk','cleric', 'paladin']:

  #Clerics and Paladins get special action points.
  if rnr_class.lower() in ['cleric', 'paladin']:
    icons.append(('prayer.svg', 'Action Points'))
  else:
    icons.append(('ink-swirl.svg', 'Action Points'))

  #Sorcerers have influence points
  if rnr_class.lower() == 'sorcerer':
    icons.append(('magic-swirl.svg', 'Influence'))

  #necromancers have souls
  if rnr_class.lower() == 'necromancer':
    icons.append(('tombstone.svg', 'Souls'))

  #highborn have gumption
  if rnr_class.lower() == 'highborn':
    icons.append(('swords-power.svg', 'Gumption'))

  # #archers have magic arrows
  # if rnr_class == 'archer':
  #   icons.append(('quiver.svg', 'Magic Quiver'))

  #Bards have spell coins
  if rnr_class.lower() == 'bard':
    icons.append(('swap-bag.svg', 'Spell Coins'))

  #Everyone has spell power, armor, and magic armor.
  icons.append(('fire-spell-cast.svg', 'Spell Power'))
  icons.append(('shield.svg', 'Armor'))
  icons.append(('bolt-shield.svg', 'Mage Armor'))
  icons.append(('moebius-trefoil.svg', 'Level Up'))
  return icons


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


def get_gendered_art(relative_art_folder, absolute_art_folder, art_name, male):
  global BASE_DIRECTORY
  jpg_art_name = f'{art_name}.jpg'
  gender_string = 'male' if male else 'female'

  gender_image =  os.path.join(gender_string, jpg_art_name)
  neutral_image = jpg_art_name

  if os.path.exists(os.path.join(absolute_art_folder, gender_image)):
    path = os.path.join(relative_art_folder, gender_image)
    art_request = f'{art_name}_{gender_string}'
  else:
    path = os.path.join(relative_art_folder, neutral_image)
    art_request = art_name

  markdown_rights = generate_markdown_art_attribution(art_request)

  if markdown_rights is None:
    print(f'could not find rights info for {art_request}.')
    return None, None
  else:
    return path, markdown_rights

def generate_markdown_art_attribution(art):
  global GLOBAL_ART_DICTIONARY

  rights = GLOBAL_ART_DICTIONARY.get(art,None)

  if rights == None:
    return None

  try:
    title           = GLOBAL_ART_DICTIONARY[art]['title']
    url             = GLOBAL_ART_DICTIONARY[art]['url']
    artist          = GLOBAL_ART_DICTIONARY[art]['artist']
    license_acronym = GLOBAL_ART_DICTIONARY[art]['license_acronym']
    license_url     = GLOBAL_ART_DICTIONARY[art]['license_url']
  except Exception as e:
    traceback.print_exc()
    return None

  return f'"[{title}"]({url}) by {artist} is licensed under [{license_acronym}]({license_url})  \n'

def get_expertises_for_stat(stat):
  global EXPERTISES

  if stat.lower().replace(' ', '_') in EXPERTISES:
    return EXPERTISES[stat.lower().replace(' ', '_')]
  return []


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
        convert_yml_file_to_json_file(source, destination)
      except Exception as e:
        print("ERROR: Could not install {0} to {1}".format(source, destination))
        traceback.print_exc()
        raise
      timestamps[filename] = mod_time

    with open(timestamp_json_path, 'w') as outfile:
      json.dump(timestamps, outfile)
    pbar.close()

def update_version(version_string):
  global VERSION_NUMBER
  load_Rangers_And_Ruffians_Data()

  major, greater, minor = version_string.split('.')
  major = int(major)
  greater = int(greater)
  minor = int(minor)

  current_major, current_greater, current_minor = VERSION_NUMBER.split('.')
  current_major = int(current_major)
  current_greater = int(current_greater)
  current_minor = int(current_minor)

  good_version = False
  if current_major < major:
    if current_major + 1 == major:
      if greater != 0 or minor != 0:
        raise("Incrementing major, but not setting greater and minor to 0.")
      good_version = True
    else:
      raise Exception('Attempting to raise major version by an increment greater than 1.')
  elif current_major > major:
    raise Exception('Attempting to decrease major version')

  # major versions are equal.
  if not good_version:
    if current_greater < greater:
      if current_greater + 1 == greater:
        if minor != 0:
          raise('Attempting to raise greater, but not setting minor to 0.')
        good_version = True
      else:
        raise Exception('Attempting to raise greater version by an increment greater than 1.')
    elif current_greater > greater:
      raise Exception('Attempting to decrease greater version')

  if not good_version:
    if current_minor < minor:
      if current_minor + 1 == minor:
        good_version = True
      else:
        raise Exception('Attempting to raise minor version by an increment greater than 1.')
    elif current_minor > minor:
      raise Exception('Attempting to decrease minor version')
    else: #the are equal
      raise Exception('Called update version with the current version')

  #We can safely increase the version.
  VERSION_NUMBER = f'{major}.{greater}.{minor}'

  with open(os.path.join(BASE_DIRECTORY, 'meta.json'), 'r') as infile:
    data = json.load(infile)

  data['most_recent_version'] = VERSION_NUMBER

  with open(os.path.join(BASE_DIRECTORY, 'meta.json'), 'w') as outfile:
    json.dump(data, outfile, indent=4)

def load_Rangers_And_Ruffians_Data():
  global VERSION_NUMBER, GLOBAL_ABILITY_DICT, GLOBAL_STANDARD_ITEMS, GLOBAL_SPELL_BOOKS, GLOBAL_RACE_DATA, GLOBAL_SKILL_DATA, GLOBAL_CLASS_DATA, GLOBAL_COMPENDIUM_OF_SPELLS, GLOBAL_DESCRIPTIONS_DATABASE, GLOBAL_ART_DICTIONARY, GLOBAL_MAGIC_CLASSES, GLOBAL_INITIAL_SPELL_ABILITIES, GLOBAL_SPELL_TIER_ABILITIES, GLOBAL_BOOK_OF_KNOWN_BEATS, GLOBAL_PANTHEON
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
  skill_path = os.path.join(INSTALL_DIRECTORY, 'skills.json')
  pantheon_path = os.path.join(INSTALL_DIRECTORY, 'pantheon.json')
  description_path = os.path.join(INSTALL_DIRECTORY, 'description_database.json')
  art_path = os.path.join(INSTALL_DIRECTORY, 'art.json')
  known_beasts_path = os.path.join(INSTALL_DIRECTORY, 'book_of_known_beasts.json')
  version_number_path = os.path.join(BASE_DIRECTORY, 'meta.json')
  items_path = os.path.join(INSTALL_DIRECTORY, 'items.json')

  with open(version_number_path) as infile:
    data = json.load(infile)
    VERSION_NUMBER = data['most_recent_version']

  with open(spell_path) as data_file:
    GLOBAL_SPELL_BOOKS = json.load(data_file)

  with open(skill_path, 'r') as data_file:
    GLOBAL_SKILL_DATA = json.load(data_file)

  for spellbook, chapters in GLOBAL_SPELL_BOOKS.items():
    for tier, spells in chapters.items():
      if spells == None:
        continue
      for spell, details in spells.items():
        GLOBAL_COMPENDIUM_OF_SPELLS[spell] = dict()
        GLOBAL_COMPENDIUM_OF_SPELLS[spell]['tier'] = tier
        GLOBAL_COMPENDIUM_OF_SPELLS[spell]['details'] = details

  with open(race_path) as data_file:
    GLOBAL_RACE_DATA = json.load(data_file)

  with open(class_path) as data_file:
    GLOBAL_CLASS_DATA = json.load(data_file)

  with open(ability_path) as data_file:
    GLOBAL_ABILITY_DICT = json.load(data_file)

  with open(description_path) as data_file:
    GLOBAL_DESCRIPTIONS_DATABASE = json.load(data_file)

  with open(art_path) as data_file:
    GLOBAL_ART_DICTIONARY = json.load(data_file)

  with open(known_beasts_path) as data_file:
    GLOBAL_BOOK_OF_KNOWN_BEATS = json.load(data_file)

  with open(items_path) as data_file:
    GLOBAL_STANDARD_ITEMS = json.load(data_file)

  with open(pantheon_path) as data_file:
    GLOBAL_PANTHEON = json.load(data_file)

  GLOBAL_MAGIC_CLASSES = {
    'bard': ["the_bard's_songbook", ],
    'cleric': ['the_book_of_healing', ],
    'paladin': ['the_book_of_healing', ],
    'wizard': ['the_novice_spellbook', "the_wizard's_addendum"],
    'sorcerer': ['the_novice_spellbook', "the_sorcerer's_scrolls"],
    'druid': ['the_novice_spellbook', "the_druid's_guidebook"],
    'necromancer': ['the_macabre_manual', ]
  }

  GLOBAL_INITIAL_SPELL_ABILITIES = {
    'Minor Spell Choice' : { 'Tier_0': 1},
    'Spell Choice' : {'Tier_0': 2},
    'Starting Fighting Techniques' : {'Basic_Techniques' : 2}
  }

  GLOBAL_SPELL_TIER_ABILITIES   = {
    'Tier Zero Spells'   : 'Tier_0',
    'Tier One Spells'    : 'Tier_1',
    'Tier Two Spells'    : 'Tier_2',
    'Tier Three Spells'  : 'Tier_3',
    'Tier Four Spells'   : 'Tier_4',
    'Tier Five Spells'   : 'Tier_5',
    'Fighting Techniques' : 'Basic_Techniques',
    'Master Fighting Techniques' : 'Master_Techniques',
    'Legendary Fighting Techniques' : 'Legendary Techniques'
  }


  finish = time.time()
  #print('LOAD TIME: {0}(s)'.format(finish - start))

def filterAbilities(abilities):
  global GLOBAL_ABILITY_DICT

  if abilities is None:
    return {}

  filtered_abilities = dict()
  for ability in abilities:
    ability_type = GLOBAL_ABILITY_DICT[ability]["type"]
    if not ability_type in filtered_abilities:
      filtered_abilities[ability_type] = dict()
    filtered_abilities[ability_type][ability] = dict()
    filtered_abilities[ability_type][ability]['brief'] = GLOBAL_ABILITY_DICT[ability]['brief']
    filtered_abilities[ability_type][ability]['verbose'] = GLOBAL_ABILITY_DICT[ability]['description']
    filtered_abilities[ability_type][ability]['cost'] = GLOBAL_ABILITY_DICT[ability]['cost'] if 'cost' in GLOBAL_ABILITY_DICT[ability] else 0
  return filtered_abilities

def abbreviate_stat(stat, upper=False, capitalize_first=False):
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

  if capitalize_first:
    ret = ret.capitalize()
  if upper:
    ret = ret.upper()
  return ret

def standard_stat_order():
  return list(['Strength', 'Dexterity', 'Intelligence', 'Inner_Fire', 'Charisma', 'Perception', 'Luck'])

# Mod is applied once.
def roll_dice(number, sides, roll_type='standard'):
  if roll_type not in ['standard', 'advantage', 'disadvantage']:
    raise Exception(f'Tried to roll a dice with roll type {roll_type}')

  first_total = 0
  second_total = 0
  for i in range(number):
    first_total += random.randint(1, sides)
  for i in range(number):
    second_total += random.randint(1, sides)


  if roll_type == 'advantage':
    total = max(first_total, second_total)
  elif roll_type == 'disadvantage':
    total = min(first_total, second_total)
  else:
    total = first_total

  return total

def get_max_health_to_level(health_dice, level):
  health = 0
  for i in range(0, level):
    health += health_dice + 4
  return health

def get_average_health_to_level(health_dice, level):
  health = health_dice + 2.5
  for i in range(1, level):
    health += (health_dice // 2) + .5 + 2.5
  return health

def convert_json_file_to_yml_file(input_file, output_file):
  try:
    with open(input_file) as data_file:
      d = json.load(data_file)
    with open(output_file, 'w') as outfile:
      yaml.dump(d, outfile, default_flow_style=False)
  except Exception as e:
    raise Exception("ERROR: could not save {0} to {1} as a yml file\n{2}".format(input_file, output_file,traceback.format_exc()))

def convert_yml_file_to_json_file(input_file, output_file):
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
    return copy.deepcopy(GLOBAL_COMPENDIUM_OF_SPELLS[spell]['tier']), copy.deepcopy(GLOBAL_COMPENDIUM_OF_SPELLS[spell]['details'])
  return None, None

def gather_spells(spell_data):
  load_Rangers_And_Ruffians_Data()

  player_spellbook = dict()

  tmp_spells = dict()
  for spell in spell_data:
    tier, data = find_spell_by_name(spell.replace('_',' '))
    #if data is None, the spell could not be found in the spellbook.
    if data == None:
      print("Could not find {0}".format(spell))
      continue
    #put the spell in the player's spellbook.
    if not tier in player_spellbook:
      player_spellbook[tier] = dict()
    player_spellbook[tier][spell] = data
  return player_spellbook

def is_casting_class(rnr_class):
  global GLOBAL_MAGIC_CLASSES
  if rnr_class.name.replace(' ', '_').lower() in GLOBAL_MAGIC_CLASSES:
    return True
  else:
    return False

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

def get_overarching_rnr_race_data_with_name(race):
  global GLOBAL_RACE_DATA
  load_Rangers_And_Ruffians_Data()

  if race.title() in GLOBAL_RACE_DATA:
    return copy.deepcopy(GLOBAL_RACE_DATA[race.title()])

  return None

def get_overarching_rnr_class_data_with_name(rnr_class):
  global GLOBAL_CLASS_DATA
  load_Rangers_And_Ruffians_Data()

  if rnr_class.title() in GLOBAL_CLASS_DATA:
    return copy.deepcopy(GLOBAL_CLASS_DATA[rnr_class.title()])

  return None

def get_subclass_data_with_name(subclass):
  load_Rangers_And_Ruffians_Data()

  for rnr_class, info in GLOBAL_CLASS_DATA.items():
    if subclass in info["subclasses"]:
      return get_subclass_data(rnr_class, subclass)
  return None

def get_subclass_data(rnr_class, subclass):
  load_Rangers_And_Ruffians_Data()

  if rnr_class in GLOBAL_CLASS_DATA:
    if subclass in GLOBAL_CLASS_DATA[rnr_class]['subclasses']:
      return copy.deepcopy(GLOBAL_CLASS_DATA[rnr_class]['subclasses'][subclass])
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

def get_class_given_subclass(subclass):
  global GLOBAL_CLASS_DATA
  load_Rangers_And_Ruffians_Data()

  for rnr_class, data in GLOBAL_CLASS_DATA.items():
    if subclass.replace('_',' ').title() in data['subclasses'].keys():
      return rnr_class
  return None

def get_subraces_for_race(race):
  global GLOBAL_RACE_DATA

  load_Rangers_And_Ruffians_Data()
  if race in GLOBAL_RACE_DATA:
    return list(GLOBAL_RACE_DATA[race]["subraces"].keys())
  return None

def get_subclasses_for_class(needle):
  global GLOBAL_CLASS_DATA

  load_Rangers_And_Ruffians_Data()
  if needle in GLOBAL_CLASS_DATA:
    return list(GLOBAL_CLASS_DATA[needle]["subclasses"].keys())
  else:
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

def get_all_class_names(underscore=False):
  global GLOBAL_CLASS_DATA
  underscore_char = '_' if underscore else ' '
  load_Rangers_And_Ruffians_Data()

  class_names = list()
  for class_name in GLOBAL_CLASS_DATA.keys():
    for subclass_name in GLOBAL_CLASS_DATA[class_name]['subclasses']:
      class_names.append((class_name.replace(' ', underscore_char), subclass_name.replace(' ', underscore_char)))
  return class_names

def get_all_race_names(underscore=False):
  global GLOBAL_RACE_DATA
  load_Rangers_And_Ruffians_Data()
  underscore_char = '_' if underscore else ' '
  race_names = list()
  for race in GLOBAL_RACE_DATA.keys():
    for subrace in GLOBAL_RACE_DATA[race]['subraces']:
      race_names.append((race.replace(' ', underscore_char), subrace.replace(' ', underscore_char)))
  return race_names

def get_all_subrace_names(underscore=False):
  load_Rangers_And_Ruffians_Data()
  global GLOBAL_RACE_DATA
  underscore_char = '_' if underscore else ' '

  subrace_names = list()
  for race in GLOBAL_RACE_DATA.keys():
    for subrace in GLOBAL_RACE_DATA[race]['subraces']:
      subrace_names.append(subrace.replace(' ', underscore_char))
  return subrace_names

def get_all_subclass_names(underscore=False):
  load_Rangers_And_Ruffians_Data()
  global GLOBAL_CLASS_DATA
  underscore_char = '_' if underscore else ' '

  subclass_names = list()
  for rnr_class in GLOBAL_CLASS_DATA.keys():
    for subclass in GLOBAL_CLASS_DATA[rnr_class]['subclasses']:
      subclass_names.append(subclass.replace(' ', underscore_char))
  return subclass_names

def get_all_stat_names():
  return standard_stat_order()

def get_all_rnr_abilities():
  global GLOBAL_ABILITY_DICT
  return copy.deepcopy(GLOBAL_ABILITY_DICT)

def get_rnr_class_dict():
  global GLOBAL_CLASS_DATA
  return copy.deepcopy(GLOBAL_CLASS_DATA)

def get_rnr_race_dict():
  global GLOBAL_RACE_DATA
  return copy.deepcopy(GLOBAL_RACE_DATA)

# def get_possible_skills(character):
#   global GLOBAL_SKILL_DATA
#   ret = dict()
#   for name, info in GLOBAL_SKILL_DATA.items():
#     if not 'requirements' in info:
#       ret[name] = GLOBAL_SKILL_DATA[name]
#     else:
#       bad_requirement = False
#       if 'stats' in info['requirements']:
#         for stat, value in info['requirements']['stats'].items():
#           if character.get_stat(stat.lower()) < value:
#             print(f"{name}: Bad requirment, {stat} is too low {character.get_stat(stat.lower())} < {value}")
#             bad_requirement = True
#             break
#       if not bad_requirement and 'skills' in info['requirements']:
#         for skill in info['requirements']['skills']:
#           if not skill in character.skills:
#             print(f"{name}: Bad requirement, didn't have {skill}")
#             bad_requirement = True
#             break
#       if not bad_requirement:
#         ret[name] = GLOBAL_SKILL_DATA[name]
#   return ret

####################################################################################
#
# OBJECT LOADING FUNCTIONS
#
####################################################################################

def load_all_race_objects():
  global GLOBAL_RACE_DATA
  load_Rangers_And_Ruffians_Data()
  races = list()
  for race, data in GLOBAL_RACE_DATA.items():
    for subrace in data['subraces'].keys():
      try:
        new_race = rnr_race.basic_constructor(race, subrace)
      except:
        traceback.print_exc()
        continue
      races.append(new_race)
  return races

#TODO doesn't take subclass into account.
def load_all_class_objects():
  global GLOBAL_CLASS_DATA
  load_Rangers_And_Ruffians_Data()
  rnr_classes = list()
  for class_name, data in GLOBAL_CLASS_DATA.items():
    for subclass in data['subclasses'].keys():
      try:
        new_class = rnr_class(class_name, subclass)
      except:
        traceback.print_exc()
        continue
      rnr_classes.append(new_class)
  return rnr_classes

def load_all_class_wrappers():
  load_Rangers_And_Ruffians_Data()

  class_names = get_all_class_names()
  ret = list()
  visited = set()
  for rnr_class, _ in class_names:
    if rnr_class in visited:
      continue
    visited.add(rnr_class)
    ret.append(rnr_class_wrapper(rnr_class))

  return ret

def load_all_race_wrappers():
  load_Rangers_And_Ruffians_Data()

  race_names = get_all_race_names()
  ret = list()
  visited = set()
  for rnr_race, _ in race_names:
    if rnr_race in visited:
      continue
    visited.add(rnr_race)
    ret.append(rnr_race_wrapper(rnr_race))

  return ret

def load_all_characters(level=0):
  load_Rangers_And_Ruffians_Data()
  rnr_races = get_all_race_names()
  rnr_classes = get_all_class_names()

  lis = list()
  for race_name, subrace_name in rnr_races:
    for class_name, subclass_name in rnr_classes:
      character = rnr_character('', race_name, subrace_name, class_name, subclass_name, level)
      lis.append(character)
  return lis

'''
Races should be a list of tuples of the form (race, subrace)
'''
def load_combos_given_list(races, classes, level):
  load_Rangers_And_Ruffians_Data()
  characters = list()
  for race, subrace in races:
    for class_name, subclass_name in classes:
      try:
        character = rnr_character('', race, subrace, class_name, subclass_name, level)
      except:
        traceback.print_exc()
        continue
      characters.append(character)
  return characters



