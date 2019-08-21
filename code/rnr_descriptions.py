import json
import sys
import os
import yaml
import traceback
import random
import argparse
import names
import rnr_utils

def getHairDescription(race, male):
  rnr_utils.load_Rangers_And_Ruffians_Data()
  hair_description = rnr_utils.GLOBAL_DESCRIPTIONS_DATABASE['hair_descriptions']
  gender = "male" if male else "female"

  if race.lower() in rnr_utils.GLOBAL_DESCRIPTIONS_DATABASE['hairless_races']:
    return None
  else:
    #get my hair description
    my_possible_hair_descriptions = hair_description[gender] + hair_description['unisex']
    my_hair_description = random.choice(my_possible_hair_descriptions)
    return my_hair_description

def getHairlessDescription(race):
  rnr_utils.load_Rangers_And_Ruffians_Data()
  hairless_races = rnr_utils.GLOBAL_DESCRIPTIONS_DATABASE['hairless_head_descriptions']

  if race.lower() not in hairless_races:
    return None
  else:
    #get my hair description
    return random.choice(hairless_races[race.lower()])

def getHairStyle(male):
  rnr_utils.load_Rangers_And_Ruffians_Data()
  #get my hair style
  hair_style = rnr_utils.GLOBAL_DESCRIPTIONS_DATABASE['hair_styles']  
  gender = "male" if male else "female"
  my_possible_hair_styles = hair_style[gender] + hair_style['unisex']
  my_hair_style = random.choice(list(my_possible_hair_styles))
  return my_hair_style

def getHairColor(male):
  rnr_utils.load_Rangers_And_Ruffians_Data()
  hair_colors = rnr_utils.GLOBAL_DESCRIPTIONS_DATABASE['hair_colors']   
  # if race in fantasy_haired_races:
  #   my_possible_hair_colors += list(hair_colors['fantasy'])
  my_hair_color = random.choice(hair_colors)
  return my_hair_color

def getBeard(male, bearded_override=False):
  rnr_utils.load_Rangers_And_Ruffians_Data()
  facial_hair = rnr_utils.GLOBAL_DESCRIPTIONS_DATABASE["beards"]
  bearded = (male and random.choice([True, False])) or bearded_override

  my_facial_hair = None
  if bearded:
    my_facial_hair = random.choice(facial_hair)
  return my_facial_hair

def getEyeDescription():
  rnr_utils.load_Rangers_And_Ruffians_Data()
  eye_description = rnr_utils.GLOBAL_DESCRIPTIONS_DATABASE['eye_descriptions']
  return random.choice(eye_description)
  
def getEyeColor():
  rnr_utils.load_Rangers_And_Ruffians_Data()
  eye_color = rnr_utils.GLOBAL_DESCRIPTIONS_DATABASE['eye_colors']
  return random.choice(eye_color)

def getBody(male):
  rnr_utils.load_Rangers_And_Ruffians_Data()
  physical_description = rnr_utils.GLOBAL_DESCRIPTIONS_DATABASE['physical_descriptions']
  gender = "male" if male else "female"
 
  my_possible_physical_description = physical_description[gender] + physical_description['unisex']
  return random.choice(my_possible_physical_description)
 
def getUniqueRaceDescription(race):
  rnr_utils.load_Rangers_And_Ruffians_Data()
  unique_races = rnr_utils.GLOBAL_DESCRIPTIONS_DATABASE['skin_colors']
  if race.lower() in unique_races:
    return random.choice(unique_races[race.lower()])
  else:
    return None

# def getQuirk(gender, name):
#   if name == None:
#     name = "he" if gender == "male" else "she"

#   my_quirk = random.choice(physical_quirk[gender] + physical_quirk['unisex'])
#   ret_string = "{0} {1}.".format(name, my_quirk)
#   return gender_word_replacement(ret_string, gender)


def getFaceShape(male):
  rnr_utils.load_Rangers_And_Ruffians_Data()
  face_shape = rnr_utils.GLOBAL_DESCRIPTIONS_DATABASE['face_shapes']
  gender = "male" if male else "female"
  
  return random.choice(face_shape[gender] + face_shape['unisex'])
  
def getFaceFeature(male):
  rnr_utils.load_Rangers_And_Ruffians_Data()
  face_features = rnr_utils.GLOBAL_DESCRIPTIONS_DATABASE['face_features']
  gender = "male" if male else "female"

  return random.choice(face_features[gender] + face_features['unisex'])

def getOrigins(race, rnr_class):
  rnr_utils.load_Rangers_And_Ruffians_Data()
  origins = rnr_utils.GLOBAL_DESCRIPTIONS_DATABASE['origins']
  return random.choice(origins)

def getWeakness(race, rnr_class):
  rnr_utils.load_Rangers_And_Ruffians_Data()
  weaknesses = rnr_utils.GLOBAL_DESCRIPTIONS_DATABASE['weaknesses']
  return random.choice(weaknesses)

def getName(race,male):
  rnr_utils.load_Rangers_And_Ruffians_Data()
  gender = "male" if male else "female"
  return names.get_first_name(gender=gender.lower())

def gender_word_replacement(string, gender):
  rnr_utils.load_Rangers_And_Ruffians_Data()
  my_gender_dict = rnr_utils.GLOBAL_DESCRIPTIONS_DATABASE["replacements"][gender]
  for term in my_gender_dict.keys():
    string = string.replace(term, my_gender_dict[term])
  return string

def getCharacterDescription(my_name,my_race,my_class,my_gender,flawed=True):
  rnr_utils.load_Rangers_And_Ruffians_Data()

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
  my_origins = getOrigins(my_race, my_class)
  my_weakness = getWeakness(my_race,my_class)
  my_unique_race_description = getUniqueRaceDescription(my_race)

  #origins
  ret = "{0} {1}. ".format(my_name, my_origins)
  #physical description
  ret += "<HE_SHE> {0},".format(my_physical_description)
  #hair
  if my_hair_description != None:
    if my_race.lower() != "catterwol":
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

  if flawed:
    ret += "{0} {1}.".format(my_name, my_weakness)

  if my_class.lower() == "beastmaster":
    my_animal_male = random.choice([True,False])
    my_animal_name = getName("animal",my_animal_male)
    animal_type = random.choice(["Wolf", "Dire Wolf", "Bear", "Hawk"])
    ret += "\n\n{0} has a companion {1} named {2}".format(my_name, animal_type, my_animal_name)

  return gender_word_replacement(ret, my_gender)
