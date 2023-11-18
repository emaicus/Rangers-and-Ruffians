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
import pathlib

CODE_DIRECTORY = pathlib.Path(__file__).resolve()
BASE_DIRECTORY = CODE_DIRECTORY.parent.parent.parent
print(f'Rangers and Ruffians is being run from {BASE_DIRECTORY}')
INSTALL_DIRECTORY = os.path.join(BASE_DIRECTORY, 'INSTALLED_DATA')
DATA_DIRECTORY = os.path.join(BASE_DIRECTORY, 'data')

GLOBAL_ART_DICTIONARY = dict()
GLOBAL_CLASS_DATA = dict()
GLOBAL_RACE_DATA = dict()
GLOBAL_BOOK_OF_KNOWN_BEATS = dict()
GLOBAL_PANTHEON = dict()

GLOBAL_ART_PATH = os.path.join(BASE_DIRECTORY, 'site', 'images')
GLOBAL_SITE_ART_PATH = os.path.join(BASE_DIRECTORY, 'site', 'static', 'images')
VERSION_NUMBER = None

class rnr_race():
  #Base constructor
  def __init__(self, name, health_dice_bonus, base_movement, abilities, handbook, is_a):
    self.name = name
    self.health_dice_bonus =  health_dice_bonus
    self.base_movement =  base_movement
    self.abilities = abilities
    self.handbook = handbook
    self.is_a = is_a if is_a is not None else name  

  #simple constructor
  @classmethod
  def basic_constructor(cls, name):
    race_data = get_rnr_race_data(name)

    if race_data == None:
      raise Exception(f'ERROR: Could not load race "{name}"')
    return cls(name, race_data['health_dice_bonus'], race_data['base_movement'], 
                race_data['abilities'], race_data['handbook'], race_data.get('is_a', None))

  def serialize(self, male=False, skip_art=False):
    global GLOBAL_SITE_ART_PATH

    underscore_char = ' '
    serial = dict()
    serial['name'] = self.name
    serial['health_dice_bonus'] = self.health_dice_bonus
    serial['base_movement'] = self.base_movement
    serial['abilities'] = self.abilities
    serial['handbook'] = self.handbook
    serial['is_a'] = self.is_a

    if not skip_art:
      gender_string = 'male' if male else 'female'
      absolute_art_folder = os.path.join(GLOBAL_SITE_ART_PATH, 'race')
      relative_art_folder = os.path.join('static', 'images', 'race')

      image_path, attribution = get_gendered_art(relative_art_folder, absolute_art_folder, self.name.replace(' ','_').lower(), male)

      img_name = image_path.split('/')[-1].split('.')[0]
      serial['rights'] = GLOBAL_ART_DICTIONARY.get(f'{img_name}_{gender_string}', None)
      serial["path_to_image"] = image_path

    serial['health_die_pieces'] = self.health_die_pieces
    return serial

class rnr_class():
  ''' Takes in classname and json object, instantiates class.'''
  def __init__(self, rnr_classname, rnr_classdata):

    self.name = rnr_classname
    self.evasion = rnr_classdata['base_evasion']
    self.stat_recommendation = rnr_classdata['recommended_stats']
    self.handbook = rnr_classdata.get('handbook', {})
    self.health_dice_bonus = rnr_classdata['health_dice_bonus']
    self.abilities = rnr_classdata['abilities']
    self.expertise = rnr_classdata.get('expertise', list())

  #simple constructor
  @classmethod
  def basic_constructor(cls, name):
    class_data = get_rnr_class_data(name)

    if get_rnr_class_data == None:
      raise Exception(f'ERROR: Could not load class "{name}"')
    return cls(name, class_data)

  def serialize(self, male=False, verbose=False, skip_art=False):
    global GLOBAL_SITE_ART_PATH, GLOBAL_ART_DICTIONARY

    serial = {}
    serial['name'] = self.name
    serial['evasion'] = self.evasion
    serial['stat_recommendation'] = self.stat_recommendation
    serial['handbook'] = self.handbook
    serial['health_dice_bonus'] = self.health_dice_bonus
    serial['abilities'] = self.abilities
    serial['expertise'] = self.expertise

    gender_string = 'male' if male else 'female'

    if not skip_art:
      absolute_art_folder = os.path.join(GLOBAL_SITE_ART_PATH, 'class')
      relative_art_folder = os.path.join('static', 'images', 'class')

      image_path, attribution = get_gendered_art(relative_art_folder, absolute_art_folder, self.name.lower(), male)

      img_name = image_path.split('/')[-1].split('.')[0]
      rights = GLOBAL_ART_DICTIONARY.get(f'{img_name}_{gender_string}', None)
      if rights is None:
        rights = GLOBAL_ART_DICTIONARY.get(f'{img_name}', None)

      serial['rights'] = rights
      serial["path_to_image"] = image_path
    return serial

class rnr_character():
  def __init__(self, character_name, race_name, class_name, level, male=False):
    rnr_race_obj = rnr_race.basic_constructor(race_name)
    rnr_class_obj = rnr_class.basic_constructor(class_name)

    self.abilities = rnr_race_obj.abilities + rnr_class_obj.abilities
    self.stats = rnr_class_obj.stat_recommendation
    self.health_dice = rnr_race_obj.health_die_pieces + rnr_class_obj.health_dice_bonus
    self.character_name = f'{race_name} {class_name}' if character_name == '' else character_name
    self.gender = 'male' if male==True else 'female'
    self.race = rnr_race_obj.name
    self.rnr_class = rnr_class_obj.name
    self.rnr_race_obj = rnr_race_obj
    self.rnr_class_obj = rnr_class_obj
    self.level = level

  def serialize(self, verbose=False):
    serial = self.base_serialize(verbose)
    serial['race'] = self.race.lower()
    serial['class'] = self.rnr_class.lower()
    serial['health'] = self.get_health()
    serial['health_dice'] = self.health_dice
    serial['character_name'] = self.character_name
    serial['gender'] = self.gender
    serial['level'] = self.level
    return serial

  def new_character_sheet_serialize(self, verbose=False):
    serial = dict()
    serial['race'] = self.race
    serial['class'] = self.rnr_class
    serial['stats'] = self.stats
    serial['base_abilities'] = self.abilities
    serial['levels'] = self.rnr_class_obj.abilities
    serial['icons'] = which_icons(self.race, self.rnr_class)
    return serial

  def get_average_health(self):
    return get_average_health_to_level(self.health_dice, self.level)

  def get_max_health(self):
    return get_max_health_to_level(self.health_dice, self.level)

def which_icons(rnr_race, rnr_class):
  icons = list()

  #Everyone has health
  icons.append(('hearts.svg', 'Health'))


  # #Necromancers, Monks, and Sorcerers don't have spell_points. Cleric and paladin get special.
  # if rnr_class in core.magical_classes and rnr_class not in ['necromancer', 'sorcerer', 'monk','cleric', 'paladin']:

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
      reinstall.append((filename, f'installing {filename}', mod_time))
    elif mod_time != timestamps[filename]:
      reinstall.append((filename, f'updating {filename}', mod_time))

  if len(reinstall) > 0:
    # progress bar.
    pbar = tqdm(reinstall)
    for filename, description, mod_time in pbar:
      pbar.set_description(description)
      source = os.path.join(DATA_DIRECTORY, filename)
      json_filename = f'{filename.split(".")[0]}.json'
      destination = os.path.join(INSTALL_DIRECTORY, json_filename)
      try:
        convert_yml_file_to_json_file(source, destination)
      except Exception as e:
        print(f"ERROR: Could not install {source} to {destination}")
        traceback.print_exc()
        raise
      timestamps[filename] = mod_time

      with open(timestamp_json_path, 'w') as outfile:
        json.dump(timestamps, outfile)
    pbar.close()

def update_version(version_string):
  global VERSION_NUMBER
  load_Rangers_And_Ruffians_Data()

  # Split and convert to int
  major, greater, minor = list(map(int, version_string.split('.')))
  current_major, current_greater, current_minor = list(map(int, VERSION_NUMBER.split('.')))

  if major == current_major and greater == current_greater and minor == current_minor:
    raise Exception('Called update version with the current version')

  for variable_name, new_version, current_version, sub_variables in [
    ('major', major, current_major, (greater, minor)),
    ('greater', greater, current_greater, (minor)),
    ('minor', minor, current_minor, ())
  ]:
  
    # Major is too low
    if current_version > new_version:
      raise Exception(f'Attempting to roll back {variable_name} from {current_version} to {new_version}')
    
    # Major is too big
    if new_version > current_version + 1:
      raise Exception(f'Attempting to increment {variable_name} by more than one step from {current_version} to {new_version}')
    
    for var in sub_variables:
      if var != 0:
        raise(f"Incrementing {variable_name}, but not setting lesser versions to 0.")

  #We can safely increase the version.
  VERSION_NUMBER = f'{major}.{greater}.{minor}'

  with open(os.path.join(BASE_DIRECTORY, 'meta.json'), 'r') as infile:
    data = json.load(infile)

  data['most_recent_version'] = VERSION_NUMBER

  with open(os.path.join(BASE_DIRECTORY, 'meta.json'), 'w') as outfile:
    json.dump(data, outfile, indent=4)

def load_Rangers_And_Ruffians_Data():
  global VERSION_NUMBER, GLOBAL_RACE_DATA, GLOBAL_CLASS_DATA, GLOBAL_ART_DICTIONARY, GLOBAL_BOOK_OF_KNOWN_BEATS, GLOBAL_PANTHEON
  start = time.time()

  try:
    INSTALL_RANGERS_AND_RUFFIANS()
  except Exception as e:
    print("Critical Error while loading Rangers and Ruffians Data. Aborting")
    sys.exit(1)

  class_path = os.path.join(INSTALL_DIRECTORY, 'classes.json')
  race_path = os.path.join(INSTALL_DIRECTORY, 'races.json')
  pantheon_path = os.path.join(INSTALL_DIRECTORY, 'pantheon.json')
  art_path = os.path.join(INSTALL_DIRECTORY, 'art.json')
  known_beasts_path = os.path.join(INSTALL_DIRECTORY, 'book_of_known_beasts.json')
  version_number_path = os.path.join(BASE_DIRECTORY, 'meta.json')

  with open(version_number_path) as infile:
    data = json.load(infile)
    VERSION_NUMBER = data['most_recent_version']

  with open(race_path) as data_file:
    GLOBAL_RACE_DATA = json.load(data_file)

  with open(class_path) as data_file:
    GLOBAL_CLASS_DATA = json.load(data_file)

  with open(art_path) as data_file:
    GLOBAL_ART_DICTIONARY = json.load(data_file)

  with open(known_beasts_path) as data_file:
    GLOBAL_BOOK_OF_KNOWN_BEATS = json.load(data_file)

  with open(pantheon_path) as data_file:
    GLOBAL_PANTHEON = json.load(data_file)

  finish = time.time()
  print('LOAD TIME: {finish - start}(s)')

def abbreviate_stat(stat, upper=True):
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
    ret = 'cha'
  elif stat == 'luck':
    ret = 'luk'
  else:
    print('ERROR: BAD STAT {stat}')
    return None

  if upper:
    ret = ret.upper()
  return ret

def standard_stat_order():
  return list(['Strength', 'Dexterity', 'Intelligence', 'Inner_Fire', 'Charisma', 'Perception', 'Luck'])

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
    raise Exception(f"ERROR: could not save {input_file} to {output_file} as a yml file\n{traceback.format_exc()}")

def convert_yml_file_to_json_file(input_file, output_file):
  try:
    with open(input_file) as data_file:
      d = yaml.load(data_file)
    with open(output_file, 'w') as outfile:
      json.dump(d, outfile)
  except Exception as e:
    raise Exception("ERROR: could not save {0} to {1} as a yml file\n{2}".format(input_file, output_file,traceback.format_exc()))

def get_rnr_class_data(class_name):
  global GLOBAL_CLASS_DATA
  load_Rangers_And_Ruffians_Data()
  return copy.deepcopy(GLOBAL_CLASS_DATA[class_name])

def get_rnr_race_data(name):
  global GLOBAL_RACE_DATA
  load_Rangers_And_Ruffians_Data()
  return copy.deepcopy(GLOBAL_RACE_DATA[name.title()])

def get_all_class_names(underscore=False):
  global GLOBAL_CLASS_DATA
  load_Rangers_And_Ruffians_Data()
  return GLOBAL_CLASS_DATA.keys()

def get_all_race_names(underscore=False):
  global GLOBAL_RACE_DATA
  load_Rangers_And_Ruffians_Data()
  return GLOBAL_RACE_DATA.keys()

def get_all_stat_names():
  return standard_stat_order()

def get_rnr_class_dict():
  global GLOBAL_CLASS_DATA
  return copy.deepcopy(GLOBAL_CLASS_DATA)

def get_rnr_race_dict():
  global GLOBAL_RACE_DATA
  return copy.deepcopy(GLOBAL_RACE_DATA)

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
    try:
      new_race = rnr_race.basic_constructor(race)
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

def load_all_characters(level=0):
  load_Rangers_And_Ruffians_Data()
  return load_combos_given_list(get_all_race_names(), get_all_class_names(), level=0)


def load_combos_given_list(races, classes, level):
  load_Rangers_And_Ruffians_Data()
  characters = list()
  for race in races:
    for class_name in classes:
      try:
        character = rnr_character('', race, class_name, level)
      except:
        traceback.print_exc()
        continue
      characters.append(character)
  return characters



