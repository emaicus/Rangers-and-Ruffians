import os
import flask
import sys
from flask import Flask,redirect, render_template
from flask import request
import cgi
import names
import random
import json
import site_utils
sys.path.append(os.path.abspath('../code'))
import rnr_utils
import rnr_descriptions

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index_page():
  print('hit index page')
  return render_template('homepage.html')

@app.route('/legal')
def legal():
  print('hit legal')
  return render_template('legal.html',art=rnr_utils.GLOBAL_ART_DICTIONARY)

@app.route('/creation')
def creation_landing_page():
  print('Hit creation landing page')
  page_objects = None
  populated_value = ""
  forwarding_param = ""
  serial_data = list()
  
  info = site_utils.validity_check()
  next_to_populate = site_utils.find_next_page(info)
  redirect_string = site_utils.generate_redirect_string(info)

  prev_stats = None
  if info['class'] != None:
    prev_stats = rnr_utils.rnr_class(info['class']).stats
  if info['subrace'] != None:
    subrace = info['subrace'].replace('_', ' ')
    race = rnr_utils.get_race_given_subrace(subrace)
    prev_stats = rnr_utils.rnr_race.basic_constructor(race, subrace).stats

  if next_to_populate == 'name' or next_to_populate == 'level':
    random_name = names.get_first_name(gender=info['gender'])
    print('Going to username form')
    return render_template("user_name_form.html", chosen_gender=info['gender'], chosen_subrace=info['subrace'], chosen_rnr_class=info['class'], all_genders=['male','female'], all_races=rnr_utils.get_all_race_names(), all_rnr_classes=rnr_utils.get_all_class_names(), random_name=random_name.title())
  elif next_to_populate == 'gender':
    serial_data = site_utils.populate_gender()
    print('Going to gender page')
    return render_template("display_page.html", data=serial_data, next_page='/creation', forwarding_param=redirect_string, next_param='gender',prev_stats=None,display_class=False)
  elif next_to_populate == 'class':
    serial_data = site_utils.populate_class(info)
    print('Going to class page')
    return render_template("display_page.html", data=serial_data, stat_order=rnr_utils.standard_stat_order(), next_page='/creation', forwarding_param=redirect_string, next_param='class',prev_stats=prev_stats,display_class=True)
  elif next_to_populate == 'subrace':
    serial_data = site_utils.populate_race(info)
    print('Going to race page')
    return render_template("display_page.html", data=serial_data, next_page='/creation', forwarding_param=redirect_string, next_param='subrace',prev_stats=prev_stats,display_class=False)
  else:
    name = info['name']
    subrace = info['subrace']
    race = rnr_utils.get_race_given_subrace(subrace.replace('_', ' '))
    print(subrace, race)
    rnr_class = info['class']
    level = info['level']
    gender = info['gender']
    # If we need to hit the spells form
    if rnr_class.lower() in rnr_utils.GLOBAL_MAGIC_CLASSES.keys():
      print('Going to spell page helper')
      return spell_page_helper('creation/character_sheet', rnr_class, name, race, subrace, level, gender )
    else:
      male=True if gender.lower() == 'male' else False
      character = rnr_utils.rnr_character(name,race,subrace,rnr_class,level)
      serial = character.serialize()
      serial_class = rnr_utils.rnr_class(rnr_class.lower()).serialize()
      print('Going to character sheet')
      return render_template("character_sheet.html",character=serial, icons=site_utils.which_icons(rnr_class, rnr_class), spells=None, class_data=serial_class)

@app.route('/creation/character_sheet', methods=['POST',])
def character_sheet_helper():
  print('hit char_sheet helper')
  info = site_utils.validity_check()
  next_page = site_utils.find_next_page(info)

  # Route back if something goes wrong
  if next_page is not None:
    return creation_landing_page()
  # if next_page is not None:
  #   if next_page == 'deity':
  #     #render the deity page
  #     pass
  #   else:
  #     creation_landing_page()
  # else:
  name = info['name']
  subrace = info['subrace'].replace('_', ' ')
  race = rnr_utils.get_race_given_subrace(subrace)
  rnr_class = info['class']
  level = info['level']
  gender = info['gender']
  spells = info['spells']
  print(spells)
  player_spellbook = rnr_utils.gather_spells(spells)
  print(json.dumps(player_spellbook, indent=4))
  male=True if gender.lower() == 'male' else False
  character = rnr_utils.rnr_character(name,race,subrace,rnr_class,level)
  serial = character.serialize()
  serial_class = rnr_utils.rnr_class(rnr_class.lower()).serialize()
  return render_template("character_sheet.html",character=serial,icons=site_utils.which_icons(rnr_class, rnr_class), spells=player_spellbook, class_data=serial_class)

@app.route('/ajax_load_content', methods=['POST',])
def ajax_load_content():
  print('hit ajax_load_content')
  class_names = rnr_utils.get_all_class_names()
  class_names = [x.lower() for x in class_names]
  subrace_names = rnr_utils.get_all_subrace_names()
  subrace_names = [x.lower() for x in subrace_names]

  entity_to_load = request.form.get('entity_to_load','NO ENTITY SPECIFIED').lower()

  if entity_to_load in class_names:
    serial = rnr_utils.rnr_class(entity_to_load, level=10, subclass="").serialize()
    return render_template('display_class.html', data=serial)
  elif entity_to_load in subrace_names:
    serial = rnr_utils.rnr_race.basic_constructor(rnr_utils.get_race_given_subrace(entity_to_load), entity_to_load).serialize()
    return render_template('display_subrace.html', data=serial)
  else:
    return render_template('display_error.html', entity_name=entity_to_load)

@app.route('/random')
def random_page():
  print('hit random')

  class_names = rnr_utils.get_all_class_names()
  class_names = [x.lower() for x in class_names]
  race_names = rnr_utils.get_all_subrace_names()
  race_names = [x.lower() for x in race_names]

  allowed_genders = request.args.getlist('allowed_genders',None)
  allowed_races = request.args.getlist('allowed_races',None)
  allowed_classes = request.args.getlist('allowed_classes',None)
  allowed_flaws = request.args.getlist('allowed_flaws', None)
  #roll_stats = request.args.get('roll_stats',0)
  
  # try:
  #   roll_stats = int(roll_stats)
  # except Exception as e:
  #   roll_stats = 0

  # roll_stats = True if roll_stats == 1 else False

  if len(allowed_genders) == 0 or len(allowed_races) == 0 or len(allowed_classes) == 0 or len(allowed_flaws) == 0:
    return render_template("rnr_character_form.html",rnr_classes=class_names, rnr_races=race_names)

  for gender in allowed_genders:
    if not gender in ['male', 'female']:
      allowed_genders.remove(gender)

  for race in allowed_races:
    if not race in race_names:
      allowed_races.remove(race)
  for rclass in allowed_classes:
    if not rclass in class_names:
      allowed_classes.remove(rclass)
  for flaw in allowed_flaws:
    if not flaw in ['flawed', 'flawless']:
      allowed_flaws.remove(flaw)

  if len(allowed_genders) == 0:
    allowed_genders = ['male', 'female']
  if len(allowed_races) == 0:
    allowed_races = race_names
  if len(allowed_classes) == 0:
    allowed_classes = class_names
  if len(allowed_flaws) == 0:
    allowed_flaws = ['flawed', 'flawless']

  chosen_gender = random.choice(allowed_genders)
  chosen_race   = random.choice(allowed_races)
  chosen_class  = random.choice(allowed_classes)
  chosen_flawed = random.choice(allowed_flaws)
  spellbook = None

  flawed = True if chosen_flawed == 'flawed' else False

  chosen_name = names.get_first_name(gender=chosen_gender.lower())

  chosen_race_parent = rnr_utils.get_race_given_subrace(chosen_race)
  description = rnr_descriptions.getCharacterDescription(chosen_name,chosen_race_parent,chosen_class,chosen_gender,flawed=flawed)
  
  male=True if chosen_gender.lower() == 'male' else False

  character = rnr_utils.rnr_character(chosen_name, chosen_race_parent, chosen_race, chosen_class, level=3,male=male,character_origin=description)
  serial = character.serialize()

  serial_class = rnr_utils.rnr_class(chosen_class).serialize()


  spellbook = None
  if chosen_class.lower() in rnr_utils.GLOBAL_MAGIC_CLASSES.keys():
    spellbook = rnr_utils.get_random_spellbook(chosen_class, character.rnr_class_obj.get_spell_counts())

  return render_template("character_sheet.html",character=serial,icons=site_utils.which_icons(chosen_race_parent, chosen_race), spells=spellbook, class_data=serial_class)

@app.route('/blank_character_sheet')
def blank_character_sheet():
  print('hit blank')
  serial = {
    'subrace' : None,
    'character_name' : '', 
    'class' : None, 
    'subclass' : None, 
    'gender' : None, 
    'abilities': {'general' : [], 'advantage' : [], 'disadvantage' : [], 'combat' : []}
    }
  return render_template("character_sheet.html",character=serial,icons=site_utils.which_icons("human", "fighter"), spells=None, class_data=None)

@app.route('/spells')
def spell_page():
  print('hit spells')
  rnr_class = request.args.get('chosen_class','').lower()
  return spell_page_helper('spells/print_spell_page', rnr_class)

def spell_page_helper(next_page, rnr_class, name=None, race=None, subrace=None, level=None, gender=None ):
  print('hit spell helper')
  if rnr_class.lower() in rnr_utils.GLOBAL_MAGIC_CLASSES.keys():
    spellbook_name, data = rnr_utils.join_spellbooks(rnr_class)
    spell_data = dict()
    spell_data[spellbook_name] = data
  elif rnr_class == 'all':
    spell_data = rnr_utils.get_all_spellbooks()
  else:
    spell_data = dict()

  return render_template("spell_form.html", data=spell_data, rnr_class=rnr_class, next_page=next_page, name=name, race=race, subrace=subrace, level=level, gender=gender)


@app.route('/spells/print_spell_page', methods=['POST',])
def print_spell_page():
  print('hit print spell_page')
  spells = request.form.getlist('spells', None)
  spellbook = rnr_utils.gather_spells(spells)
  return render_template("spellbook.html", spellbook = spellbook, name = 'Bilgolf', rnr_class = None)

@app.route('/level_up')
def level_up_page():
  print('hit level up')
  rnr_class_name = request.args.get('chosen_class','').title()
  if not rnr_class_name in rnr_utils.get_all_class_names():
    print('could not find {0} in classes.'.format(rnr_class_name))
    return render_template('homepage.html')
  
  try:
    r_class = rnr_utils.rnr_class(rnr_class_name)
  except:
    print('could not load class {0}'.format(rnr_class_name))
    return render_template('homepage.html')
  
  serial_data = r_class.serialize()
  return render_template("level_up_page.html",data=serial_data, class_name=rnr_class_name)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    rnr_utils.printLogo()
    rnr_utils.load_Rangers_And_Ruffians_Data()
    port = int(os.environ.get('PORT', 9000))
    if len(sys.argv) > 1 and sys.argv[1] == '--public':
      print("Don't forget to run the following command '{0}'".format('sudo ufw allow {0}/tcp'.format(port)))
      print("Run ifconfig to find the correct local network inet address.")
      app.run(host='0.0.0.0', port=port, threaded=True)
    else:
      app.run(port=port)

