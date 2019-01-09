import os
import flask
import sys
from flask import Flask,redirect, render_template
from flask import request
import rnr_utils
import cgi
import names
import random
import rnr_descriptions
import json

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

  class_names = rnr_utils.get_all_class_names()
  class_names = [x.lower() for x in class_names]
  race_names = rnr_utils.get_all_race_names()
  race_names = [x.lower() for x in race_names]

  chosen_gender = request.args.get('gender','')
  chosen_race = request.args.get('race','')
  chosen_class = request.args.get('class','')
  chosen_name = request.args.get('name','')
  valid_gender = valid_race = valid_class = valid_name = False
  tier = request.args.get('tier', 0)

  try:
    tier = int(tier)
  except Exception as e:
    tier = 0
  if tier not in [0,1]:
    tier = 1


  serial_data = list()
  page_objects = list()
  populated_value = ""
  forwarding_param = ""
  male = False

  next_char = "?"

  # TODO load gender pictures.
  if chosen_gender.lower() in ('male', 'female'):
    valid_gender = True
    male = True if chosen_gender.lower() == 'male' else False

  if chosen_race.lower() in race_names:
    valid_race = True


  if chosen_class.lower() in class_names:
    valid_class = True

  magic_class = False
  if chosen_class.lower() in ['wizard','bard','cleric','paladin']:
    magic_class=True

  chosen_name = cgi.escape(chosen_name)
  if chosen_name != '':
    valid_name = True


  if valid_gender and valid_race and valid_class and valid_name == False:
    print("The name {0} was invalid".format(chosen_name))
    random_name = names.get_first_name(gender=chosen_gender.lower())
    return render_template("user_name_form.html", gender=chosen_gender.lower(), race=chosen_race.lower(), rnr_class=chosen_class.lower(), random_name=random_name.title())

  if valid_gender and valid_race and valid_class and valid_name:
    print("the name '{0}' was valid".format(chosen_name))
    character = rnr_utils.load_race_class_with_names(chosen_race.title(), chosen_class.title(), name=chosen_name)
    serial = character.serialize()
    return render_template("rnr_character_sheet.html",character=serial,tier=tier,magic_class=magic_class)

  if not valid_gender:
    for gender in ("male", "female"):
      serial = dict()
      serial["stats"] = {}
      serial["name"] = gender
      serial["abilities"] = {}
      serial["description"] = '''Your chosen gender can affect the way that you roleplay your character
                                 in Rangers and Ruffians. However, it should not affect your chosen race
                                 or class. While using the website, your chosen gender will affect the 
                                 race and class images that are displayed.
                              '''
      serial["standings"] = ''
      serial["path_to_image"] = "/static/images/gender/{0}.jpg".format(gender.lower())

      with open('../data/art.json','r') as art_json:
        art = json.load(art_json)

      serial['rights'] = art.get(gender.lower(), None)

      serial_data.append(serial)
    populated_value = "gender"
  else:
    forwarding_param = "{0}{1}gender={2}".format(forwarding_param,next_char,chosen_gender.lower())
    next_char = "&"

  if not valid_race:
    if valid_gender:
      page_objects = rnr_utils.load_all_race_objects()
      populated_value = "race"
  else:
    forwarding_param = "{0}{1}race={2}".format(forwarding_param,next_char,chosen_race.lower())
    next_char = "&"
  
  if not valid_class:
    if valid_race and valid_gender:
      page_objects = rnr_utils.load_all_class_objects()
      populated_value = "class"
  else:
    forwarding_param = "{0}{1}class={2}".format(forwarding_param,next_char,chosen_class.lower())
    next_char = "&"

  for entity in page_objects:
    serial = entity.serialize(male)
    serial_data.append(serial)

  populated_value = "{0}{1}".format(next_char,populated_value)
  next_page = "/creation"
  
  return render_template("display_page.html", data=serial_data, next_page=next_page, forwarding_param=forwarding_param, next_param = populated_value, tier=tier)

@app.route('/random')
def random_page():

  class_names = rnr_utils.get_all_class_names()
  class_names = [x.lower() for x in class_names]
  race_names = rnr_utils.get_all_race_names()
  race_names = [x.lower() for x in race_names]

  allowed_genders = request.args.getlist('allowed_genders',None)
  allowed_races = request.args.getlist('allowed_races',None)
  allowed_classes = request.args.getlist('allowed_classes',None)
  allowed_flaws = request.args.getlist('allowed_flaws', None)

  tier = request.args.get('tier', 0)

  try:
    tier = int(tier)
  except Exception as e:
    tier = 0

  if tier not in [0,1]:
    tier = 1

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
  if chosen_class.lower() in ['wizard','bard','cleric','paladin']:
    magic_class=True

  flawed = True if chosen_flawed == 'flawed' else False

  chosen_name = names.get_first_name(gender=chosen_gender.lower())

  description = rnr_descriptions.getCharacterDescription(chosen_name,chosen_race,chosen_class,chosen_gender,flawed=flawed)

  character = rnr_utils.load_race_class_with_names(chosen_race.title(), chosen_class.title(), name=chosen_name,origin=description)
  serial = character.serialize()
  return render_template("rnr_character_sheet.html",character=serial,tier=tier,magic_class=magic_class)

@app.route('/spells')
def spell_page():
  spell_books = rnr_utils.get_all_spellbooks_with_level()
  return render_template("spell_form.html", data=spell_books)

@app.route('/print_spell_page')
def print_spell_page():
  spells = request.args.getlist('chosen_spells', None)
  player_spellbook = rnr_utils.gather_spells(spells)
  return render_template("printable_spellbook.html",data=player_spellbook)



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    rnr_utils.printLogo()
    port = int(os.environ.get('PORT', 5015))
    app.run(host='0.0.0.0', port=port)