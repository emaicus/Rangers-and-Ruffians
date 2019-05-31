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

'''
Helper functions
'''
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

    with open('../data/art.json','r') as art_json:
      art = json.load(art_json)

    serial['rights'] = art.get(gender.lower(), None)

    serial_data.append(serial)
  return serial_data

def validity_check():
  print(json.dumps(request.args, indent=4))
  class_names = rnr_utils.get_all_class_names()
  class_names = [x.lower() for x in class_names]
  subrace_names = rnr_utils.get_all_subrace_names()
  subrace_names = [x.lower() for x in subrace_names]
  valid_levels = ['0','1','2','3','4','5','6','7','8','9','10']
  info = dict()
  chosen_gender = request.args.get('gender','')
  chosen_subrace = request.args.get('subrace','')
  chosen_class = request.args.get('class','')
  chosen_name = request.args.get('name','')
  roll_stats = request.args.get('roll_stats',0)
  level = request.args.get('level', '')

  try:
    roll_stats = int(roll_stats)
  except Exception as e:
    roll_stats = 0
  
  roll_stats   = True if roll_stats == 1 else False
  
  print(subrace_names)
  print(chosen_subrace)
  chosen_subrace  = chosen_subrace.lower() if chosen_subrace.lower() in subrace_names else None

  chosen_class = chosen_class.lower() if chosen_class.lower() in class_names else None
  magic_class  = True if chosen_class != None and chosen_class.lower() in rnr_utils.magical_classes.keys() else False
  chosen_name = cgi.escape(chosen_name)
  chosen_name = None if chosen_name.strip() == '' else chosen_name
  chosen_gender = chosen_gender.lower() if chosen_gender.lower() in ('male', 'female') else None
  chosen_level = int(level) if level in valid_levels else None

  info['name'] = chosen_name
  info['magic_class'] = magic_class
  info['class'] = chosen_class
  info['subrace'] = chosen_subrace
  info['roll_stats'] = roll_stats
  info['gender'] = chosen_gender
  info['level'] = chosen_level

  return info

def generate_redirect_string(param_map):
  ret = '?'
  for key in ['gender','subrace','class','name']:
    if param_map[key] != None:
      ret = '{0}{1}={2}&'.format(ret,key,param_map[key])
  #fist char is a ?, then & everything
  print('forwarding param {0}'.format(ret))
  return ret

#Order of operations: gender, race, class, name
def find_first_invalid_value(params):
  for key in ['gender','subrace','class','name', 'level']:
    if params[key] == None:
      print('returning {0}'.format(key))
      return key
  return None


'''
Flask app
'''

app = Flask(__name__, static_url_path='/static')

# @app.route('/races')
@app.route('/')
def index_page():
  return render_template('homepage.html')

@app.route('/legal')
def legal():
  with open('../data/art.json','r') as art_json:
    art = json.load(art_json)  
  return render_template('legal.html',art=art)

@app.route('/creation')
def creation_landing_page():
  #return render_template("iterated_display_page.html")
  # info = {'gender' : 'female'}
  # serial_data = populate_race(info)
  # return render_template("new_display_page.html", data=serial_data)

  page_objects = None
  populated_value = ""
  forwarding_param = ""
  serial_data = list()
  
  info = validity_check()
  next_to_populate = find_first_invalid_value(info)
  redirect_string = generate_redirect_string(info)

  prev_stats = None
  if info['class'] != None:
    prev_stats = rnr_utils.rnr_class(info['class']).stats
  if info['subrace'] != None:
    subrace = info['subrace'].replace('_', ' ')
    race = rnr_utils.get_race_given_subrace(subrace)
    prev_stats = rnr_utils.rnr_race(race, subrace).stats

  if next_to_populate == 'name' or next_to_populate == 'level':
    print("The name {0} was invalid".format(info['name']))
    random_name = names.get_first_name(gender=info['gender'])
    return render_template("user_name_form.html", chosen_gender=info['gender'], chosen_subrace=info['subrace'], chosen_rnr_class=info['class'], all_genders=['male','female'], all_races=rnr_utils.get_all_race_names(), all_rnr_classes=rnr_utils.get_all_class_names(), random_name=random_name.title())
  elif next_to_populate == 'gender':
    serial_data = populate_gender()
    return render_template("display_page.html", data=serial_data, next_page='/creation', forwarding_param=redirect_string, next_param='gender',prev_stats=None,display_class=False)
  elif next_to_populate == 'class':
    serial_data = populate_class(info)
    return render_template("display_page.html", data=serial_data, next_page='/creation', forwarding_param=redirect_string, next_param='class',prev_stats=prev_stats,display_class=True)
  elif next_to_populate == 'subrace':
    serial_data = populate_race(info)
    return render_template("display_page.html", data=serial_data, next_page='/creation', forwarding_param=redirect_string, next_param='subrace',prev_stats=prev_stats,display_class=False)
  else:
    subrace = info['subrace'].replace('_', ' ')
    race = rnr_utils.get_race_given_subrace(subrace)
    male=True if info['gender'].lower() == 'male' else False
    character = rnr_utils.rnr_character(info['name'],race,subrace,info['class'],info['level'], male=male)
    serial = character.serialize()
    return render_template("iterated_char_sheet.html",character=serial,magic_class=info['magic_class'])

@app.route('/ajax_load_content', methods=['POST',])
def ajax_load_content():
  class_names = rnr_utils.get_all_class_names()
  class_names = [x.lower() for x in class_names]
  subrace_names = rnr_utils.get_all_subrace_names()
  subrace_names = [x.lower() for x in subrace_names]

  entity_to_load = request.form.get('entity_to_load','NO ENTITY SPECIFIED').lower()

  if entity_to_load in class_names:
    serial = rnr_utils.rnr_class(entity_to_load, level=10, subclass="").serialize()
    return render_template('display_class.html', data=serial)
  elif entity_to_load in subrace_names:
    serial = rnr_utils.rnr_race(rnr_utils.get_race_given_subrace(entity_to_load), entity_to_load).serialize()
    return render_template('display_subrace.html', data=serial)
  else:
    return render_template('display_error.html', entity_name=entity_to_load)

@app.route('/random')
def random_page():

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

  magic_class = False
  if chosen_class.lower() in rnr_utils.magical_classes.keys():
    magic_class=True

  flawed = True if chosen_flawed == 'flawed' else False

  chosen_name = names.get_first_name(gender=chosen_gender.lower())

  chosen_race_parent = rnr_utils.get_race_given_subrace(chosen_race)
  description = rnr_descriptions.getCharacterDescription(chosen_name,chosen_race_parent,chosen_class,chosen_gender,flawed=flawed)
  
  male=True if chosen_gender.lower() == 'male' else False

  character = rnr_utils.rnr_character(chosen_name, chosen_race_parent, chosen_race, chosen_class, 0,male=male,character_origin=description)
  serial = character.serialize()
  return render_template("new_character_sheet.html",character=serial,magic_class=magic_class)

@app.route('/spells')
def spell_page():
  chosen_class = request.args.get('chosen_class','').lower()
  chosen_name = request.args.get('chosen_name', None)
  spell_data = dict()
  spell_books = rnr_utils.get_all_spellbooks()
  if chosen_class.lower() in rnr_utils.magical_classes.keys():
    book_list = list()
    for book_name in rnr_utils.magical_classes[chosen_class]:
      print('we are appendinging {0} to {1}'.format(book_name, chosen_class))
      book_list.append(book_name)
    print(book_list)
    big_book_name = ' and '.join(book_list)
    spell_data[big_book_name] = dict()
    for book_name in rnr_utils.magical_classes[chosen_class]:
      for chapter, pages in spell_books[book_name].items():
        if not chapter in spell_data[big_book_name]:
          spell_data[big_book_name][chapter] = dict()
        for spell_name, spell_info in pages.items():
          print(book_name, chapter, spell_name)
          if not spell_name in spell_data[big_book_name][chapter]:
            spell_data[big_book_name][chapter][spell_name] = spell_info
  if chosen_class == 'all':
    spell_data = spell_books

  return render_template("spell_form.html", data=spell_data, chosen_name=chosen_name)

@app.route('/print_spell_page')
def print_spell_page():
  spells = request.args.getlist('chosen_spells', None)
  chosen_name = request.args.get('chosen_name')
  player_spellbook = rnr_utils.gather_spells(spells)
  return render_template("printable_spellbook.html",data=player_spellbook,chosen_name=chosen_name)

@app.route('/level_up')
def level_up_page():
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
    port = int(os.environ.get('PORT', 5015))
    app.run(host='0.0.0.0', port=port)
