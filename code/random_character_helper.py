import json
import sys
import os
import yaml
import traceback
import random
import argparse
import time

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
weaknesses = [
  "is afraid of the dark",
  "is very unsure of <HIMSELF_HERSELF>",
  "can't read or write",
  "hears voices is <HIS_HER> head",
  "steals anything that isn't bolted down",
  "guards <HIS_HER> food closely",
  "thinks that <HE_SHE> is the chosen one",
  "smiles all the time",
  "has a very creepy smile",
  "is physically aroused by pain",
  "falls in love really easily",
  "isn't afraid to cry",
  "holds in <HIS_HER> emotions",
  "can't hold in <HIS_HER> emotions",
  "likes animals more than people",
  "isn't afraid of anything",
  "is afraid of everything",
  "is socially awkward",
  "loves a good fight",
  "is a <MAN_WOMAN> of few words",
  "won't shut up",
  "has heavy scarring on <HIS_HER> face",
  "is covered in freckles",
  "carries the scar of an old wound",
  "is super attractive",
  "is very naive",
  "is relatively homely",
  "squeaks when <HE_SHE> laughs",
  "thinks in black and white",
  "likes to set fires",
  "can't swim well",
  "doesn't take discomfort well",
  "is always too cold",
  "has a cold personality",
  "gets angry easily",
  "is infinitely levelheaded",
  "has trouble sleeping and always has dark bags under <HIS_HER> eyes",
  "worries about everything",
  "suffers from depression",
  "giggles at everything",
  "desperately seeks approval",
  "is very smart, but doesn't know how to talk to people",
  "is very social around people, but is quiet and depressed when <HE_SHE> is alone",
  "is scared of fighting, but does it anyway",
  "doesn't like heights",
  "thinks <HE_SHE> is a total idiot",
  "can't ride a horse",
  "won't stop when <HE_SHE> has <HIS_HER> mind set on something",
  "likes to be fashionable",
  "recently broke up with <HIS_HER> longtime lover",
  "loves them and leaves them",
  "takes promises deadly serious",
  "hates the government",
  "always follows the rules",
  "is madly in love with a person <HE_SHE> barely met",
  "has a hyperinflated ego",
  "is terrified of animals",
  "performs best when others aren't watching",
  "will do anything for money",
  "speaks in the third person",
  "always believes the best of everyone",
  "always believes the worst of everyone",
  "is very clumsy",
  "is afraid of death",
  "feels woozy at the sight of blood",
  "is a showoff",
  "is built like a brick shithouse",
  "only weighs about eighty pounds"
]

hometowns = [
  "was raised in the wilds",
  "was raised in a castle",
  "was born in servitude",
  "was brought up as a student in an academy",
  "was brought up as a servant in an academy",
  "was 37 years old when <HIS_HER> <OPPOSITE_GENDER_WIFE_HUSBAND> died",
  "hates being away from <HIS_HER> <OPPOSITE_GENDER_WIFE_HUSBAND>",
  "married into a cult",
  "is the god of a small cult",
  "lost <HIS_HER> <OPPOSITE_GENDER_SON_DAUGHTER> to disease",
  "was stolen as a baby and raised by wizards",
  "was brought up by wolves",
  "was born into a circus",
  "was born to peasants",
  "served in the army",
  "spent some time as a bandit",
  "spent some time as a sailor",
  "apprenticed to a general",
  "owns a small shop",
  "lost <HIS_HER> home in a raid",
  "lost <HIS_HER> family in a fire",
  "lost <HIS_HER> <SAME_GENDER_MOTHER_FATHER> to a dragon",
  "has seen <HIS_HER> fair share of dungeons",
  "grew up working in a mine",
  "spent some time training to be a <SAME_GENDER_PRIEST_PRIESTESS>",
  "is of royal blood, but <HIS_HER> family was usurped",
  "is 7th in line to the throne",
  "is next in line to the throne",
  "adventured in <HIS_HER> youth",
  "retired some years ago",
  "spent <HIS_HER> youth as an adventurer",
  "was traumatized by abusive parents",
  "was raised by <HIS_HER> older <SAME_GENDER_BROTHER_SISTER>",
  "was raised by <HIS_HER> older <OPPOSITE_GENDER_BROTHER_SISTER>",
  "was raised by a blacksmith",
  "was raised by a bandit <SAME_GENDER_KING_QUEEN>",
  "was raised by a paladin",
  "was raised by a <SAME_GENDER_PRIEST_PRIESTESS>",
  "was raised by <HIS_HER> <SAME_GENDER_MOTHER_FATHER>, a <SAME_GENDER_LORD_LADY>",
  "was raised by a blacksmith",
  "was raised by a bandit <OPPOSITE_GENDER_KING_QUEEN>",
  "was raised by a paladin",
  "was raised by a <OPPOSITE_GENDER_PRIEST_PRIESTESS>",
  "was raised by <HIS_HER> <SAME_GENDER_MOTHER_FATHER>, a <OPPOSITE_GENDER_LORD_LADY>",
  "taught <HIMSELF_HERSELF> how to fight in the streets of a large city",
  "had no parents, so <HE_SHE> had to bring up <HIS_HER> little <SAME_GENDER_BROTHER_SISTER> in the streets",
  "had no parents, so <HE_SHE> had to bring up <HIS_HER> little <OPPOSITE_GENDER_BROTHER_SISTER> in the streets",
]

introductions = [
  "What about trying",
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

def random_choice(allowed_genders, allowed_races, allowed_classes, boring):
  bad = True
  if boring:
    print("Enter yes or no.")
  else:
    print("Enter 'yes' for yes or literally anything else for no.") 
  while bad:
    random_gender = random.choice(allowed_genders)
    my_gender_dict = gender_words[random_gender]

    random_weakness = random.choice(weaknesses)

    for term in my_gender_dict.keys():
      random_weakness = random_weakness.replace(term, my_gender_dict[term])

    random_origin = random.choice(hometowns)

    for term in my_gender_dict.keys():
      random_origin = random_origin.replace(term, my_gender_dict[term])

    random_race = random.choice(allowed_races)
    random_class = random.choice(allowed_classes)

    if not boring:
      random_intro = random.choice(introductions)
    else:
      random_intro = "Would you like to play as"

    response = input("{0} a {1} {2} {3} who {4}, and who {5}?\n".format(random_intro, random_gender, random_race,random_class, random_origin, random_weakness))
    
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

    for term in my_gender_dict.keys():
      gender_response = gender_response.replace(term, my_gender_dict[term])

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
      for term in my_gender_dict.keys():
        origin = origin.replace(term, my_gender_dict[term])
      satisfied = rnr_utils.answerQuestionFancy("Alright, what if your character {0}?".format(origin),[["Sounds perfect!", "yes"],["Nah, that ain't me!", "no"]], "How about {0}?".format(origin), boring)
  else:
    origin = input("Finish this sentence: My character is a {0} {1} {2} who ".format(gender, race, c))

  answer = rnr_utils.answerQuestionFancy("Alright, now it's time to give them a weakness. Want some help?", [["Do I look like a flippin' child to you!", "no"], ["Hell Yeah!", "yes"]], "Do you want help coming up with a weakness for your character?", boring)

  if answer == "yes":
    satisfied = "no"
    while satisfied == "no":
      weakness = random.choice(weaknesses)
      for term in my_gender_dict.keys():
        weakness = weakness.replace(term, my_gender_dict[term])
      satisfied = rnr_utils.answerQuestionFancy("Alright, what if your character {0}?".format(weakness),[["Sounds par for the course.", "yes"],["I don't think so.", "no"]],"How about: {0}".format(weakness),boring)
  else:
    weakness = input("Finish this sentence: My character is a {0} {1} {2} who {3} and ".format(gender, race, c, origin))

  return origin, weakness

 

def main():

  parser = argparse.ArgumentParser(description='This utility will help you make an awesome rangers and ruffians character!',)
  parser.add_argument('--random', action="store_true", default=False)
  parser.add_argument('--boring', action="store_true", default=False)
  args = parser.parse_args()
  boring = args.boring
  create_random = args.random
 
  allowed_races = rnr_utils.get_all_race_names()
  allowed_classes = rnr_utils.get_all_class_names()  
  allowed_genders = ["male", "female"]
  
  os.system("clear")
  rnr_utils.printLogo()

  if not create_random:
    answer = rnr_utils.answerQuestion("Would you like to create a character manually, or let the cold whims of entropy into your heart?", ["random", "manual"], "Would you like to create a character randomly or manually?", boring)
    if answer == "random":
      create_random = True

  if create_random:
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