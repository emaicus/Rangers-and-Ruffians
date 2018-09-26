import json
import sys
import os
import yaml
import traceback
import random
import argparse
import time
import names

import rnr_utils
import rnr_descriptions

weird_response = [
  "sexy ass",
  "sweet sweet",
  "glorious",
  "vivacious",
  "lovely",
  "dope",
  "damn fine"
]

manual_gender_selection = [
  "A badass <DUDE_DUDETTE> huh? Sounds like a plan!",
  "I can see <HIM_HER> now! Let's do this!",
  "Ah, alright, I can see what you're going for with <HIM_HER>. Let's keep the ball rolling!",
  "Oh! Oh! And what if <HE_SHE> was a famous mage who had a treacherous younger brother,\
  and was afraid to eat pickles!\nWait, I'm getting ahead of myself again! This is all you."
]

def get_physical_description(race, gender, bearded_override, name):
  face  = rnr_descriptions.getFace(gender, name) 
  hair  = rnr_descriptions.getHair(gender, name, race, bearded_override)
  eyes  = rnr_descriptions.getEyes(gender, name)
  body  = rnr_descriptions.getBody(gender, name, race)
 # quirk = rnr_descriptions.getQuirk(gender, name)

  print(face)
  print(hair)
  print(eyes)
  print(body)
  #print(quirk)

def random_choice(allowed_genders, allowed_races, allowed_classes, boring, beard_override=False):
  bad = True
  if boring:
    print("Enter yes or no.")
  else:
    print("Enter 'yes' for yes or literally anything else for no.") 
  while bad:
    random_gender = random.choice(allowed_genders)

    random_weakness = random.choice(rnr_descriptions.weaknesses)
    random_weakness = rnr_descriptions.gender_word_replacement(random_weakness, random_gender)

    random_origin = random.choice(rnr_descriptions.hometowns)
    random_origin = rnr_descriptions.gender_word_replacement(random_origin, random_gender)

    random_race = random.choice(allowed_races)
    random_class = random.choice(allowed_classes)

    if not boring:
      random_intro = random.choice(rnr_descriptions.introductions)
    else:
      random_intro = "Would you like to play as"

    name = names.get_first_name(gender=random_gender)

    print("Meet {0}.".format(name))
    print("{0} is a {1} {2}".format(name, random_race, random_class))
    get_physical_description(random_race, random_gender, beard_override, name)
    print("{0} {1}, and {2}".format(name, random_origin, random_weakness))

    response = input("do you want to play as {0}".format(name))
    #response = input("{0} a {1} {2} {3} who {4}, and who {5}?\n".format(random_intro, random_gender, random_race,random_class, random_origin, random_weakness))
    
    if response.strip() == "yes":
      bad = False
  return random_gender, random_race, random_class, random_origin, random_weakness

def manual_build(allowed_genders, allowed_races, allowed_classes, boring):
  if not boring:
    print("Alrighty then, sounds like you know what you want.")

  final_answer = ""
  while final_answer != "yes":
    gender = rnr_utils.answerQuestion("What gender do you want your character to be?", allowed_genders,"What gender do you want your character to be?",boring)
    my_gender_dict = gender_words[gender]

    gender_response = random.choice(manual_gender_selection)
    gender_response = gender_word_replacement(gender_response, gender)


    print(gender_response)
    print()
    race = rnr_utils.answerQuestion("What race are we looking at?", allowed_races, "What race do you want your character to be", boring)

    print("A {0}, huh? That's a solid choice.".format(race))
    print()
    c = rnr_utils.answerQuestion("How about your class?", allowed_classes, "What class do you want your character to be?",boring)

    final_answer = rnr_utils.answerQuestion("Alright, so you're looking at a {0} {1} {2}. Does that sound good?".format(gender, race, c), ["yes", "no"], "You have chosen a {0} {1} {2}.format(gender, race, c). Is that correct?", boring)
    print()
  return gender, race, c

def manual_backstory(gender, race, c, boring):
  if not boring:
    print("alright, now let's get some backstory for your character.")

  answer = rnr_utils.answerQuestionFancy("Do you want some help coming up with an origin for your character?", [["Do you think I'm a novice!", "no"], ["What have you got?", "yes"]], "Do you want help coming up with an origin for your character?", boring)
  my_gender_dict = gender_words[gender]
  if answer == "yes":
    satisfied = "no"
    while satisfied == "no":
      origin = random.choice(hometowns)
      origin = gender_word_replacement(origin, gender)
      satisfied = rnr_utils.answerQuestionFancy("Alright, what if your character {0}?".format(origin),[["Sounds perfect!", "yes"],["Nah, that ain't me!", "no"]], "How about {0}?".format(origin), boring)
  else:
    origin = input("Finish this sentence: My character is a {0} {1} {2} who ".format(gender, race, c))

  answer = rnr_utils.answerQuestionFancy("Alright, now it's time to give them a weakness. Want some help?", [["Do I look like a flippin' child to you!", "no"], ["Hell Yeah!", "yes"]], "Do you want help coming up with a weakness for your character?", boring)

  if answer == "yes":
    satisfied = "no"
    while satisfied == "no":
      weakness = random.choice(weaknesses)
      weakness = gender_word_replacement(weakness, gender)
      satisfied = rnr_utils.answerQuestionFancy("Alright, what if your character {0}?".format(weakness),[["Sounds par for the course.", "yes"],["I don't think so.", "no"]],"How about: {0}".format(weakness),boring)
  else:
    weakness = input("Finish this sentence: My character is a {0} {1} {2} who {3} and ".format(gender, race, c, origin))

  return origin, weakness

 

def main():

  # data_trove = 'feature_trainer.json'
  # all_combos = dict()
  # exit(1)


  parser = argparse.ArgumentParser(description='This utility will help you make an awesome rangers and ruffians character!',)
  parser.add_argument('--random', action="store_true", default=False, help="Start off making a random character!")
  parser.add_argument('--boring', action="store_true", default=False, help="Remove the program's soul!")
  parser.add_argument('--generate_name', action="store_true", default=False, help="Let the program generate character names for you!")
  parser.add_argument('--bearded', action="store_true", default=False, help="Your characters all have facial hair!")
  parser.add_argument('--train', action="store_true", default=False, help="Train the program!")

  args = parser.parse_args()
  boring = args.boring
  create_random = args.random
  random_names = args.generate_name

  allowed_races = rnr_utils.get_all_race_names()
  allowed_classes = rnr_utils.get_all_class_names()  
  allowed_genders = ["male", "female"]
  
  os.system("clear")
  rnr_utils.printLogo()

  if not create_random:
    answer = rnr_utils.answerQuestion("Would you like to create a character manually, or let the cold whims of entropy into your heart?", ["random", "manual"], "Would you like to create a character randomly or manually?", boring)
    if answer == "random":
      create_random = True

  if create_random and not args.random:
    answer = rnr_utils.answerQuestion("Alright, so you want a random character, huh. Are you going to be picky about it?", ["totally random", "remove options"], "Do you want a totally random character, or do you want to remove options?", boring)
    if answer == "remove options":
      keep = rnr_utils.answerQuestionFancy("Would you like your characters to be created with a specific gender?", [["Either is fine, I ain't no sexist!", "either"], ["Nah, I want male characters!", "male"], ["Hit me up with a female character, my man!", "female"]], "Do you have a character gender preference?", boring)
      if keep == 'male':
        allowed_genders.remove('female')
      elif keep == 'female':
        allowed_genders.remove('male')
      if rnr_utils.confirm("Would you like your characters to be created with a specific race?", ["I'm not racist, but...", "remove"], ["Any race is fine, I ain't no racist!", "any"], boring=boring):
        allowed_races   = rnr_utils.removeOptions(allowed_races)
      if rnr_utils.confirm("Would you like your characters to be created with a specific class?",  ["There are some classes I would rather not be!", "remove"], ["Class is an artificial construct created by the bourgeois!", "any"], boring=boring):
        allowed_classes = rnr_utils.removeOptions(allowed_classes)
  os.system("clear")
  os.system("clear")
  rnr_utils.printLogo()
  if create_random:
    random_gender, random_race, random_class, random_origin, random_weakness = random_choice(allowed_genders, allowed_races, allowed_classes, boring)
  else:
    random_gender, random_race, random_class = manual_build(allowed_genders, allowed_races, allowed_classes, boring)
    random_origin, random_weakness = manual_backstory(random_gender, random_race, random_class, boring)


  random_weird_response = random.choice(weird_response)

  if not boring:
    print("Sounds like a plan. I'm gonna write you up a stat sheet for this {0} {1} {2} {3}.\n".format(random_weird_response, random_gender, random_race,random_class))
  else:
    print("Generating stat sheet.")
  
  his_her = gender_words[random_gender]["<HIS_HER>"]

  name = input("What do you want {0} full name to be?\n".format(his_her))
  file_name = name.replace(' ', '_')

  character = rnr_utils.rnr_character(name, random_origin, random_weakness, rnr_utils.load_race(random_race), rnr_utils.load_class(random_class))
  character.pretty_print()

  # race = races[random_race]

  # print(json.dumps(race, indent=4))



  # with open("{0}.txt".format(file_name), 'w') as outfile:
  #   outfile.write("{0}: a {1} {2} {3} who {4}, and who {5}.\n".format(name, random_gender, random_race,random_class, random_origin, random_weakness))

  # print("I saved your character to {0}.txt".format(file_name))

if __name__ == "__main__":
    main()