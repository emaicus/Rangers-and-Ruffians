import json
import sys
import os
import yaml
import traceback
from operator import attrgetter
import collections
import csv
from spellchecker import SpellChecker
import inquirer
import contractions
import string
import re
from pathlib import Path

from rangers_and_ruffians import core
#from rangers_and_ruffians import rnr_descriptions


STAT_OUTPUT = 'reports'

'''
Rank races and classes by their stats. call rank_races() and rank_classes()
'''
#Generate the race by race rankings.
def rank_races():
  races = core.load_all_race_objects()
  if not os.path.exists(STAT_OUTPUT):
    os.mkdir(STAT_OUTPUT)

  with open(os.path.join(STAT_OUTPUT, 'race_rankings.txt'), 'w') as outfile:
    for stat in core.get_all_stat_names():
      outfile.write("SORT BY: {0}\n".format(stat))
      #races.sort(key = attrgetter(stat.lower()), reverse = True)
      races.sort(key = lambda k:k.get_stat(stat.lower()), reverse=True)
      for race in races:
        outfile.write("    {0}: {1}\n".format(race.name, race.get_stat(stat)))
      outfile.write("\n")

#Generate the race by race rankings.
def rank_classes():
  if not os.path.exists(STAT_OUTPUT):
    os.mkdir(STAT_OUTPUT)
  with open(os.path.join(STAT_OUTPUT, 'class_rankings.txt'), 'w') as outfile:

    level_zero  = core.load_all_class_objects(level=0)
    level_five = core.load_all_class_objects(level=5)
    level_ten  = core.load_all_class_objects(level=10)
    level_fifteen  = core.load_all_class_objects(level=15)


    for stat in core.get_all_stat_names():
      outfile.write("SORT BY: {0}\n".format(stat))
      level_zero.sort(key = lambda k:k.get_stat(stat.lower()), reverse=True)
      level_five.sort(key = lambda k:k.get_stat(stat.lower()), reverse=True)
      level_ten.sort(key = lambda k:k.get_stat(stat.lower()), reverse=True)
      level_fifteen.sort(key = lambda k:k.get_stat(stat.lower()), reverse=True)
      for level_classes, level_str in ((level_zero,'0'),):#(level_five,'5'),(level_ten,'10')):
        outfile.write('    LEVEL {0}:\n'.format(level_str))
        for rnr_class in level_classes:
          outfile.write("        {0}: {1}\n".format(rnr_class.name, rnr_class.get_stat(stat)))
      outfile.write('\n')

#load_combos_given_list
def rank_characters():
  #rank race vs all classes.
  rnr_classes = core.get_all_class_names(underscore=False)
  rnr_races = core.get_all_race_names(underscore=False)
  with open(os.path.join(STAT_OUTPUT, 'character_rankings.txt'), 'w') as outfile:
    for r_class in rnr_classes:
      outfile.write('{0}:\n'.format(r_class))
      for stat in core.get_all_stat_names():
        outfile.write('  {0}:\n'.format(stat))
        characters = core.load_combos_given_list(rnr_races, [r_class,], level=0)
        characters.sort(key = lambda k:k.get_stat(stat.lower()), reverse=True)
        for c in characters:
          outfile.write("    {0}: {1}\n".format(c.name, c.get_stat(stat)))
        outfile.write('\n')
      outfile.write('\n')
    outfile.write('NOW, IT GETS REAL!\n')
    characters = core.load_all_characters(level=0)
    for stat in core.get_all_stat_names():
      characters.sort(key = lambda k:k.get_stat(stat.lower()), reverse=True)
      outfile.write('{}\n'.format(stat))
      for c in characters:
        outfile.write("  {0}: {1}\n".format(c.name, c.get_stat(stat)))
      outfile.write('\n')
    outfile.write('\n')

#load_combos_given_list
def dump_characters():
  #rank race vs all classes.
  with open(os.path.join(STAT_OUTPUT, 'all_characters.txt'), 'w') as outfile:
    characters = core.load_all_characters()
    for c in characters:
      outfile.write('{0}\n'.format(c))
    outfile.write('\n')

'''
Health binning and vitality chart. Call vitality_chart()
'''
def quick_health(old_health, new_level, health_dice, mode):
  if mode == 'max':
    bonus = health_dice
  elif mode == 'avg':
    bonus = health_dice // 2
  elif mode == 'min':
    bonus = 1
  elif mode == 'rand':
    bonus = core.roll_dice(sides=health_dice)
  elif mode == 'adv':
    bonus = core.roll_dice(sides=health_dice, advantage=True)
  elif mode == 'round to half':
    bonus = max(core.roll_dice(sides=health_dice), health_dice//2)

  if new_level == 0:
    bonus = health_dice

  return old_health + bonus + new_level

def vitality_chart(data_packet):
  if not os.path.exists(STAT_OUTPUT):
    os.mkdir(STAT_OUTPUT)
  with open(os.path.join(STAT_OUTPUT, 'vitality_chart.txt'), 'w') as outfile:
    outfile.write('NOTE: Vitality is computed using a function housed in rnr_balance_reports which is decoupled from rangers_and_ruffians.core.\nHEALTH COMPUTATIONS COULD BE INACCURATE\n')
    outfile.write('\n')
    for mode in ['max', 'min', 'avg', 'rand', 'adv', 'round to half']:
      outfile.write('\n')
      outfile.write('{0}\n'.format(mode.upper()))

      outfile.write('{0:<4}'.format('DIE'))
      for i in range(0,16):
        s = 'LV{0}'.format(i)
        outfile.write('{0:<5}'.format(s))
      outfile.write('\n')

      for health_die in [4, 6, 8, 10, 12]:
        outfile.write('{0:<4}'.format(health_die))
        health = health_die
        for level in range(0,16):
          health = quick_health(health, level, health_die, mode)
          outfile.write('{0:<5}'.format(health))
        outfile.write('\n')


        # for data in data_packet:
        #   for i in range(0,6):
        #     health_dict[i] = list()
        #   for obj in data:
        #     health_dict[obj.vitality].append(obj.name)
        #   for i in range(0,6):
        #     outfile.write('{0}: '.format(i))
        #     lis = health_dict[i]
        #     for name in lis:
        #       outfile.write(name + ', ')
        #     outfile.write('\n')
        #   outfile.write('\n')

    outfile.write('\n')
    all_characters = core.load_all_characters()
    health_dice_dict = dict()
    for c in all_characters:
      h_d = c.health_dice
      if not h_d in health_dice_dict:
        health_dice_dict[h_d] = list()
      health_dice_dict[h_d].append(c)
    for i in range(20):
      if i in health_dice_dict:
        outfile.write('{0}: '.format(i))
        for item in health_dice_dict[i]:
          outfile.write('{0}, '.format(item.name))
        outfile.write('\n')


'''
Spell output function. Call spell_stats()
'''
def spell_stats():
  wizard = core.get_subclass_data_with_name('Wizard')
  print(json.dumps(wizard, indent=4))

  print('Assuming classes start with 2 spells, and wizard spell gaining cadence')
  print()
  print('-----------------------------------------')
  level_dict = {'Level Zero' : 2}
  can_learn_mask = {}
  for num in range(16):
    level_string = 'level_{0}'.format(num)
    if not level_string in wizard['levels']:
      continue
    if 'abilities' in wizard['levels'][level_string] and wizard['levels'][level_string]["abilities"] is not None and len(wizard['levels'][level_string]["abilities"]) >= 1:
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
  races = core.load_all_race_objects()
  abilities = list()
  for race in races:
    abilities += race.abilities
  return abilities

def get_all_class_abilities_used():
  rnr_classes = core.get_rnr_class_dict()
  abilities = list()
  for rnr_class, info in rnr_classes.items():
    for subclass, subclass_info in info["subclasses"].items():
      abilities += subclass_info.get('base_abilities', list())
      for level, stats in subclass_info['levels'].items():
        for key, value in stats.items():
          if 'abilities' in key and not stats[key] is None:
            abilities += value
  return abilities

def get_non_existent_abilities():
  race_class_abilities = set(get_all_race_abilities_used() + get_all_class_abilities_used())
  all_abilities = set(core.get_all_rnr_abilities().keys())
  return race_class_abilities - all_abilities

def get_unused_abilities():
  race_class_abilities = set(get_all_race_abilities_used() + get_all_class_abilities_used())
  all_abilities = set(core.get_all_rnr_abilities().keys())
  return all_abilities - race_class_abilities

def ability_check():
  core.load_Rangers_And_Ruffians_Data()
  print()

  non_existent = get_non_existent_abilities()
  if len(non_existent) > 0:
    print("The following abilities don't exist:")
    for ability in non_existent:
      print('    {0}'.format(ability))
  else:
    print("All abilities referenced by classes exist.")
  print()

  unused = get_unused_abilities()
  if len(unused) > 0:
    print("The following abilities aren't used:")
    for ability in unused:
      print('    {0}'.format(ability))
  else:
    print("All abilities are used.")
  print()

def print_header(level, name, file_stream):
  file_stream.write('\n')
  file_stream.write('Level {0} {1}:\n'.format(level,name))
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


'''
Game stats. call game_stats()
'''

def evaluate(num, target):
  if num < target:
    return 'FAIL!'.format((target*2)-num)
  elif num >= target*2:
    return 'VICTORY!'.format(num-(target*2))
  else:
    return 'PASS!'.format((target*2)-num)

def game_stats():
  store_data = dict()
  core.load_Rangers_And_Ruffians_Data()

  all_races = core.load_all_race_objects()

  target_spell_counts = {'Level_0':11,'Level_1':10,'Level_2':8,'Level_3':6,'Level_4':4,'Level_5':2}

  #core.printLogo()
  print('RANGERS AND RUFFIANS STAT TRACKER')
  print('R&R CONSISTS OF:')
  print('{0} Races'.format(len(all_races)))
  print('{0} Classes consisting of:'.format(len(core.load_all_class_objects())))

  ability_counts = {}
  total = 0
  for key, value in core.get_all_rnr_abilities().items():
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
  all_spellbooks = core.get_all_spellbooks()
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

def evaluate_spells_for_failures(print_errors=True):
  core.load_Rangers_And_Ruffians_Data()
  all_spellbooks = core.get_all_spellbooks()
  # Get new spell tier at levels 0, 1, 5, 8, 11, 14
  target_spell_counts = {'Tier_0':16,'Tier_1':15,'Tier_2':10,'Tier_3':8,'Tier_4':5,'Tier_5':2}
  offenders = list()
  for spell_book, levels in all_spellbooks.items():
    # These spell books won't pass anytime soon and are augmented by the novice spellbook.
    if spell_book in ["the_sorcerer's_scrolls", "the_wizard's_addendum"]:
      continue
    for level, spell_list in levels.items():
      num = len(spell_list)
      if level in target_spell_counts:
        if evaluate(num, target_spell_counts[level]) == "FAIL!":
          offenders.append('{0} {2} needs {1}'.format(spell_book, target_spell_counts[level] - num, level))
  if print_errors:
    for error in offenders:
      print(error)
  return offenders

def evaluate_spells_for_doubling(print_errors=True):
  core.load_Rangers_And_Ruffians_Data()
  all_spellbooks = core.get_all_spellbooks()
  target_spell_counts = {'Tier_0':16,'Tier_1':15,'Tier_2':10,'Tier_3':8,'Tier_4':5,'Tier_5':2}
  offenders = list()
  running_total = 0
  for spell_book, levels in all_spellbooks.items():
    for level, spell_list in levels.items():
      num = len(spell_list)
      if level in target_spell_counts:
        if "VICTORY!" not in evaluate(num, target_spell_counts[level]):
          offenders.append('{0} {2} needs {1}'.format(spell_book, (target_spell_counts[level]*2) - num, level))
          running_total += (target_spell_counts[level]*2) - num
  if running_total > 0:
    offenders.append("We need {0} total spells".format(running_total))
  if print_errors:
    for error in offenders:
      print(error)
  return offenders

def check_brief_abilities(print_errors=True):
  target_length = 100
  errors = list()
  for ability_name, ability_info in core.get_all_rnr_abilities().items():
    if not 'type' in ability_info:
      errors.append(f'ERROR: No type in {ability_name}')

    if not 'brief' in ability_info:
      errors.append(f'ERROR: No brief in {ability_name}')
    else:
      if len(ability_info['brief']) > target_length:
        errors.append(f"WARNING: {ability_name}'s brief is {len(ability_info['brief']) - target_length} characters too long ({len(ability_info['brief'])} characters long)")
      if len(ability_info['brief']) > len(ability_info['description']):
        success = False
        errors.append(f"ERROR: {ability_name}'s brief is longer than it's description!")
  if print_errors:
    for error in errors:
      print(error)
  return errors

def check_ability_types(print_errors=True):
  errors = list()
  for ability_name, ability_info in core.get_all_rnr_abilities().items():
    if not 'type' in ability_info:
      errors.append(f'ERROR: No type in {ability_name}')
      continue
    if not ability_info['type'] in ["starting_item", "general", "combat", "general", "advantage", "disadvantage", "choice", "spellbook", "rule", "action"]:
      errors.append(f'{ability_name} has unexpected ability type: {ability_info["type"]}')
  if print_errors:
    for error in errors:
      print(error)
  return errors

# def check_descriptions(print_errors=True):
#   errors = list()
#   for gender in ['male', 'female']:
#     for outer, inner in core.GLOBAL_DESCRIPTIONS_DATABASE.items():
#       if isinstance(inner, str):
#         tmp = rnr_descriptions.gender_word_replacement(inner, gender)
#         if '<' in tmp or '>' in tmp:
#           errors.append('ERROR: {0}'.format(tmp))
#       else:
#         for inner_inner in inner:
#           tmp = rnr_descriptions.gender_word_replacement(inner_inner, gender)
#           if '<' in tmp or '>' in tmp:
#             errors.append('ERROR: {0}'.format(tmp))
#   if print_errors:
#     for error in errors:
#       print(error)
#   return errors

def type_check(dictionary, key, t, error, required=False):
  errors = list()
  if key in dictionary:
    if not isinstance(dictionary[key], t):
      errors.append(f'{error}: {key} is not the correct type, expected is a(n) {type(dictionary[key]).__name__}.')
  elif required:
    errors.append(f'{error}: {key} is missing.')
  return errors

def check_weapons(print_errors=True):
  errors = list()
  for weapon_type, weapon_type_data in core.GLOBAL_STANDARD_ITEMS['weapons'].items():
    for weapon, details in weapon_type_data.items():
      errors += type_check(details, 'cost', str, weapon, True)
      errors += type_check(details, 'minimum_damage_dice', int, weapon, True)
      errors += type_check(details, 'maximum_damage_dice', int, weapon, True)
      errors += type_check(details, 'range', str, weapon, True)
      errors += type_check(details, 'movement_penalty', int, weapon, True)
      errors += type_check(details, 'abilities', dict, weapon, False)
      errors += type_check(details, 'drawbacks', dict, weapon, False)

      known_keys = ['cost', 'minimum_damage_dice', 'maximum_damage_dice', 'range', 'movement_penalty', 'abilities', 'drawbacks']
      for key in details.keys():
        if key not in known_keys:
          errors.append(f"{weapon}: unexpected key {key}")


      if 'abilities' in details:
        for key, val in details['abilities'].items():
          errors += type_check(details['abilities'], key, str, f'{weapon} abilities, {key}', True)

      if 'drawbacks' in details:
        for key, val in details['drawbacks'].items():
          errors += type_check(details['drawbacks'], key, str, f'{weapon} drawbacks, {key}', True)

  if print_errors:
    for error in errors:
      print(error)
  return errors

def is_word_unknown(word, spell, new_words):
  if len(spell.unknown([word,])) == 1 and word not in new_words:
    return True
  else:
    return False

def split_words_on(words, c):
  ret = list()
  for word in words:
    ret += word.split(c)
  return ret

def process_word(word):
  words = contractions.fix(word).split()
  words = split_words_on(words, '/')
  words = split_words_on(words, '-')
  words = split_words_on(words, '_')

  ret = list()
  for word in words:
    if re.findall("\\d*d\\d+", word) or re.findall("\\d+x\\d+x?\\d*", word):
      continue
    if word.endswith("'s"):
      word = word[:-2]
    translator = str.maketrans('', '', string.punctuation.replace('-', ''))
    word = word.translate(translator)
    ret.append(word)
  return ret

def fix_spelling_errors(words, spell, rnr_dictionary):
  errors = set()
  for word in words:
    w = process_word(word)
    for element in w:
      if element == '':
        continue
      if is_word_unknown(element, spell, rnr_dictionary) and not element in errors:
        correct = inquirer.prompt([inquirer.Confirm('correct', message=f'Is {element} properly spelled? (originally {word})'),])['correct']
        print("yes" if correct else "error")
        if correct == True:
          rnr_dictionary.add(element)
        else:
          errors.add(element)
  return errors

def just_find_typos(words, spell, rnr_dictionary):
  errors = set()
  for word in words:
    w = process_word(word)
    for element in w:
      if element == '':
        continue
      if is_word_unknown(element, spell, rnr_dictionary):
        errors.add(element)
  return errors

def spell_check_a_file(filename, spell_check_function, spell, rnr_dictionary):
  with open(filename, 'r') as infile:
    lines = infile.readlines()

  words = set()
  for line in lines:
    words_in_line = line.split()
    for word in words_in_line:
      words.add(word.lower())

  return spell_check_function(list(words), spell, rnr_dictionary)

def spell_check(fix_errors=True, print_errors=True):

  if fix_errors == True:
    spell_check_function = fix_spelling_errors
  else:
    spell_check_function = just_find_typos

  spell = SpellChecker()
  rnr_dictionary = list()
  ability_errors = set()
  spell_errors = set()

  dictionary_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'rnr_dictionary.json')
  if os.path.exists(dictionary_path):
    with open(dictionary_path, 'r') as infile:
      data = json.load(infile)
      rnr_dictionary = set(data['rnr_words']) if 'rnr_words' in data else set()


  directories_to_check = [
                           Path(os.path.join(core.BASE_DIRECTORY, 'data')),
                           Path(os.path.join(core.BASE_DIRECTORY, 'docs')),
                         ]

  directories_to_skip = [
    os.path.join(core.BASE_DIRECTORY, "data", "wip"),
    os.path.join(core.BASE_DIRECTORY, "data", "legacy"),
    os.path.join(core.BASE_DIRECTORY, "data", "scratch.txt"),
    os.path.join(core.BASE_DIRECTORY, "data", "art.yml"),
    os.path.join(core.BASE_DIRECTORY, "data", "description_database.yml"),
    os.path.join(core.BASE_DIRECTORY, "data", "helper_scripts"),
  ]
  testable_extensions = ['.txt', '.yml', '.json', '.md']

  all_errors = dict()
  all_errors["turtle"] = list()
  for directory in directories_to_check:
    for extension in testable_extensions:
      for file in directory.glob(f'**/*{extension}'):
        skip = False
        for skip_dir in directories_to_skip:
          if str(file).startswith(skip_dir):
            skip = True
            break
        if not skip:
          all_errors[file] = spell_check_a_file(str(file), spell_check_function, spell, rnr_dictionary)

  # if len(spell_errors) > 0:
  #   all_errors["spellbooks"] = list(spell_errors)
  # if len(ability_errors) > 0:
  #   all_errors["abilities"] = list(ability_errors)



  # ##############################################
  # # ABILITIES
  # ###############################################
  # for ability_name, ability_info in core.get_all_rnr_abilities().items():
  #   title_words = ability_name.split(' ')
  #   spell_check_function(title_words, spell, rnr_dictionary, ability_errors)

  #   words = ability_info['description'].split(' ') + ability_info['brief'].split(' ')
  #   spell_check_function(words, spell, rnr_dictionary, ability_errors)

  # ##############################################
  # # Spells
  # ###############################################
  # for spell_name, spell_info in core.GLOBAL_COMPENDIUM_OF_SPELLS.items():
  #   title_words = spell_name.split(' ')
  #   spell_errors.update(spell_check_function(title_words, spell, rnr_dictionary, spell_errors))

  #   words = spell_info['details']['description'].split(' ')
  #   spell_check_function(words, spell, rnr_dictionary, spell_errors)


  if fix_errors:
    output_json = {'rnr_words' : list(rnr_dictionary)}
    with open('rnr_dictionary.json', 'w') as outfile:
      json.dump(output_json, outfile, indent=4)

  if print_errors:
    for file, errors in all_errors.items():
      print("The following values are misspelled in {0}".format(file))
      for error in errors:
        print("  {0}".format(error))

  return all_errors

# Returns a list of errors found in a description.
def string_key_check(dictionary, key, err_name, required=True, punctuation_check=True):
  errors = list()
  if key in dictionary:
    if not isinstance(dictionary[key], str):
      errors.append(f'{err_name}: {key} is not a string.')
    else:
      if not dictionary[key][-1] in ['.', '!'] and punctuation_check:
        errors.append(f'{err_name}: {key} should end in punctuation.')
  elif required:
    errors.append(f'{err_name}: does not have {key}.')

  return errors

def check_known_beasts():
  all_errors = list()
  for category, category_info in core.GLOBAL_BOOK_OF_KNOWN_BEATS.items():

    # all_errors += string_key_check(category_info, 'description', category)
    # all_errors += string_key_check(category_info, 'tactics', category)

    if not 'types' in category_info:
      all_errors.append(f'{category}: no types defined.')
      continue

    for beast_class, beasts in category_info['types'].items():
      all_errors += string_key_check(beasts, 'description', beast_class)
      all_errors += string_key_check(beasts, 'tactics', beast_class)

      if not 'types' in beasts:
        all_errors.append(f'{beast_class}: no types defined.')
        continue

      for beast, info in beasts['types'].items():
        is_villain = False
        if 'type' not in info:
          all_errors.append(f'{beast} missing type.')
        else:
          try:
            level_str, num, size = info['type'].split(' ')
            if level_str != 'Level' or int(num) < 0 or int(num) > 15 or size not in ['Light', 'Heavy', 'Villain']:
              all_errors.append(f'{beast}: malformed type')
            else:
              if size == 'Villain':
                is_villain = True
          except Exception as e:
            all_errors.append(f'{beast}: (exception) malformed type')

        all_errors += string_key_check(beast, 'description', info, required=False)
        all_errors += string_key_check(beast, 'tactics', beast, required=is_villain)

        for k in ['average_damage_per_round', 'average_villain_damage_per_round']:
          if k in info:
            if not isinstance(info[k], int):
              all_errors.append(f'{beast}: {k} ADPR is not an int')
            if not is_villain and k == 'average_villain_damage_per_round':
              all_errors.append(f'{beast}: has Villain ADPR despite not being a villain.')
          elif is_villain and k == 'average_villain_damage_per_round':
            all_errors.append(f'{beast}: is a villain but does not have a Villain ADPR.')
          elif k == 'average_damage_per_round':
            all_errors.append(f'{beast} is missing {k}.')

        if not 'health' in info:
          all_errors.append(f'{beast}: missing health')
        else:
          try:
            h = int(info['health'])
            if h <= 0:
              all_errors.append(f'{beast}: bad value for health')
          except Exception as e:
            all_errors.append(f'{beast}: malformed health')

        if 'action_spec' in info:
          for key, val in info['action_spec'].items():
            if not isinstance(val, str):
              all_errors.append(f'{beast} action_spec {key}: description should be a string')
            else:
              if not val[-1] in ['.', '!']:
                all_errors.append(f'{beast} action_spec {key}: description should end in punctuation.')


        if not 'actions' in info:
          all_errors.append(f'{beast}: does not have actions')
        else:
          for action, a_info in info['actions'].items():
            if 'damage' in a_info:
              if not 'modifier' in a_info:
                all_errors.append(f'{beast} {action}: missing modifier')
              else:
                if not isinstance(a_info['modifier'], str):
                  all_errors.append(f'{beast} {action}: modifier should be a string')
                else:
                  if not a_info['modifier'] in ["Strength", "Dexterity", "Inner_Fire"]:
                    all_errors.append(f'{beast} {action}: bad modifier {a_info["modifier"]}')
              try:
                n, d = a_info['damage'].split('d')
                n_i = int(n)
                d_i = int(d)
                if n_i <= 0 or d_i not in [2, 4, 6, 8, 10, 12, 20, 100]:
                  all_errors.append(f'{beast} {action}: bad damage {a_info["damage"]}')
              except Exception as e:
                all_errors.append(f'{beast} {action}: (exception) bad damage {a_info["damage"]}')

            if not 'description' in a_info:
              all_errors.append(f'{beast} {action}: no description')
            else:
              if a_info['description'][-1] not in ['.', '!']:
                all_errors.append(f'{beast} {action}: description does not end with punctuation.')

            if 'modifier' in a_info and 'damage' not in a_info:
              all_errors.append(f'{beast} {action}: has modifier but no damage')


        if 'abilities' in info:
          for ability, description in info['abilities'].items():
            if not isinstance(description, str):
              all_errors.append(f'{beast} {ability} does not have a string description.')
            else:
              if description[-1] not in ['.', '!']:
                all_errors.append(f'{beast} {ability}: description does not end with punctuation.')

        if not 'movement' in info:
          all_errors.append(f'{beast}: does not have movement')
        else:
          if not isinstance(info['movement'], dict):
            all_errors.append(f'{beast}: movement should be a dict of terrain to speed')
          else:
            for m_type, m_dist in info['movement'].items():
              if not m_type in ['land', 'water', 'air']:
                all_errors.append(f'{beast}: movement has unsupported type {m_type}')
              if not isinstance(m_dist, int):
                all_errors.append(f'{beast}: {m_type} movement is not an integer')

        if not 'stats' in info:
          all_errors.append(f'{beast}: does not have stats')
        else:
          for stat, val in info['stats'].items():
            if not stat in core.get_all_stat_names():
              all_errors.append(f'{beast}: bad stat name {stat}')
            if not isinstance(val, int):
              all_errors.append(f'{beast}: bad {stat} value {val}')

        for key in ['conditional_actions', 'sanctuary_actions', 'villain_actions', 'offhand_actions']:
          if key in info:
            for action_type, a_description in info[key].items():
              if not isinstance(a_description, str):
                all_errors.append(f'{beast} {key} {action_type}: description is not a string')
              else:
                if a_description[-1] not in ['.', '!']:
                  all_errors.append(f'{beast} {key} {action_type}: description does not end with punctuation.')

  return all_errors

def check_pantheon():
  all_errors = list()
  for deity, info in core.GLOBAL_PANTHEON.items():
    if 'evil' in info:
      if not isinstance(info['evil'], bool):
        all_errors.append(f'{deity}: evil is not a boolean')
    else:
      all_errors.append(f'{diety}: missing evil value')

    all_errors += string_key_check(info, "description", deity)

    if 'abilities' in info:
      for level, abilities in info['abilities'].items():
        try:
          level_str, level_num = level.split('_')
          level_num = int(level_num)
          if not level_str == 'level' or level_num > 15 or level_num < 0:
            all_errors.append(f'{deity}: bad level {level}')
        except Exception as e:
          all_errors.append(f'{deity}: bad level (exception) {level}')

        for ability in abilities:
          if not isinstance(ability, str):
            all_errors.append(f'{deity} {ability}: not a string')
    elif deity.strip().lower() != 'the shaper':
      all_errors.append(f"{deity}: missing abilities.")

  return all_errors



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
  vitality_chart((core.load_all_race_objects(), core.load_all_class_objects(level=5)))
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
  # print('CHECKING DESCRIPTIONS')
  # check_descriptions()
  # print()
  # print('RUNNING CUSTOM SPELL CHECK')
  # spell_check()
  # print()
  print("FINISHED!")
