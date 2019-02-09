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

magical_classes = {
  'bard' : ["the_bard's_songbook",],
  'cleric' : ['the_book_of_healing',],
  'paladin' : ['the_book_of_healing',],
  'wizard' : ['the_novice_spellbook', "the_wizard's_addendum"],
  'sorcerer' : ['the_novice_spellbook', "the_sorcerer's_scrolls"],
  'druid' : ['the_novice_spellbook', "the_druid's_guidebook"],
  'necromancer' : ['the_macabre_manual',],
  'monk' : ['the_book_of_chi',],
  'battle mage' : ['the_novice_spellbook',] 
}

tier_map = {
  'new_character' : 0,
  'heroic_character' : 1,
  'legendary_character' : 2
}

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
  global tier_map


  page_objects = None
  populated_value = ""
  forwarding_param = ""
  next_char = "?"
  serial_data = None
  
  info = validity_check()

  #Just need a name.
  if info['tier'] != None and info['gender'] != None and info['race'] != None and info['class'] != None and info['name'] == None:
    print("The name {0} was invalid".format(info['name']))
    random_name = names.get_first_name(gender=info['gender'])
    return render_template("user_name_form.html", gender=info['gender'], race=info['race'], rnr_class=info['class'], random_name=random_name.title(), tier=info['tier'])

  #All set!
  if info['gender'] != None and info['race'] != None and info['class'] != None and info['name'] != None and info['tier'] != None:
    character = rnr_utils.load_race_class_with_names(info['race'].title(), info['class'].title(), name=info['name'], roll_stats=info['roll_stats'],tier=tier_map[info['tier']])
    serial = character.serialize()
    return render_template("rnr_character_sheet.html",character=serial,tier=info['tier'],magic_class=info['magic_class'],chosen_name=info['name'])

  if info['tier'] == None:
    if serial_data == None:
      serial_data = populate_tier()
      populated_value = "tier"
  else:
    forwarding_param = "{0}{1}tier={2}".format(forwarding_param,next_char,info['tier'])
    next_char = "&"

  if info['gender'] == None:
    if serial_data == None:
      serial_data = populate_gender()
      populated_value = "gender"
  else:
    forwarding_param = "{0}{1}gender={2}".format(forwarding_param,next_char,info['gender'])
    next_char = "&"

  if info['race'] == None:
    if serial_data == None:
      page_objects = rnr_utils.load_all_race_objects()
      populated_value = "race"
  else:
    forwarding_param = "{0}{1}race={2}".format(forwarding_param,next_char,info['race'])
    next_char = "&"
  
  if info['class'] == None:
    if page_objects == None and serial_data == None:
      page_objects = rnr_utils.load_all_class_objects(tier=tier_map[info['tier']])
      populated_value = "class"
  else:
    forwarding_param = "{0}{1}class={2}".format(forwarding_param,next_char,info['class'])
    next_char = "&"

  prev_stats = None
  if info['class'] != None and tier != None:
    prev_stats = rnr_utils.load_class(info['class'],tier=tier_map[info['tier']]).stats
  if info['race']:
    prev_stats = rnr_utils.load_race(info['race']).stats

  if page_objects != None and serial_data == None:
    serial_data = list()
    for entity in page_objects:
      male = True if info['gender'] == 'male' else False
      serial = entity.serialize(male)
      serial_data.append(serial)

  populated_value = "{0}{1}".format(next_char,populated_value)
  next_page = "/creation"
  
  return render_template("display_page.html", data=serial_data, next_page=next_page, forwarding_param=forwarding_param, next_param = populated_value, tier=info['tier'], prev_stats=prev_stats)

def populate_tier():
  with open('../data/art.json','r') as art_json:
      art = json.load(art_json)
  new_dict = dict()
  serial_data = list()
  new_dict["stats"] = None
  new_dict["name"] =  "New_Character"
  new_dict["abilities"] = None
  new_dict["description"] = "\
                  Ask your Poohbah what tier of character their campaign is meant for.\
                  \n\
                  New adventurers are just beginning their journey, and are still wet behind their ears.\
                  Their stats are lower than their heroic and legendary couterparts, and the challenges that \
                  they face will be simpler, but no less important. New adventurers must work hard to become\
                  the legends that they were meant to be!\
                  \n\
                  New adventurers are at home settling tavern brawls, hunting minor monsters, and helping with\
                  local issues."
  new_dict["path_to_image"] = "/static/images/tier/new.jpg"
  new_dict["rights"] = art.get("new", None)
  
  heroic_dict = dict()
  heroic_dict["stats"] = None
  heroic_dict["name"] =  "Heroic_Character"
  heroic_dict["abilities"] = None
  heroic_dict["description"] = "\
                  Ask your Poohbah what tier of character their campaign is meant for.\
                  \n\
                  Heroic adventurers have accomplished mighty deeds, and are on the path to accomplish more.\
                  The are becoming established in their lands, and have grown stronger through months or years\
                  of hard training. Heroes are stronger, sturdy, and more worldwise than new adventurers, but\
                  have not yet hit legendary status.\
                  \n\
                  With careful planning and the right equiptment, heroic characters can slay drakes, take on vampires,\
                  and play complex political games."
  heroic_dict["path_to_image"] = "/static/images/tier/heroic.jpg"
  heroic_dict["rights"] = art.get("heroic", None)
  
  legendary_dict = dict()
  legendary_dict["stats"] = None
  legendary_dict["name"]  = "Legendary_Character"
  legendary_dict["abilities"] = None
  legendary_dict["description"] = "\
                  Ask your Poohbah what tier of character their campaign is meant for.\
                  \n\
                  Legendary adventurers have spent years becoming the best of the best. They are the archetype of their\
                  class, and have gained powerful abilities as a result. Legendary characters take on the worst that the \
                  world has to offer, and can affect real change that resonates throughout all of the land. Almost no\
                  adventures should begin with legendary characters.\
                  \n\
                  Legendary characters can challenge deities, vast networks of spies and enemies, and ancient or primordial beasts.\
                  "
  legendary_dict["path_to_image"] = "/static/images/tier/legendary.jpg"
  legendary_dict["rights"] = art.get("legendary", None)

  serial_data.append(new_dict)
  serial_data.append(heroic_dict)
  serial_data.append(legendary_dict)
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
  class_names = rnr_utils.get_all_class_names()
  class_names = [x.lower() for x in class_names]
  race_names = rnr_utils.get_all_race_names()
  race_names = [x.lower() for x in race_names]

  info = dict()
  chosen_gender = request.args.get('gender','')
  chosen_race = request.args.get('race','')
  chosen_class = request.args.get('class','')
  chosen_name = request.args.get('name','')
  tier = request.args.get('tier', '')
  roll_stats = request.args.get('roll_stats',0)

  try:
    roll_stats = int(roll_stats)
  except Exception as e:
    roll_stats = 0
  
  roll_stats   = True if roll_stats == 1 else False
  chosen_race  = chosen_race.lower() if chosen_race.lower() in race_names else None
  chosen_class = chosen_class.lower() if chosen_class.lower() in class_names else None
  magic_class  = True if chosen_class != None and chosen_class.lower() in magical_classes.keys() else False
  chosen_name = cgi.escape(chosen_name)
  chosen_name = None if chosen_name.strip() == '' else chosen_name
  chosen_gender = chosen_gender.lower() if chosen_gender.lower() in ('male', 'female') else None
  tier = tier.lower() if tier.lower() in ['new_character','heroic_character','legendary_character'] else None

  info['name'] = chosen_name
  info['magic_class'] = magic_class
  info['class'] = chosen_class
  info['race'] = chosen_race
  info['tier'] = tier
  info['roll_stats'] = roll_stats
  info['gender'] = chosen_gender

  return info



@app.route('/random')
def random_page():
  global tier_map

  class_names = rnr_utils.get_all_class_names()
  class_names = [x.lower() for x in class_names]
  race_names = rnr_utils.get_all_race_names()
  race_names = [x.lower() for x in race_names]

  allowed_genders = request.args.getlist('allowed_genders',None)
  allowed_races = request.args.getlist('allowed_races',None)
  allowed_classes = request.args.getlist('allowed_classes',None)
  allowed_flaws = request.args.getlist('allowed_flaws', None)
  tier = request.args.get('tier', '')
  tier = tier.lower() if tier.lower() in ['new_character','heroic_character','legendary_character'] else None

  roll_stats = request.args.get('roll_stats',0)
  
  try:
    roll_stats = int(roll_stats)
  except Exception as e:
    roll_stats = 0

  roll_stats = True if roll_stats == 1 else False

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
  if chosen_class.lower() in magical_classes.keys():
    magic_class=True

  flawed = True if chosen_flawed == 'flawed' else False

  chosen_name = names.get_first_name(gender=chosen_gender.lower())

  description = rnr_descriptions.getCharacterDescription(chosen_name,chosen_race,chosen_class,chosen_gender,flawed=flawed)

  character = rnr_utils.load_race_class_with_names(chosen_race.title(), chosen_class.title(), name=chosen_name,origin=description, roll_stats=roll_stats,tier=tier_map[tier])
  serial = character.serialize()
  return render_template("rnr_character_sheet.html",character=serial,magic_class=magic_class,chosen_name=chosen_name)

@app.route('/spells')
def spell_page():
  chosen_class = request.args.get('chosen_class','').lower()
  chosen_name = request.args.get('chosen_name', None)
  spell_data = dict()
  spell_books = rnr_utils.get_all_spellbooks()
  if chosen_class.lower() in magical_classes.keys():
    book_list = list()
    for book_name in magical_classes[chosen_class]:
      print('we are appendinging {0} to {1}'.format(book_name, chosen_class))
      book_list.append(book_name)
    print(book_list)
    big_book_name = ' and '.join(book_list)
    spell_data[big_book_name] = dict()
    for book_name in magical_classes[chosen_class]:
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



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    rnr_utils.printLogo()
    port = int(os.environ.get('PORT', 5015))
    app.run(host='0.0.0.0', port=port)