import sys
import os
import traceback
import rnr_utils
import csv
import inquirer
import random
import math

def random_stats(race1, race2):
  stats1 = race1.stats
  stats2 = race2.stats 
  new_stats = dict()
  for key in rnr_utils.standard_stat_order():
    if random.choice([True, False]):
      print('{0}: {1} ({2})'.format(rnr_utils.abbreviate_stat(key), stats1[key], race1.subrace_name)) 
      new_stats[key] = stats1[key]  
    else:
      print('{0}: {1} ({2})'.format(rnr_utils.abbreviate_stat(key), stats2[key], race2.subrace_name)) 
      new_stats[key] = stats2[key]
  return new_stats

def avg_stats(race1, race2):
  stats1 = race1.stats
  stats2 = race2.stats 
  new_stats = dict()
  for key in rnr_utils.standard_stat_order():
    func = math.ceil if random.choice([True, False]) else math.floor
    new_stats[key] = func((stats1[key] + stats2[key]) / 2)
    print('{0}: {1}'.format(rnr_utils.abbreviate_stat(key), new_stats[key])) 
  return new_stats

def generate_split_race():
  all_races = rnr_utils.load_all_race_objects()
  subrace_names = rnr_utils.get_all_subrace_names()

  questions = [
    inquirer.List('race1',
                  message="What is the first race?",
                  choices=subrace_names,
              ),
    inquirer.List('race2',
                  message="And the second?",
                  choices=subrace_names,
              ),
  ]
  answers = inquirer.prompt(questions)

  subrace1 = answers["race1"]
  subrace2 = answers["race2"]

  race1 = rnr_utils.get_race_given_subrace(subrace1)
  race2 = rnr_utils.get_race_given_subrace(subrace2)

  race_obj1 = rnr_utils.rnr_race.basic_constructor(race1, subrace1)
  race_obj2 = rnr_utils.rnr_race.basic_constructor(race2, subrace2)
  
  print(subrace1)
  print(race_obj1)
  print(subrace2)
  print(race_obj2)

  name1 = 'random {0} {1}'.format(subrace1, subrace2)
  print(name1)
  stats1 = random_stats(race_obj1, race_obj2)
  print()
  name2 = 'average {0} {1}'.format(subrace1, subrace2)
  print(name2)
  stats2 = avg_stats(race_obj1, race_obj2)
  print()


 

if __name__ == '__main__':
  rnr_utils.printLogo()
  rnr_utils.load_Rangers_And_Ruffians_Data()
  while True:
    generate_split_race()