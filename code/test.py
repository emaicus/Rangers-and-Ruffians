import rnr_utils
import json

def sum_vals(d):
  s = 0
  for key, val in d.items():
    s += val
  return s

def choice_mod(d):
  s=0
  if 'Choice Stat' in d:
    s += 1
  elif 'Greater Choice Stat' in d:
    s += 2
  elif 'Choice of Model' in d:
    s += 2
  return s

def find_ability_costs(abilities):
  cost = 0
  for ability in abilities:
    ab = rnr_utils.GLOBAL_ABILITY_DICT[ability]
    if ab.get('cost', 0) > cost:
      cost = ab.get('cost', 0)
  return cost

if __name__ == '__main__':
  actual_offset = dict()
  rnr_utils.printLogo()
  rnr_utils.load_Rangers_And_Ruffians_Data()
  space = '  '
  two_space = '{0}{1}'.format(space, space)
  zero_stats = list()
  off_neutral_list = list()
  most_negative = (5,'','')
  most_positive = (-5,'','')
  ability_costs = dict()
  for class_name, class_details in rnr_utils.GLOBAL_CLASS_DATA.items():
    print("{0}".format(class_name))
    print('{0}stats:'.format(space))

    for stat, stat_val in class_details['base_stats'].items():
      if stat != 'Vitality' and not (class_name == 'Cleric' and stat == 'Strength'):
        if stat_val < most_negative[0]:
          most_negative = (stat_val, stat, class_name)
        if stat_val > most_positive[0]:
          most_positive = (stat_val, stat, class_name)

    off_neutral = sum_vals(class_details['base_stats']) + choice_mod(class_details['base_abilities'])
    off_neutral_list.append(('{0:12} {1:2d}'.format(class_name+':', off_neutral), off_neutral))

    cost = find_ability_costs(class_details.get('base_abilities', list()))
    if cost > 0:
      ability_costs[class_name] = 'At {0} {1} has an ability of cost {2}'.format(level, class_name, cost)

    # print('{0}{1} OFF NEUTRAL'.format(two_space, off_neutral))
    level_up_tokens = 0
    for level, level_info in class_details['levels'].items():
      this_level_tokens = sum_vals(level_info.get('stats', {})) + choice_mod(level_info.get('abilities', list()))
      off_neutral += this_level_tokens
      print('{0}{1:8}: {2:2d} OFF NEUTRAL'.format(two_space, level, off_neutral))
      cost = find_ability_costs(level_info.get('abilities', list()))
      if cost > 0 and not class_name in ability_costs:
        ability_costs[class_name] = 'At {0} {1} has an ability of cost {2}'.format(level, class_name, cost)
      #print('{0}{1}: {2}'.format(two_space, level, this_level_tokens))
      level_up_tokens += this_level_tokens
      if level == 'level_0' and level_up_tokens > 0:
        zero_stats.append(('{0} has {1} at LV0'.format(class_name, level_up_tokens), level_up_tokens))
    actual_offset[class_name] = off_neutral
    print('{0}TOTAL {1} AVG {2}'.format(two_space, level_up_tokens, level_up_tokens/10))
    print()
  print()

  print('Starting off neutrality:')
  avg = 0
  for val in off_neutral_list:
    print(val[0])
    avg += val[1]
  print(avg / len(off_neutral_list))
  print()

  print('Final neutrality:')
  print()
  for key, val in actual_offset.items():
    print(key, val)

  print()
  if len(zero_stats) > 0:
    print('ERROR: the following classes have stat points awarded at level zero')
    for val in zero_stats:
      print(val[0])

  print()
  print('most negative stat to start')
  print(most_positive)
  print('most positive stat to start')
  print(most_negative)

  print()
  print('Intelligence requirements:')
  for key, val in ability_costs.items():
    print(val)

  r_off_neutral = list()
  for race_name, race_details in rnr_utils.GLOBAL_RACE_DATA.items():
    for subrace_name, subrace_details in race_details['subraces'].items():
      off_neutral = sum_vals(subrace_details['stats']) + choice_mod(subrace_details['abilities'])
      r_off_neutral.append(('{0:12} {1:2d}'.format(subrace_name+':', off_neutral), off_neutral))
  print()
  print('Race Neutrality')
  print()
  avg = 0
  for val in r_off_neutral:
    print(val[0])
    avg += val[1]
  print(avg / len(r_off_neutral))
  print()