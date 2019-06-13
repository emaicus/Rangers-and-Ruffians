import json
import sys
import os
import yaml
import traceback
import rnr_utils
from operator import attrgetter
import collections
import csv

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

    level_one  = rnr_utils.load_all_class_objects(level=1)
    level_five = rnr_utils.load_all_class_objects(level=5)
    level_ten  = rnr_utils.load_all_class_objects(level=10)
    
    for stat in rnr_utils.get_all_stat_names():
      outfile.write("SORT BY: {0}\n".format(stat))
      level_one.sort(key = attrgetter(stat.lower()), reverse = True)
      level_five.sort(key = attrgetter(stat.lower()), reverse = True)
      level_ten.sort(key = attrgetter(stat.lower()), reverse = True)
      for level_classes, level_str in ((level_one,'1'),(level_five,'5'),(level_ten,'10')):
        outfile.write('    LEVEL {0}:\n'.format(level_str))
        for rnr_class in level_classes:
          outfile.write("        {0}: {1}\n".format(rnr_class.name, rnr_class.get_stat(stat)))
      outfile.write('\n')

'''
Health binning and vitality chart. Call vitality_chart()
'''
def quick_health(level, vitality):
  extra = vitality // 2 if level == 0 else level*vitality
  return 15 + sum(range(level+1)) + extra

def vitality_chart(data_packet):
  if not os.path.exists(STAT_OUTPUT):
    os.mkdir(STAT_OUTPUT)
  with open(os.path.join(STAT_OUTPUT, 'vitality_chart.txt'), 'w') as outfile:
    outfile.write('NOTE: Vitality is computed using a function housed in rnr_balance_reports which is decoupled from rnr_utils\n')
    outfile.write('{0:4}'.format('vit'))
    for i in range(11):
      outfile.write('{0:4}'.format(i))
    outfile.write('\n')

    for vitality in range(0,11):
      outfile.write('{0:4}'.format(vitality))
      for level in range(0,11):
        outfile.write('{0:4}'.format(quick_health(level, vitality)))
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
  for ability_name, ability_info in rnr_utils.get_all_rnr_abilities().items():
    if not 'brief' in ability_info:
      print('ERROR: No brief in {0}'.format(ability_name))
  for ability_name, ability_info in rnr_utils.get_all_rnr_abilities().items():
    if len(ability_info['brief']) > 120:
      print("WARNING: {0}'s brief is {1} characters long".format(ability_name, len(ability_info['brief'])))
    if len(ability_info['brief']) > len(ability_info['description']):
      print("ERROR: {0}'s brief is longer than it's description!".format(ability_name))

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
  print()
  check_brief_abilities()
  print()
  print("FINISHED!")