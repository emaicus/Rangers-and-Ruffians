import json
import sys
import os
import yaml
import traceback
import rnr_utils
from operator import attrgetter
import collections
import csv
import rnr_descriptions
from spellchecker import SpellChecker
import inquirer

STAT_OUTPUT = 'reports'

'''
Rank races and classes by their stats. call rank_races() and rank_classes()
'''
#Generate the race by race rankings.
def rank_races():
  races = rnr_utils.load_all_race_objects()
  if not os.path.exists(STAT_OUTPUT):
    os.mkdir(STAT_OUTPUT)

  with open(os.path.join(STAT_OUTPUT, 'race_rankings.txt'), 'w') as outfile:
    for stat in rnr_utils.get_all_stat_names():
      outfile.write("SORT BY: {0}\n".format(stat))
      races.sort(key = attrgetter(stat.lower()), reverse = True)
      for race in races:
        outfile.write("    {0}: {1}\n".format(race.name, race.get_stat(stat)))
      outfile.write("\n")

#Generate the race by race rankings.
def rank_classes():
  if not os.path.exists(STAT_OUTPUT):
    os.mkdir(STAT_OUTPUT)
  with open(os.path.join(STAT_OUTPUT, 'class_rankings.txt'), 'w') as outfile:

    level_zero  = rnr_utils.load_all_class_objects(level=0)
    level_five = rnr_utils.load_all_class_objects(level=5)
    level_ten  = rnr_utils.load_all_class_objects(level=10)
    
    for stat in rnr_utils.get_all_stat_names():
      outfile.write("SORT BY: {0}\n".format(stat))
      level_zero.sort(key = attrgetter(stat.lower()), reverse = True)
      level_five.sort(key = attrgetter(stat.lower()), reverse = True)
      level_ten.sort(key = attrgetter(stat.lower()), reverse = True)
      for level_classes, level_str in ((level_zero,'0'),):#(level_five,'5'),(level_ten,'10')):
        outfile.write('    LEVEL {0}:\n'.format(level_str))
        for rnr_class in level_classes:
          outfile.write("        {0}: {1}\n".format(rnr_class.name, rnr_class.get_stat(stat)))
      outfile.write('\n')

#load_combos_given_list
def rank_characters():
  #rank race vs all classes.
  rnr_classes = rnr_utils.get_all_class_names(underscore=False)
  rnr_races = rnr_utils.get_all_race_names(underscore=False)
  with open(os.path.join(STAT_OUTPUT, 'character_rankings.txt'), 'w') as outfile:
    for r_class in rnr_classes:
      outfile.write('{0}:\n'.format(r_class))
      for stat in rnr_utils.get_all_stat_names():
        outfile.write('  {0}:\n'.format(stat))
        characters = rnr_utils.load_combos_given_list(rnr_races, [r_class,], level=0)
        characters.sort(key = attrgetter(stat.lower()), reverse = True)
        for c in characters:
          outfile.write("    {0}: {1}\n".format(c.name, c.get_stat(stat)))
        outfile.write('\n')
      outfile.write('\n')
    outfile.write('NOW, IT GETS REAL!\n')
    characters = rnr_utils.load_all_characters(level=0)
    for stat in rnr_utils.get_all_stat_names():
      characters.sort(key = attrgetter(stat.lower()), reverse = True)
      outfile.write('{}\n'.format(stat))
      for c in characters:
        outfile.write("  {0}: {1}\n".format(c.name, c.get_stat(stat))) 
      outfile.write('\n')
    outfile.write('\n')

#load_combos_given_list
def dump_characters():
  #rank race vs all classes.
  with open(os.path.join(STAT_OUTPUT, 'all_characters.txt'), 'w') as outfile:
    characters = rnr_utils.load_all_characters()
    for c in characters:
      outfile.write('{0}\n'.format(c))
    outfile.write('\n')

def get_effective_vitality(vit):
  if vit <= 3:
    return vit
  else:
    real_vit = 3
    vit = vit-3
    return real_vit + (vit//2)

'''
Health binning and vitality chart. Call vitality_chart()
'''
def quick_health(level, vitality, tier, mode):
  tiers = {'light' : 4, 'medium' : 6, 'heavy' : 8}
  if mode == 'max':
    bonus = tiers[tier]
  elif mode == 'avg':
    bonus = tiers[tier] // 2
  else:
    bonus = 1


  summed_level = sum(range(level+1))
  modifier = get_effective_vitality(vitality) * (level + 1)
  return 10 + summed_level + modifier + (bonus*(level + 1))

def vitality_chart(data_packet):
  if not os.path.exists(STAT_OUTPUT):
    os.mkdir(STAT_OUTPUT)
  for mode in ['max', 'min', 'avg']:
    with open(os.path.join(STAT_OUTPUT, 'vitality_chart_{0}.txt'.format(mode)), 'w') as outfile:
      outfile.write('NOTE: Vitality is computed using a function housed in rnr_balance_reports which is decoupled from rnr_utils\n')
      outfile.write('{0:4}'.format('vit'))
      for tier in ['light', 'medium', 'heavy']:
        for i in range(11):
          outfile.write('{0:4}'.format(i))
        outfile.write('\n')

        for vitality in range(0,11):
          outfile.write('{0:4}'.format(vitality))
          for level in range(0,11):
            outfile.write('{0:4}'.format(quick_health(level, vitality, tier, mode)))
          outfile.write('\n')

        health_dict = dict()
        outfile.write('\n')

        for data in data_packet:
          for i in range(0,6):
            health_dict[i] = list()
          for obj in data:
            health_dict[obj.vitality].append(obj.name)
          for i in range(0,6):
            outfile.write('{0}: '.format(i))
            lis = health_dict[i]
            for name in lis:
              outfile.write(name + ', ')
            outfile.write('\n')
          outfile.write('\n')

'''
Spell output function. Call spell_stats()
'''
def spell_stats():
  wizard = rnr_utils.get_rnr_class_data_with_name('wizard')

  print('Assuming classes start with 2 spells, and wizard spell gaining cadence')
  print()
  print('-----------------------------------------')
  level_dict = {'Level Zero' : 2}
  can_learn_mask = {}
  for num in range(11):
    level_string = 'level_{0}'.format(num)
    if 'abilities' in wizard['levels'][level_string]:
      for ability in wizard['levels'][level_string]['abilities']:
        if 'Level' in ability and 'Spells' in ability:
          split = ability.split(' ')
          key = '{0} {1}'.format(split[0],split[1])
          if not key in can_learn_mask:
            can_learn_mask[key] = True
    for key, val in can_learn_mask.items():
      if val == True:
        if not key in level_dict:
          level_dict[key]= 0
        level_dict[key] += 1
    print(level_string)
    tot=0
    for key, val in level_dict.items():
      tot += val
      print('{0} {1} Spells'.format(val, key))
    print()
    print('TOTAL SPELLS: {0}'.format(tot))
    print('-----------------------------------------')

'''
Check for bad abilities. Call ability_check()
'''
def get_all_race_abilities_used():
  races = rnr_utils.load_all_race_objects()
  abilities = list()
  for race in races:
    abilities += race.abilities
  return abilities

def get_all_class_abilities_used():
  rnr_classes = rnr_utils.get_rnr_class_dict()
  abilities = list()
  for rnr_class, info in rnr_classes.items():
    abilities += info['base_abilities']
    for level, stats in info['levels'].items():
      for key, value in stats.items():
        if 'abilities' in key and not stats[key] is None:
          abilities += value
  return abilities 

def ability_check():
  rnr_utils.load_Rangers_And_Ruffians_Data()
  race_class_abilities = set(get_all_race_abilities_used() + get_all_class_abilities_used())
  all_abilities = set(rnr_utils.get_all_rnr_abilities().keys())

  print()
  non_existent = race_class_abilities - all_abilities
  if len(non_existent) > 0:
    print("The following abilities don't exist:")
    for ability in non_existent:
      print('    {0}'.format(ability))
  else:
    print("All abilities referenced by classes exist.")

  print()

  unused = all_abilities - race_class_abilities
  if len(unused) > 0:
    print("The following abilities aren't used:")
    for ability in unused:
      print('    {0}'.format(ability))
  else:
    print("All abilities are used.")
  print()
'''
Leveling details. Call process_classes(), level_details(level=0)
'''

def print_header(level, name, health, file_stream):
  file_stream.write('\n')
  file_stream.write('Level {0} {1}:\n'.format(level,name))
  file_stream.write('HP: {0}\n'.format(health))
  file_stream.write('\n')

def print_stats(stats, file_stream):
 
  file_stream.write("Stats:\n")
  for stat, value in stats.items():
    file_stream.write("    {0} {1}\n".format(stat, value))
  file_stream.write('\n')

def print_abilities(subclass, abilities, file_stream):
  if subclass:
    file_stream.write("{0} abilities\n".format(subclass))
  else:
    file_stream.write("Abilities:\n")
  for ability in abilities:
    file_stream.write('    {0}\n'.format(ability))
  file_stream.write('\n')

def process_classes():
  class_names = rnr_utils.get_all_class_names()
  if not os.path.exists(STAT_OUTPUT):
    os.mkdir(STAT_OUTPUT)
  if not os.path.exists(os.path.join(STAT_OUTPUT, 'level_output')):
    os.mkdir(os.path.join(STAT_OUTPUT, 'level_output'))

  for name in class_names:
    with open(os.path.join(STAT_OUTPUT, 'level_output','{0}.txt'.format(name)), 'w') as outfile:
      for level in range(0,11):
        subclasses = rnr_utils.subclasses_at_level(name, level)

        if len(subclasses) == 0:
          subclasses.add('')
                
        for subclass in subclasses:
          rnr_class_object = rnr_utils.rnr_class(name, level,subclass=subclass)
          print_header(level, name, rnr_class_object.get_health(), outfile)
          print_stats(rnr_class_object.stats, outfile)
          print_abilities(subclass, rnr_class_object.abilities, outfile)

def level_details(level=0):
  class_names = rnr_utils.get_all_class_names()
  if not os.path.exists(STAT_OUTPUT):
    os.path.mkdir(STAT_OUTPUT)
  if not os.path.exists(os.path.join(STAT_OUTPUT, 'level_output')):
    os.mkdir(os.path.join(STAT_OUTPUT, 'level_output'))
  
  with open(os.path.join(STAT_OUTPUT, 'level_output','level_{0}.txt'.format(level)), 'w') as outfile:
    for name in class_names:
      subclasses = rnr_utils.subclasses_at_level(name, level)

      if len(subclasses) == 0:
        subclasses.add('')
              
      for subclass in subclasses:
        rnr_class_object = rnr_utils.rnr_class(name, level,subclass=subclass)
        print_header(level, name, rnr_class_object.get_health(), outfile)
        print_stats(rnr_class_object.stats, outfile)
        print_abilities(subclass, rnr_class_object.abilities, outfile)   

'''
Game stats. call game_stats()
'''

def evaluate(num, target):
  if num < target:
    return 'FAIL! (-{0})'.format((target*2)-num)
  elif num >= target*2:
    return 'VICTORY! (+{0})'.format(num-(target*2))
  else:
    return 'PASS! (-{0})'.format((target*2)-num)

def game_stats():
  store_data = dict()
  process_classes()
  rnr_utils.load_Rangers_And_Ruffians_Data()

  all_races = rnr_utils.load_all_race_objects()
  all_classes = rnr_utils.load_all_class_objects_by_type()

  target_spell_counts = {'Level_0':11,'Level_1':10,'Level_2':8,'Level_3':6,'Level_4':4,'Level_5':2}

  #rnr_utils.printLogo()
  print('RANGERS AND RUFFIANS STAT TRACKER')
  print('R&R CONSISTS OF:')
  print('{0} Races'.format(len(all_races)))
  print('{0} Classes consisting of:'.format(len(rnr_utils.load_all_class_objects())))

  total = 0
  for class_type, classes in all_classes.items():
    total+= len(classes)
    print('    {0} {1} classes'.format(len(classes), class_type))
  print()

  ability_counts = {}
  total = 0
  for key, value in rnr_utils.get_all_rnr_abilities().items():
    ability_type = value['type']
    if not ability_type in ability_counts:
      ability_counts[ability_type] = list()
    ability_counts[ability_type].append(key)
    total+=1

  print('{0} Abilities consisting of:'.format(total))

  for key, lis in ability_counts.items():
    total+=len(lis)
    print('    {0} {1} abilities'.format(len(lis), key))
  print()
  
  total = 0
  all_spellbooks = rnr_utils.get_all_spellbooks()
  spell_counts = {}
  for spell_book, levels in all_spellbooks.items():
    print(spell_book)
    for level, spell_list in levels.items():
      num = len(spell_list)
      total += num
      if level in target_spell_counts:
        print('    {0} / {1} {2} spells: {3}'.format(num, target_spell_counts[level], level, evaluate(num, target_spell_counts[level])))
    print()
  print('TOTAL SPELLS: {0}'.format(total))

def check_brief_abilities():
  target_length = 80
  num_warnings = 0
  num_errors = 0
  for ability_name, ability_info in rnr_utils.get_all_rnr_abilities().items():
    if not 'brief' in ability_info:
      print('ERROR: No brief in {0}'.format(ability_name))
    if ability_info['type'] in ['rule', 'choice', 'starting_item', 'action']:
      continue
    if len(ability_info['brief']) > target_length:
      num_warnings+=1
      print("WARNING: {0}'s brief is {1} characters too long ({2} characters long)".format(ability_name, len(ability_info['brief']) - target_length, len(ability_info['brief']) ))
    if len(ability_info['brief']) > len(ability_info['description']):
      print("ERROR: {0}'s brief is longer than it's description!".format(ability_name))
      num_errors+=1
  print("\n{0} Warnings\n{1} Errors".format(num_warnings, num_errors))

def check_descriptions():
  for gender in ['male', 'female']:
    for outer, inner in rnr_utils.GLOBAL_DESCRIPTIONS_DATABASE.items():
      if isinstance(inner, str):
        tmp = rnr_descriptions.gender_word_replacement(inner, gender)
        if '<' in tmp or '>' in tmp:
          print('ERROR: {0}'.format(tmp))
      else:
        for inner_inner in inner:
          tmp = rnr_descriptions.gender_word_replacement(inner_inner, gender)
          if '<' in tmp or '>' in tmp:
            print('ERROR: {0}'.format(tmp))

def is_word_unknown(word, spell, new_words):
  return True if len(spell.unknown([word,])) == 1 and word not in new_words else False

def fix_spelling_errors(words, spell, rnr_dictionary, corrections):
  errors = 0
  for w in words:
    word = w.replace('.', '')
    word = word.replace(',', '')
    word = word.replace('!', '')
    word = word.replace('?', '')
    if is_word_unknown(word, spell, rnr_dictionary) and not word in corrections:
      correction = inquirer.prompt([inquirer.Text('correction', message='What is the proper spelling of {0} ({1})?'.format(word, spell.correction(word))),])['correction']
      if correction == '' or correction == 'word':
        rnr_dictionary.append(word)
      else:
        corrections[word] = correction   
    elif word in corrections:
      errors += 1
  return errors

def spell_check():
  spell = SpellChecker()
  rnr_dictionary = list()
  corrections = dict()
  ability_errors = 0
  spell_errors = 0

  if os.path.exists('rnr_dictionary.json'):
    with open('rnr_dictionary.json', 'r') as infile:
      data = json.load(infile)
      rnr_dictionary = data['rnr_words']
      corrections = data['corrections']

  ##############################################
  # ABILITIES
  ###############################################
  for ability_name, ability_info in rnr_utils.get_all_rnr_abilities().items():
    title_words = ability_name.split(' ')
    ability_errors += fix_spelling_errors(title_words, spell, rnr_dictionary, corrections)

    words = ability_info['description'].split(' ') + ability_info['brief'].split(' ')
    ability_errors += fix_spelling_errors(words, spell, rnr_dictionary, corrections)

  ##############################################
  # Spells
  ###############################################
  for spell_name, spell_info in rnr_utils.GLOBAL_COMPENDIUM_OF_SPELLS.items():
    title_words = spell_name.split(' ')
    spell_errors += fix_spelling_errors(title_words, spell, rnr_dictionary, corrections)

    words = spell_info['details']['description'].split(' ')
    spell_errors += fix_spelling_errors(words, spell, rnr_dictionary, corrections)

  output_json = {'corrections' : corrections, 'rnr_words' : rnr_dictionary}
  with open('rnr_dictionary.json', 'w') as outfile:
    json.dump(output_json, outfile, indent=4)

  if ability_errors > 0:
    print('ERROR: {0} spelling errors in abilities.yml'.format(ability_errors))
  if spell_errors > 0:
    print('ERROR: {0} spelling errors in spells.yml'.format(spell_errors))
  


if __name__ == '__main__':
  print('GENERATING SPELL STATS:')
  spell_stats()
  print()
  print('RUNNING ABILITY CHECK:')
  ability_check()
  print()
  print('GENERATING GAME STATS:')
  print()
  game_stats()
  print()
  print('GENERATING VITALITY CHARTS')
  vitality_chart((rnr_utils.load_all_race_objects(), rnr_utils.load_all_class_objects(level=5)))
  print('GENERATING LEVEL DETAILS FOR 0,5,10')
  level_details(level=0)
  level_details(level=5)
  level_details(level=10)
  print('GENERATING RACE RANKINGS')
  rank_races() 
  print("GENERATING CLASS RANKINGS")
  rank_classes()
  print("GENERATING CHARACTER RANKINGS")
  rank_characters()
  print("WRITING OUT ALL CHARACTERS FOR REVIEW")
  dump_characters()
  print()
  print("CHECKING ABILITY DESCRIPTION LENGTHS")
  print()
  check_brief_abilities()
  print()
  print('CHECKING DESCRIPTIONS')
  check_descriptions()
  print()
  print('RUNNING CUSTOM SPELL CHECK')
  spell_check()
  print()
  print("FINISHED!")
