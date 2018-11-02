import json
import sys
import os
import rnr_utils



def main():
  classHelper(class_data, ability_dict, "images/class", "../classes.md")
  raceHelper(race_data, ability_dict, "images/race/female", "../female_races.md")
  raceHelper(race_data, ability_dict, "images/race/male", "../male_races.md")


if __name__ == "__main__":
  rnr_utils.printLogo()

  races = rnr_utils.load_all_race_objects()
  rnr_classes = rnr_utils.load_all_class_objects_by_type()

  with open('../classes.md', 'w') as outfile:
    for rnr_class_type, class_list in sorted(rnr_classes.items()):
      outfile.write('# {0}   \n'.format(rnr_class_type))
      for rnr_class in sorted(class_list, key=lambda x: x.name):
        outfile.write(rnr_class.markdownify("images/class"))

  for gender in ['male', 'female']:
    with open('../{0}_races.md'.format(gender), 'w') as outfile:
      for race in sorted(races, key=lambda x: x.name):
        print (race.name)
        if race.name == 'Daemonspawn':
          print('skip')
          continue
        outfile.write(race.markdownify('images/race/{0}'.format(gender)))
      d = rnr_utils.load_race('Daemonspawn')
      outfile.write(d.markdownify('images/race/{0}'.format(gender)))

  print()
  print("Done!")
