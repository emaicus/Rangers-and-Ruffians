import yaml
import math
import os
import json

def combine_stats(stats, new_level_stats):
  new_stats = dict()
  for key, value in stats.items():
    new_stats[key] = value
    if key in new_level_stats.keys():
      new_stats[key] += new_level_stats[key]
  return new_stats

def print_header(level, name, stats, file_stream):
  file_stream.write('\n')
  file_stream.write('Level {0} {1}:\n'.format(level,name))
  file_stream.write('HP: {0}\n'.format(get_health(stats, level, multiplier=2)))
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

def get_health(stats, level, multiplier, base=20):
  summed_level = 0
  for i in range(level+1):
    summed_level += i

  modifier = stats['Vitality'] * level * 2 if level > 0 else stats['Vitality']

  return base + summed_level + modifier

def process_class(name, rnr_class):

  if not os.path.exists('level_output'):
    os.mkdir('level_output')

  with open(os.path.join('level_output','{0}.txt'.format(name)), 'w') as outfile:

    outfile.write('{0}\n'.format(name))

    stats = rnr_class['base_stats']
    abilities = rnr_class['base_abilities']

    found_subclass = False
    subclass_abilities = {}

    for level in range(0,11):
      level_string = 'level_{0}'.format(level)
      level_details = rnr_class['levels'][level_string]
      level_stats = level_details.get('stats', {})
      level_abilities = level_details.get('abilities', [])

      abilities = abilities + level_abilities
      stats = combine_stats(stats, level_stats)

      for key in level_details.keys():
        if 'subclass' in key:
          found_subclass = True
          subclass_name = key.split('_')[1]
          if not key in subclass_abilities:
            subclass_abilities[key] = []
          subclass_abilities[key] = subclass_abilities[key] + level_details[key]

      if not found_subclass:
        print_header(level, name, stats, outfile)
        print_stats(stats, outfile)
        print_abilities(None, abilities, outfile)
      else:
        print_header(level, name, stats, outfile)
        print_stats(stats, outfile)
        print_abilities(None, abilities, outfile)
        
        for key in subclass_abilities.keys():
          subclass_name = key.split('_')[1]
          print_abilities(subclass_name, subclass_abilities[key], outfile)


def main():
  with open('leveled_classes.yml') as data_file:
    rnr_classes = yaml.load(data_file)

  for class_type, classes in rnr_classes.items():
    if classes is None:
      continue
    for rnr_class_name, rnr_class_info in classes.items():
      print('Working on {0}'.format(rnr_class_name))
      process_class(rnr_class_name, rnr_class_info)
  print('All done!')

if __name__ == '__main__':
  main()
