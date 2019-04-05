import yaml
import math
import os
import json
from operator import attrgetter
import rnr_utils

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
  if not os.path.exists('level_output'):
    os.mkdir('level_output')

  for name in class_names:
    with open(os.path.join('level_output','{0}.txt'.format(name)), 'w') as outfile:
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
  if not os.path.exists('level_output'):
    os.mkdir('level_output')
  
  with open(os.path.join('level_output','level_{0}.txt'.format(level)), 'w') as outfile:
    for name in class_names:
      subclasses = rnr_utils.subclasses_at_level(name, level)

      if len(subclasses) == 0:
        subclasses.add('')
              
      for subclass in subclasses:
        rnr_class_object = rnr_utils.rnr_class(name, level,subclass=subclass)
        print_header(level, name, rnr_class_object.get_health(), outfile)
        print_stats(rnr_class_object.stats, outfile)
        print_abilities(subclass, rnr_class_object.abilities, outfile)   

# def level_stats(data):
#   print("Getting level stats")

#   all_classes = set()
#   is_best = set()
#   matched_worst = list()
#   matched_best = list()


#   with open(os.path.join('level_output','stats.txt'), 'w') as outfile:
#     for stat in ['Vitality', 'Luck', 'Dexterity', 'Strength', 'Perception', 'Charisma', 'Intelligence', 'Inner_Fire']:
#       outfile.write('\n{0}\n'.format(stat))
#       for level, classes in data.items():
#         outfile.write('\tLevel {0}\n'.format(level))
#         classes.sort(key = attrgetter(stat.lower()), reverse = True)
#         for rnr_class in classes:
#           all_classes.add(rnr_class.name)
#           outfile.write("\t\t{0}: {1}\n".format(rnr_class.name, rnr_class.get_stat(stat)))
#         matched_worst.append((classes[-1].name,level,stat))
#         matched_best.append((classes[0].name,level,stat))
#         if level == 10:
#           best_val = classes[0].get_stat(stat)
#           for tmp_c in classes:
#             if best_val == tmp_c.get_stat(stat):
#               is_best.add(tmp_c.name)
#     outfile.write('\n')
#     print('All classes:')
#     print(all_classes)
#     print('Best Classes')
#     print(is_best)
#     for rnr_class in all_classes - is_best:
#       outfile.write('{0} was never the best at anything.\n'.format(rnr_class))
#     outfile.write('\n')
#     for name, level, stat in matched_best:
#       outfile.write('Level {0}: {1} had the best {2}\n'.format(level, name, stat))
#     outfile.write('\n')
#     for name, level, stat in matched_worst:
#       outfile.write('Level {0}: {1} had the worst {2}\n'.format(level, name, stat))
#     outfile.write('\n')
#     outfile.write('Health Rankings:\n')
#     for level, classes in data.items():
#       outfile.write('\tLevel {0}\n'.format(level))
#       classes.sort(key = attrgetter('vitality'), reverse = True)
#       for rnr_class in classes:
#         health = get_health({"Vitality":rnr_class.get_stat('vitality')}, level)
#         outfile.write("\t\t{0}: {1}\n".format(rnr_class.name, health))
#     outfile.write('\n')

# #If subclass_name is None, we return a list containing all subclasses
# def make_class_at_level(class_name, class_data, target_level, subclass_name=None):
#   subclass_names = list()
#   subclasses = list()
#   if subclass_name == None:
#     subclass_names = subclasses_at_level(class_data, target_level)

#   if len(subclass_names) == 0:
#     subclass_names.add(class_name)

#   for subclass in subclass_names:
#     abilities = class_data['base_abilities']
#     stats = class_data['base_stats']     
#     for level in range(0,target_level+1):
#       level_string = 'level_{0}'.format(level)
#       level_details = class_data['levels'][level_string]
#       level_stats = level_details.get('stats', {})

#       stats = combine_stats(stats, level_stats)
#       abilities = abilities + level_details.get('abilities', [])
#       if 'subclass_{0}_abilities'.format(subclass) in level_details:
#         abilities = abilities + level_details['subclass_{0}_abilities'.format(subclass)]
#     subclasses.append(rnr_entity(subclass, stats, abilities))
#   return subclasses

# def load_classes_no_type():
#   classes = dict()
#   with open('leveled_classes.yml') as data_file:
#     rnr_classes = yaml.load(data_file)

#   for class_type, classes_of_type in rnr_classes.items():
#     classes.update(classes_of_type)
#   return classes

# #Makes all races in race_info and returns as a list.
# def load_race_objects(race_info):
#   races = list()

#   for race_name, race_data in race_info.items():
#     abilities = race_data['abilities']
#     stats = race_data['stats']     
#     races.append(rnr_entity(race_name, stats, abilities))
#   return races

def balance_report():
  print("Generating Balance Report")

  class_objects = rnr_utils.load_all_class_objects(10)
  race_objects = rnr_utils.load_all_race_objects()
  all_abilities = rnr_utils.ability_dict
  all_ability_names = set(all_abilities.keys())


  # with open(os.path.join('level_output','balance_report.txt'), 'w') as outfile:
  #   outfile.write('THE STATE OF THE GAME\n')

  all_used_abilities = set()
  for class_object in class_objects:
    all_used_abilities.update(class_object.abilities)

  for race_object in race_objects:
    all_used_abilities.update(race_object.abilities)

  print('The following abilities are unused:')
  for ability in all_ability_names:
    if not ability in all_used_abilities:
      print('\t{0}'.format(ability))

  print('The following abilities have no entry in abilities.yml:')
  for ability in all_used_abilities:
    if not ability in all_ability_names:
      print('\t{0}'.format(ability))

def evaluate(num, target):
  if num < target:
    return 'FAIL'
  elif num >= target*2:
    return 'VICTORY!'
  else:
    return 'GOOD'

def main():
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
    print('\t{0} {1} classes'.format(len(classes), class_type))
  print()

  ability_counts = {}
  total = 0
  for key, value in rnr_utils.ability_dict.items():
    ability_type = value['type']
    if not ability_type in ability_counts:
      ability_counts[ability_type] = list()
    ability_counts[ability_type].append(key)
    total+=1

  print('{0} Abilities consisting of:'.format(total))

  for key, lis in ability_counts.items():
    total+=len(lis)
    print('\t{0} {1} abilities'.format(len(lis), key))
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
        print('\t{0} / {1} {2} spells: {3}'.format(num, target_spell_counts[level], level, evaluate(num, target_spell_counts[level])))
    print()
  print('TOTAL SPELLS: {0}'.format(total))
  # print('{0} spells split across:'.format(total))
  # for spell_book, lis in spell_counts.items():
  #   num_spells = len(lis)
  #   print('\t{0} spells in {1}'.format(num_spells, spell_book))

  #level_stats(store_data)
  balance_report()
  level_details(0)
  level_details(10)
  print('All done!')
#309 + 210 519
if __name__ == '__main__':
  main()
