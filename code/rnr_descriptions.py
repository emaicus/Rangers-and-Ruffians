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

# #moles
# unique_face = {
#   "unisex" : [
#     "has a face that goes blank when <HE'S_SHE'S> thinking",
#     "scrunches <HIS_HER> nose when <HE_SHE> laughs",
#     "has laugh lines",
#     "has frown lines",
#     "has deep crows feet",
#     "has heavy scarring on <HIS_HER> face",
#     "blushes"
#     "face is always a little flush",
#     "has a scar running down <HIS_HER> cheek",
#     "has a scar running over <HIS_HER> left eye",
#     "wears a single earring",
#     "has a tattoo on <HIS_HER> face",
#     "has dry, cracked lips"
#     "has pierced ears",
#     "pointed eyebrows",
#     "bushy eyebrows",
#     "arched eyebrows",
#     "straight eyebrows",
#     "plucked eyebrows",
#     "slightly pointed ears",  
#   ],
#   "male" :[
#   #all got pulled out to beards
#   ],
#   "female" : [
#    "has pierced ears",
#     "has a long neck",
#   ]
# }




def getHair(gender, name, race, bearded_override=False):
  if name == None:
    name = "he" if gender == "male" else "she"
  if race in hairless_races:
    if not race in hairless_head_descriptions:
      #this shouldn't happen, but we'll stumble on with an error.
      perror("The race {0} is hairless, but has no descriptions. Tell a developer!")
      return "{0} has a hairless head.".format(name)
    hair_feature = random.choice(hairless_head_descriptions[race])
    
    #sub in gender words (TODO: make this a function)
    return "{0} has {1}.".format(name, hair_feature) 
  else:
    #get my hair description
    my_possible_hair_descriptions = hair_description[gender] + hair_description['unisex']
    my_hair_description = random.choice(my_possible_hair_descriptions)
    #get my hair style
    my_possible_hair_styles = hair_style[gender] + hair_style['unisex']
    my_hair_style = random.choice(list(my_possible_hair_styles))

    my_possible_hair_colors = list(hair_colors['standard'])
    if race in fantasy_haired_races:
      my_possible_hair_colors += list(hair_colors['fantasy'])
    my_hair_color = random.choice(list(my_possible_hair_colors))

    ret_string = "{0} has {1} {2} hair, which <HE_SHE> wears {3}".format(name,my_hair_description,my_hair_color,my_hair_style)

    bearded = gender == "male" and random.choice([True, False])

    if bearded_override or race in always_bearded_races or bearded:
      my_facial_hair = random.choice(facial_hair)
      ret_string = "{0}, and {1}".format(ret_string, my_facial_hair)
    ret_string += '.\n'
    return gender_word_replacement(ret_string, gender)


def getEyes(gender, name):
  if name == None:
    name = "he" if gender == "male" else "she"

  my_eye_description = random.choice(eye_description)
  my_eye_color = random.choice(eye_color)

  ret_string = "{0} has {1}, {2} eyes.".format(name, my_eye_description, my_eye_color)
  return gender_word_replacement(ret_string, gender)


def getBody(gender, name, race):
  if name == None:
    name = "he" if gender == "male" else "she"
 
  allowed_skin_colors = []

  my_possible_physical_description = physical_description[gender] + physical_description['unisex']
  my_physical_description = random.choice(my_possible_physical_description)

  ret_string = "{0} {1}".format(name,my_physical_description)

  if race in skin_color:
    #flip a coin, go with race specific half the time.
    allowed_skin_colors += skin_color[race]
    my_skin_color = random.choice(allowed_skin_colors)
    ret_string += " and has {0} skin".format(my_skin_color)

  return gender_word_replacement(ret_string, gender)


def getQuirk(gender, name):
  if name == None:
    name = "he" if gender == "male" else "she"

  my_quirk = random.choice(physical_quirk[gender] + physical_quirk['unisex'])
  ret_string = "{0} {1}.".format(name, my_quirk)
  return gender_word_replacement(ret_string, gender)


def getFace(gender, name):
  if name == None:
    name = "he" if gender == "male" else "she"
  #my_nose = random.choice(noses[gender] + noses['unisex'])
  #my_face_structure = random.choice(face_structure[gender] + face_structure['unisex'])
  #my_mouth_and_cheeks = random.choice(mouth_and_cheeks[gender] + mouth_and_cheeks['unisex'])
  # my_unique_face_feature = random.choice(unique_face[gender] + unique_face['unisex'])
  #ret_string = "{0} has a {1} face with a {2} nose.\n<HE_SHE> {3}, and {4}".format(name, my_face_structure, my_nose, my_mouth_and_cheeks, my_unique_face_feature)
  my_face_shape   = random.choice(face_shape[gender] + face_shape['unisex'])
  my_face_feature = random.choice(face_feature[gender] + face_feature['unisex'])

  ret_string = "{0} has a {1} face {2}".format(name, my_face_shape, my_face_feature)

  return gender_word_replacement(ret_string, gender)


def gender_word_replacement(string, gender):
  my_gender_dict = gender_words[gender]
  for term in my_gender_dict.keys():
    string = string.replace(term, my_gender_dict[term])
  return string

def marchingTrain(reverse=False):
  with open('TRAINING_DICTIONARY.json', 'r') as infile:
    relations = json.load(infile)

  encountered_one = False
  for left_hand_side_type, left_hand_side_dicts in sorted(relations.items(), reverse=reverse):
    for l_dict in left_hand_side_dicts:
      left_hand_side_name = l_dict['name']
      for right_hand_side_type, right_hand_side_dicts in l_dict['items'].items():
        for l_dict in right_hand_side_dicts:
          if l_dict['score'] != 'MIA':
            continue
          right_hand_side_name = l_dict['name']
          encountered_one = True
          answer = rnr_utils.answerQuestion('Does {0} {1} EVER match with {2} {3}?'.format(left_hand_side_name, left_hand_side_type, right_hand_side_name, right_hand_side_type), ['y','n'],'')
          if answer == "n":
            val = 0
          elif answer == 'y':
            val = 1
          else:
            print("woah, how did this happen?")
            val = 1
          
          l_dict['score'] = val
        with open('TRAINING_DICTIONARY.json', 'w') as outfile:
          json.dump(relations, outfile, indent=4)
        if encountered_one:
          print("SAVED. You are ok to exit.")
          # stop = rnr_utils.confirm("Would you like to stop?", ("yes", "yes"),("no", "no"))
          # if stop:
          #   sys.exit(0)
  with open('TRAINING_DICTIONARY.json', 'w') as outfile:
    json.dump(relations, outfile, indent=4)




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

  # rnr_utils.printLogo()
  #updateDatabase('update.json')
 #initial_conversion_function()
 # generate_training_dictionary()  
  train()
 #generate_training_dictionary()
  #train()