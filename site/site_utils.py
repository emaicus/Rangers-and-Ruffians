import os
import flask
import sys
from flask import Flask,redirect, render_template
from flask import request
import cgi
import names
import random
import json
sys.path.append(os.path.abspath('../code'))
import rnr_utils
import rnr_descriptions


"""
Validity functions.
"""

def all_none(d):
  for key, value in d.items():
    if value is not None and value != [] and value != '' and value != False:
      return False
  return True

def validity_check():
  info = validity_check_get_request()
  return info if not all_none(info) else validity_check_post_request()


def validity_check_get_request():
  info = dict()
  info['name']        = verify_name(request.args.get('name',''))
  info['class']       = verify_class(request.args.get('class',''))
  info['magic_class'] = is_magic_class(info['class'])
  info['subrace']     = verify_subrace(request.args.get('subrace',''))
  info['roll_stats']  = verify_roll_stats(request.args.get('roll_stats', ''))
  info['gender']      = verify_gender(request.args.get('gender',''))
  info['level']       = verify_level(request.args.get('level', ''))
  info['spells']      = verify_spells(request.args.getlist('spells', None))
  info['deity']       = verify_deity(request.args.get('deity', None))

  return info

def validity_check_post_request():
  info = dict()
  info['name']        = verify_name(request.form.get('name',''))
  info['class']       = verify_class(request.form.get('class',''))
  info['magic_class'] = is_magic_class(info['class'])
  info['subrace']     = verify_subrace(request.form.get('subrace',''))
  info['roll_stats']  = verify_roll_stats(request.form.get('roll_stats', ''))
  info['gender']      = verify_gender(request.form.get('gender',''))
  info['level']       = verify_level(request.form.get('level', ''))
  info['spells']      = verify_spells(request.form.getlist('spells', None))
  info['deity']       = verify_deity(request.form.get('deity', None))

  return info


def verify_class(class_name):
  class_names = rnr_utils.get_all_class_names()
  class_names = [x.lower() for x in class_names]
  return class_name.lower() if class_name.lower() in class_names else None

def verify_subrace(race):
  subrace_names = rnr_utils.get_all_subrace_names()
  print(race)
  print(subrace_names)
  subrace_names = [x.lower() for x in subrace_names]
  return race.lower() if race.lower() in subrace_names else None  

def verify_name(name):
  name = cgi.escape(name)
  return None if name.strip() == '' else name

def verify_gender(gender):
  return gender.lower() if gender.lower() in ['male', 'female'] else None

def verify_level(level):
  valid_levels = [str(x) for x in range(16)]
  return int(level) if level in valid_levels else None

def is_magic_class(rnr_class):
  return True if rnr_class != None and rnr_class.lower() in rnr_utils.GLOBAL_MAGIC_CLASSES.keys() else False

def verify_roll_stats(roll_stats):
  return True if roll_stats == 'true' else False

# Filtered later by rnr_utils.gather_spells
def verify_spells(spell_list):
  print(spell_list)
  return list() if spell_list is None else spell_list

def verify_deity(deity):
  # return deity if deity in rnr_utils.deity_dict.keys() else None
  return deity

"""
Page data population functions
"""

def populate_race(info):
  page_objects = rnr_utils.load_all_race_objects()
  serial_data = list()
  for entity in page_objects:
    male = True if info['gender'] == 'male' else False
    serial_data.append(entity.serialize(male))
  return serial_data

def populate_class(info):
  page_objects = rnr_utils.load_all_class_objects()
  serial_data = list()
  for entity in page_objects:
    male = True if info['gender'] == 'male' else False
    serial_data.append(entity.serialize(male))
  return serial_data

def populate_gender():
  serial_data = list()
  for gender in ("male", "female"):
    serial = dict()
    serial["stats"] = None
    serial["name"] = gender
    serial["abilities"] = None
    serial["description"] = '''Your chosen gender can affect the way that you roleplay your character
                               in Rangers and Ruffians. However, it should not affect your chosen race
                               or class. While using the website, your chosen gender will affect the 
                               race and class images that are displayed.
                            '''
    serial["path_to_image"] = "/static/images/gender/{0}.jpg".format(gender.lower())

    serial['rights'] = rnr_utils.GLOBAL_ART_DICTIONARY.get(gender.lower(), None)

    serial_data.append(serial)
  return serial_data

"""
Routing Functions
"""

def generate_redirect_string(param_map):
  ret = '?'
  for key in ['gender','subrace','class','name']:
    if param_map[key] != None:
      ret = '{0}{1}={2}&'.format(ret,key,param_map[key])
  #fist char is a ?, then & everything
  print('forwarding param {0}'.format(ret))
  return ret

#Order of operations: gender, race, class, name
def find_next_page(params):
  print(params)
  for key in ['gender','subrace','class', 'name', 'level']:
    if params[key] == None:
      print('returning {0}'.format(key))
      return key
  return None

"""
Character Sheet Functions
"""

def which_icons(rnr_race, rnr_class):
  icons = list()

  #Everyone has health
  icons.append(('hearts.svg', 'Health'))

  # #Necromancers, Monks, and Sorcerers don't have spell_points. Cleric and paladin get special.
  # if rnr_class in rnr_utils.magical_classes and rnr_class not in ['necromancer', 'sorcerer', 'monk','cleric', 'paladin']:

  #Clerics and Paladins get special action points.
  if rnr_class in ['cleric', 'paladin']:
    icons.append(('prayer.svg', 'Action Points'))
  else:
    icons.append(('ink-swirl.svg', 'Action Points'))

  #Sorcerers have influence points
  if rnr_class == 'sorcerer':
    icons.append(('magic-swirl.svg', 'Influence'))
  
  #necromancers have souls
  if rnr_class == 'necromancer':
    icons.append(('tombstone.svg', 'Souls'))
  
  #highborn have gumption
  if rnr_class == 'highborn':
    icons.append(('swords-power.svg', 'Gumption'))

  # #archers have magic arrows
  # if rnr_class == 'archer':
  #   icons.append(('quiver.svg', 'Magic Quiver'))

  #Bards have spell coins
  if rnr_class == 'bard':
    icons.append(('swap-bag.svg', 'Spell Coins'))

  #Everyone has spell power, armor, and magic armor.
  icons.append(('fire-spell-cast.svg', 'Spell Power'))
  icons.append(('shield.svg', 'Armor'))
  icons.append(('bolt-shield.svg', 'Mage Armor'))
  return icons