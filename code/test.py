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
    print('!!!!!!!!!!!!!!!FOUND CHOICE STAT!!!!!!!!!!!')
    s += 1
  elif 'Greater Choice Stat' in d:
    print('!!!!!!!!!!!!!!!FOUND CHOICE STAT!!!!!!!!!!!')
    s += 2
  elif 'Choice of Model' in d:
    print('!!!!!!!!!!!!!!!FOUND CHOICE STAT!!!!!!!!!!!')
    s += 2
  return s
if __name__ == '__main__':
  actual_offset = dict()
  rnr_utils.printLogo()
  rnr_utils.load_Rangers_And_Ruffians_Data()
  space = '  '
  two_space = '{0}{1}'.format(space, space)
  for class_name, class_details in rnr_utils.GLOBAL_CLASS_DATA.items():
    print("{0}".format(class_name))
    print('{0}stats:'.format(space))
    off_neutral = sum_vals(class_details['base_stats']) + choice_mod(class_details['base_abilities'])
    print('{0}{1} OFF NEUTRAL'.format(two_space, off_neutral))
    level_up_tokens = 0
    for level, level_info in class_details['levels'].items():
      this_level_tokens = sum_vals(level_info.get('stats', {})) + choice_mod(level_info.get('abilities', list()))
      print('{0}{1}: {2}'.format(two_space, level, this_level_tokens))
      level_up_tokens += this_level_tokens
    actual_offset[class_name] = off_neutral + level_up_tokens
    print('{0}TOTAL {1} AVG {2}'.format(two_space, level_up_tokens, level_up_tokens/10))
    print()
  print()
  for key, val in actual_offset.items():
    print(key, val)

