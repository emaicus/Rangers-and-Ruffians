import json
import sys
import os
import rnr_utils

if __name__ == "__main__":
  rnr_utils.printLogo()
  print()
  wizard = rnr_utils.get_rnr_class_data_with_name('wizard')

  #print('making assumption about starting number of spells.')
  #level_dict = {'Level Zero' : 2, 'Level One' : 1}
  level_dict = {}
  can_learn_mask = {}
  for num in range(11):
    level_string = 'level_{0}'.format(num)
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