import json
import sys
import os
import yaml
import traceback
import random
import argparse
import time
import names
import uuid

import rnr_utils


def de_uuid(bad):
  new_dict = dict()
  for key, item in bad.items():
    for key2, item2 in item.items():
      if isinstance(item2, str):
        if not key in new_dict:
          new_dict[key] = list()
        new_dict[key].append(item2)
      else:
        if not key in new_dict:
          new_dict[key] = dict()
        if not key2 in new_dict[key]:
          new_dict[key][key2] = list()
        for key3, item3 in item2.items():
          new_dict[key][key2].append(item3)
  return new_dict


try:
  with open("description_database.json", 'r') as infile:
    tmp_file_in = json.load(infile)
    DESCRIPTIONS_DATABASE = de_uuid(tmp_file_in)
except Exception as e:

  print("ERROR: Could not locate description_database.json")
  sys.exit(1)

gender_words = {
  "male" : {
    "<HIMSELF_HERSELF>" : "himself",
    "<HIS_HER>" : "his",
    "<HE_SHE>" : "he",
    "<HIS_HER>" : "his",
    "<SAME_GENDER_MOTHER_FATHER>" : "father",
    "<SAME_GENDER_BROTHER_SISTER>" : "brother",
    "<SAME_GENDER_KING_QUEEN>" : "king",
    "<SAME_GENDER_PRIEST_PRIESTESS>" : "priest",
    "<SAME_GENDER_LORD_LADY>" : "lord",
    "<OPPOSITE_GENDER_MOTHER_FATHER>" : "mother",
    "<OPPOSITE_GENDER_MEN_WOMEN" : "women",
    "<OPPOSITE_GENDER_MAN_WOMAN" : "woman",
    "<OPPOSITE_GENDER_WITCH_WIZARD" : "witch",
    "<OPPOSITE_GENDER_HE_SHE" : "she",
    "<OPPOSITE_GENDER_BOY_GIRL>" : "girl",
    "<OPPOSITE_GENDER_HIM_HER>" : "her",
    "<OPPOSITE_GENDER_BROTHER_SISTER>" : "sister",
    "<OPPOSITE_GENDER_KING_QUEEN>" : "queen",
    "<OPPOSITE_GENDER_PRIEST_PRIESTESS>" : "priestess",
    "<OPPOSITE_GENDER_LORD_LADY>" : "lord",
    "<OPPOSITE_GENDER_SON_DAUGHTER>" : "daughter",
    "<OPPOSITE_GENDER_WIFE_HUSBAND>" : "wife",
    "<MAN_WOMAN>" : "man",
    "<DUDE_DUDETTE>" : "dude",
    "<HIM_HER>" : "him"
  },
  "female" : {
    "<HIMSELF_HERSELF>" : "herself",
    "<HIS_HER>" : "her",
    "<HE_SHE>" : "she",
    "<SAME_GENDER_MOTHER_FATHER>" : "mother",
    "<SAME_GENDER_BROTHER_SISTER>" : "sister",
    "<SAME_GENDER_KING_QUEEN>" : "queen",
    "<SAME_GENDER_PRIEST_PRIESTESS>" : "priestess",
    "<SAME_GENDER_LORD_LADY>" : "lady",
    "<OPPOSITE_GENDER_MOTHER_FATHER>" : "father",
    "<OPPOSITE_GENDER_MEN_WOMEN" : "men",
    "<OPPOSITE_GENDER_MAN_WOMAN" : "man",
    "<OPPOSITE_GENDER_WITCH_WIZARD" : "wizard",
    "<OPPOSITE_GENDER_HE_SHE" : "he",
    "<OPPOSITE_GENDER_BOY_GIRL>" : "boy",
    "<OPPOSITE_GENDER_HIM_HER>" : "him",
    "<OPPOSITE_GENDER_BROTHER_SISTER>" : "brother",
    "<OPPOSITE_GENDER_KING_QUEEN>" : "king",
    "<OPPOSITE_GENDER_PRIEST_PRIESTESS>" : "priest",
    "<OPPOSITE_GENDER_LORD_LADY>" : "lady",
    "<OPPOSITE_GENDER_SON_DAUGHTER>" : "son",
    "<OPPOSITE_GENDER_WIFE_HUSBAND>" : "husband",
    "<MAN_WOMAN>" : "woman",
    "<DUDE_DUDETTE>" : "dudette",
    "<HIM_HER>" : "her"
  }
}

introductions = [
  "What about trying",
  "Tu-tu-ru, Mayuri thinks you could totally cosplay as this character",
  "Wouldn't it be cool to be",
  "What if you tried being",
  "Oh shit, what if you were",
  "Hot damn, what about playing as",
  "Now hear me out, what if you played as",
  "This might sound a little crazy, but what if you tried being",
  "Hey, what about",
  "Don't you think it would be interesting to step into the shoes of",
  "Oh snap, what if you tried playing",
  "Don't you think roleplay would be simple if you were",
  "Don't you think everyone would be jealous if you played",
  "Hey hey hey! What if you were to be",
  "Son of a bitch! I think I've got it! What about",
  "Gods above! It's perfect! What if you tried playing"
]

hairless_races = ["Lizkin"]
always_bearded_races = ["Dwarf"]
bearded_races = ["Gnome", "Halfling", "Human", "Orc", "Dwarf", "Daemonspawn"]
human_like_skin = ['Elf', "Gnome", "Halfling","Human","Dwarf"]

def getHairDescription(race, male):
  global DESCRIPTIONS_DATABASE
  hair_description = DESCRIPTIONS_DATABASE['hair_descriptions']
  gender = "male" if male else "female"

  if race in hairless_races:
    return None
  else:
    #get my hair description
    my_possible_hair_descriptions = hair_description[gender] + hair_description['unisex']
    my_hair_description = random.choice(my_possible_hair_descriptions)
    return my_hair_description

def getHairlessDescription(race):
  global DESCRIPTIONS_DATABASE
  hairless_races = DESCRIPTIONS_DATABASE['hairless_head_descriptions']


  if race not in hairless_races:
    return None
  else:
    #get my hair description
    return random.choice(hairless_races[race])


def getHairStyle(male):
  #get my hair style
  global DESCRIPTIONS_DATABASE
  hair_style = DESCRIPTIONS_DATABASE['hair_styles']  
  gender = "male" if male else "female"
  my_possible_hair_styles = hair_style[gender] + hair_style['unisex']
  my_hair_style = random.choice(list(my_possible_hair_styles))
  return my_hair_style

def getHairColor(male):
  global DESCRIPTIONS_DATABASE
  hair_colors = DESCRIPTIONS_DATABASE['hair_colors']   
  # if race in fantasy_haired_races:
  #   my_possible_hair_colors += list(hair_colors['fantasy'])
  my_hair_color = random.choice(hair_colors)
  return my_hair_color


def getBeard(male, bearded_override=False):
  facial_hair = DESCRIPTIONS_DATABASE["beards"]
  bearded = (male and random.choice([True, False])) or bearded_override

  my_facial_hair = None
  if bearded:
    my_facial_hair = random.choice(facial_hair)
  return my_facial_hair


def getEyeDescription():
  global DESCRIPTIONS_DATABASE
  eye_description = DESCRIPTIONS_DATABASE['eye_descriptions']
  return random.choice(eye_description)
  
def getEyeColor():
  global DESCRIPTIONS_DATABASE
  eye_color = DESCRIPTIONS_DATABASE['eye_colors']
  return random.choice(eye_color)

def getBody(male):
  global DESCRIPTIONS_DATABASE
  physical_description = DESCRIPTIONS_DATABASE['physical_descriptions']
  gender = "male" if male else "female"
 
  my_possible_physical_description = physical_description[gender] + physical_description['unisex']
  return random.choice(my_possible_physical_description)
 
def getUniqueRaceDescription(race):
  global DESCRIPTIONS_DATABASE
  unique_races = DESCRIPTIONS_DATABASE['skin_colors']
  if race in unique_races:
    return random.choice(unique_races[race])
  else:
    return None

# def getQuirk(gender, name):
#   if name == None:
#     name = "he" if gender == "male" else "she"

#   my_quirk = random.choice(physical_quirk[gender] + physical_quirk['unisex'])
#   ret_string = "{0} {1}.".format(name, my_quirk)
#   return gender_word_replacement(ret_string, gender)


def getFaceShape(male):
  global DESCRIPTIONS_DATABASE
  face_shape = DESCRIPTIONS_DATABASE['face_shapes']
  gender = "male" if male else "female"
  
  return random.choice(face_shape[gender] + face_shape['unisex'])
  
def getFaceFeature(male):
  global DESCRIPTIONS_DATABASE
  face_features = DESCRIPTIONS_DATABASE['face_features']
  gender = "male" if male else "female"

  return random.choice(face_features[gender] + face_features['unisex'])

def getOrigins(race, rnr_class):
  global DESCRIPTIONS_DATABASE
  origins = DESCRIPTIONS_DATABASE['origins']
  return random.choice(origins)

def getWeakness(race, rnr_class):
  global DESCRIPTIONS_DATABASE
  weaknesses = DESCRIPTIONS_DATABASE['weaknesses']
  return random.choice(weaknesses)

def getName(race,male):
  gender = "male" if male else "female"
  return names.get_first_name(gender=gender.lower())



def gender_word_replacement(string, gender):
  my_gender_dict = gender_words[gender]
  for term in my_gender_dict.keys():
    string = string.replace(term, my_gender_dict[term])
  return string



def getCharacterDescription(allowed_races=None, allowed_classes=None, allowed_genders=None):
  if allowed_races == None:
    allowed_races = rnr_utils.get_all_race_names()
  if allowed_classes == None:
    allowed_classes = rnr_utils.get_all_class_names()
  if allowed_genders == None:
    allowed_genders = ["male", "female"]

  my_race  = random.choice(allowed_races)
  my_class = random.choice(allowed_classes)
  my_gender = random.choice(allowed_genders)
  male = True if my_gender == "male" else False

  my_hair_description = getHairDescription(my_race, male)
  my_hair_style = getHairStyle(male)
  my_hair_color = getHairColor(male)
  my_beard = getBeard(male)
  my_eye_description = getEyeDescription()
  my_eye_color = getEyeColor()
  my_physical_description = getBody(male)
  my_face_shape = getFaceShape(male)
  my_face_feature =  getFaceFeature(male)
  my_name = getName(my_race,male)
  my_origins = getOrigins(my_race, my_class)
  my_weakness = getWeakness(my_race,my_class)
  my_unique_race_description = getUniqueRaceDescription(my_race)

  ret = "{0}, the {1} {2}\n".format(my_name, my_race, my_class) 
  #origins
  ret += "{0} {1}. ".format(my_name, my_origins)
  #physical description
  ret += "<HE_SHE> {0},".format(my_physical_description)
  #hair
  if my_hair_description != None:
    if my_race != "Catterwol":
      ret += " and has {0}, {1} hair".format(my_hair_description, my_hair_color)
      if not male:
        if random.choice([True,False]):
          ret += ", which she wears {0}. ".format(my_hair_style)
        else:
          ret += ". "
      elif my_beard != None:
        ret += " and {0}. ".format(my_beard)
      else:
        ret += ". "
    else:
      style = random.choice(["short cut", "matted", "luminous", "long", "soft", "coarse"])
      ret += " and has {0}, {1} fur.".format(style, my_hair_color)
  else:
    my_hairless_description = getHairlessDescription(my_race)
    ret += " and has {0}. ".format(my_hairless_description)

  ret += "<HIS_HER> eyes are {0} and {1}, and <HE_SHE> has {3}. ".format(my_eye_color, my_eye_description, my_face_shape, my_face_feature)

  if my_unique_race_description != None:
    ret += "<HE_SHE> has {0}. ".format(my_unique_race_description)

  ret += "{0} {1}.".format(my_name, my_weakness)

  if my_class == "Beastmaster":
    my_animal_male = random.choice([True,False])
    my_animal_name = getName("animal",my_animal_male)
    animal_type = random.choice(["Wolf", "Dire Wolf", "Bear", "Hawk"])
    ret += "\n\n{0} has a companion {1} named {2}".format(my_name, animal_type, my_animal_name)

  return gender_word_replacement(ret, my_gender)






def fill_in_default(dic, left_hand_side_type, right_hand_side_type, target_rhs_name, val):
    for l_dict in dic[left_hand_side_type]:
      left_hand_side_name = l_dict['name']
      #for right_hand_side_type, right_hand_side_dicts in l_dict['items'].items():
      right_hand_side_dicts = l_dict['items'][right_hand_side_type]

      for r_dict in right_hand_side_dicts:
        if r_dict['score'] != 'MIA':
          continue
        right_hand_side_name = r_dict['name']
        right_hand_side_uuid = r_dict['uid']

        if right_hand_side_name != target_rhs_name:
          continue
        r_dict['score'] = val 

        print('Setting {0} {1} {2} {3} to {4}'.format(left_hand_side_name, left_hand_side_type, right_hand_side_name, right_hand_side_type, val))


def marchingTrain(reverse=False, my_name=''):
  with open('TRAINING_DICTIONARY.json', 'r') as infile:
    relations = json.load(infile)

  if my_name == 'Oliver':
    print("Hello Oliver! It's good to see you!")
    responsibilities = ['origins', 'eye_colors', 'rnr_classes']
  elif my_name == 'Evan':
    print("Evan coming online.")
    responsibilities = ['ages', 'hair_colors', 'physical_descriptions']
  else:
    print("Oliver, if you are seeing this, tell Evan! (he forgot to configure the program to run for you)")
    responsibilities = ['ages', 'origins', 'hair_colors', 'eye_colors', 'physical_descriptions', 'rnr_classes']


  encountered_one = False
  for left_hand_side_type, left_hand_side_dicts in sorted(relations.items(), reverse=reverse):
    if not left_hand_side_type in responsibilities:
      continue
    for l_dict in left_hand_side_dicts:
      left_hand_side_name = l_dict['name']
      for right_hand_side_type, right_hand_side_dicts in l_dict['items'].items():
        for r_dict in right_hand_side_dicts:
          if r_dict['score'] != 'MIA':
            continue
          right_hand_side_name = r_dict['name']
          right_hand_side_uuid = r_dict['uid']
          encountered_one = True
          
          answer = rnr_utils.answerQuestion("Does '{0}' {1} EVER match with '{2}' {3}?".format(left_hand_side_name, left_hand_side_type, right_hand_side_name, right_hand_side_type), ['y','n','all', 'none'],'')
          if answer == "n":
            val = 0
          elif answer == 'y':
            val = 1
          elif answer == 'all':
            fill_in_default(relations, left_hand_side_type, right_hand_side_type, right_hand_side_name, 1)
            val = 1
          elif answer == "none":
            fill_in_default(relations, left_hand_side_type, right_hand_side_type, right_hand_side_name, 0)
            val = 0
          else:
            print("woah, how did this happen?")
            val = 1

          
          r_dict['score'] = val
        with open('TRAINING_DICTIONARY.json', 'w') as outfile:
          json.dump(relations, outfile, indent=4)
        if encountered_one:
          print("SAVED. You are ok to exit.")
          # stop = rnr_utils.confirm("Would you like to stop?", ("yes", "yes"),("no", "no"))
          # if stop:
          #   sys.exit(0)
  with open('TRAINING_DICTIONARY.json', 'w') as outfile:
    json.dump(relations, outfile, indent=4)
  print("YOU DID IT! All finished!")



    #   for 
    # for i_uid in relations[o_uid].keys():

    #   ans = input("does {0} {1} EVER match with {2} {3}".format(printUID(o_uid), o_lname, printUID(i_uid), i_lname))


def updateDatabase(file_path):
  with open(file_path, 'r') as infile:
    update_file = json.load(infile)
  with open('description_database.json', 'r') as infile:
    database = json.load(infile)
  with open('description_database_BACKUP.json', 'w') as outfile:
    json.dump(database, outfile, indent=4)

  for list_name, values in update_file.items():
    if not list_name in database:
      if rnr_utils.confirm("Attempting to add new list name {0} to database. Is that what you were trying to do?".format(list_name), ("yes", "yes"), ("no", "no")):
        database[list_name] = dict()
      else :
        print("Shutting down. Please fix the error before rerunning")
        sys.exit(1)

    if isinstance(values, list):
      print('updating {0} with {1}'.format(list_name, values))
      database[list_name].update(to_uid_dict(values))
      continue
    elif isinstance(values, dict):
      for key, details in values.items():
        if not key in database[list_name]:
          if rnr_utils.confirm("Attempting to add new key {0} to list {1} in database. Is that what you were trying to do?".format(key, list_name), ("yes", "yes"), ("no", "no")):
            database[list_name][key] = dict()
          else:
            print('Shutting down. Please fix the error before rerunning.')
            sys.exit(1)
        print('2 updating {0} {1} with {2}'.format(list_name, key, values))
        database[list_name][key].update(to_uid_dict(details))
    else:
      print("Bad entry {0}. Please fix and run again.".format(details))
      sys.exit(1)

  # with open(file_path, 'w') as infile:
  #   pass

  with open('description_database.json', 'w') as outfile:
    json.dump(database, outfile, indent=4)








def train():
  marchingTrain()

#takes in a list or a dict of lists.
def aggregate(obj):
  if isinstance(obj, list):
    return obj
  if len(obj) == 0:
    return obj

  dic = dict()
  for key, details in obj.items():
    if not isinstance(details, dict):
      return obj
    dic.update(details)
  return dic

def to_uid_dict(obj):
  if isinstance(obj, list):
    return lis_to_uid_dict(obj)
  elif isinstance(obj, dict):
    return dict_to_uid_dict(obj)
  else:
    print("BAD TYPE GIVE TO to_uid_dict")
    sys.exit(1)

def lis_to_uid_dict(lis):
  dic = dict()
  for item in lis:
    uid = str(uuid.uuid4())
    dic[uid] = item
  return dic

def dict_to_uid_dict(input_dict):
  dic = dict()
  for key in input_dict.keys():
    dic[key] = lis_to_uid_dict(input_dict[key])
  return dic

def generate_training_dictionary():
  with open('description_database.json', 'r') as infile:
    database = json.load(infile)
  print(database.keys())
 
  if rnr_utils.confirm("You have asked to regenerate the random training dictionary. This will delete past progress. Are you certain this is what you want?", ("yes", "yes"), ("no", "no")):
    if rnr_utils.confirm("LAST CHECK. DO YOU WANT TO DELETE ALL TRAINING DATA AND REGENERATE?", ("yes, I want to delete my data", "yes"), ("no","no")):

      relationships = {
        'ages' : ['weaknesses', 'origins', 'hair_colors', 'physical_descriptions', 'face_shapes', 'physical_quirks', 'hair_styles', 'face_features'],
        'origins' : ['eye_descriptions', 'face_features', 'physical_descriptions',"face_features"],
        'hair_colors' : ['eye_colors',],
        'eye_colors' : ['eye_descriptions',],
        'physical_descriptions' : ['face_shapes',"physical_quirks","face_features"],
        'rnr_classes' : ['origins',]
      }

      train = dict()

      for master, slave in relationships.items():
        train[master] = list()
        for u_id, name in aggregate(database[master]).items():
          chunk = dict()
          chunk['uid'] = u_id
          chunk['name'] = name
          chunk['items'] = dict()
          for term in slave:
            chunk['items'][term] = list()
            for i_uid, i_name in  aggregate(database[term]).items():
              chunk['items'][term].append({'uid':i_uid, 'name':i_name, 'score':'MIA'})
          train[master].append(chunk)
    else:
      return
  else:
    return
  with open('TRAINING_DICTIONARY.json', 'w') as outfile:
    json.dump(train, outfile, indent=4)

if __name__ == "__main__":
  char = getCharacterDescription()
  print(char)
 # rnr_utils.convert_json_file_to_yml_file('TRAINING_DICTIONARY.json','out.yml')
  # rnr_utils.printLogo()
  #updateDatabase('update.json')
 #initial_conversion_function()
 # generate_training_dictionary()  
 # marchingTrain(my_name = 'Evan')
 #generate_training_dictionary()
  #train()