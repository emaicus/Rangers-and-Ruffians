import rnr_utils

def quick_health(level, vitality):
  extra = vitality if level == 0 else level*vitality
  return 20 + sum(range(level+1)) + extra

def vitality_chart():
  print('{0:4}'.format('vit'),end='')
  for i in range(11):
    print('{0:4}'.format(i), end='')
  print()

  for vitality in range(0,11):
    print('{0:4}'.format(vitality),end='')
    for level in range(0,11):
      print('{0:4}'.format(quick_health(level, vitality)),end='')
    print()

def bin_health(possibilities, data):
  possibilities = possibilities+1
  health_dict = dict()
  for i in range(0,possibilities):
    health_dict[i] = list()
  for obj in data:
    health_dict[obj.vitality].append(obj.name)
  for i in range(0,possibilities):
    print('{0}: '.format(i),end='')
    lis = health_dict[i]
    for name in lis:
      print(name,end=', ')
    print()


if __name__ == '__main__':
  races = rnr_utils.load_all_race_objects()
  classes = rnr_utils.load_all_class_objects(10)
  characters = rnr_utils.load_all_characters(10)
  print('VITALITY CHART:')
  vitality_chart()
  print()
  print('RACE VITALITY')
  bin_health(5, races)
  print()
  print('CLASS VITALITY')
  bin_health(5, classes)
  print()
  # print('10th LEVEL CHARACTER VITALITY')
  # bin_health(10, characters)