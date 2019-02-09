import json
import sys
import os
import yaml
import traceback
import rnr_utils
from operator import attrgetter
import collections

tier_map = {
  0 : "new",
  1 : "heroic",
  2 : "legendary"
}

def generate_combo_stats(races, classes):
  if not os.path.exists("stat_output"):
    os.makedirs("stat_output")

  #get the data for all classes.
  with open("stat_output/class_combos.txt", 'w') as outfile:
    for rnr_class in classes:
      outfile.write("Details for all {0}s\n".format(rnr_class))
      combos = rnr_utils.load_combos_given_list(races, [rnr_class,])

      for combo in combos:
        outfile.write(combo.tabbed_string())
      outfile.write('\n')

  #get the data for all races.
  with open("stat_output/race_combos.txt", 'w') as outfile:
    for rnr_race in races:
      outfile.write("Details for all {0}s\n".format(rnr_race))
      combos = rnr_utils.load_combos_given_list([rnr_race,],classes)
      
      for combo in combos:
        outfile.write(combo.tabbed_string())
      outfile.write('\n')

  all_combos = rnr_utils.load_all_race_class_combos(inflate_choice_stats=True)
  #get the data for all stats.
  with open("stat_output/all_combos.txt", 'w') as outfile:
    for stat in rnr_utils.get_all_stat_names():
      outfile.write("{0}\n".format(stat))
      all_combos.sort(key = attrgetter(stat.lower()), reverse = True)
      for combo in all_combos:
        outfile.write("\t{0}: {1}\n".format(combo.name, combo.get_stat(stat)))
      outfile.write('\n')

#Generate the race by race rankings.
def rankRaces():
  races = rnr_utils.load_all_race_objects(inflate_choice_stats=True)
  with open("stat_output/race_rankings.txt", 'w') as outfile:
    for stat in rnr_utils.get_all_stat_names():
      outfile.write("SORT BY: {0}\n".format(stat))
      races.sort(key = attrgetter(stat.lower()), reverse = True)
      for race in races:
        outfile.write("\t{0}: {1}\n".format(race.name, race.get_stat(stat)))
      outfile.write("\n")

#Generate the race by race rankings.
def rankClasses():
  classes = rnr_utils.load_all_class_objects(inflate_choice_stats=True)
  with open("stat_output/class_rankings.txt", 'w') as outfile:
    for stat in rnr_utils.get_all_stat_names():
      outfile.write("SORT BY: {0}\n".format(stat))
      classes.sort(key = attrgetter(stat.lower()), reverse = True)
      for rnr_class in classes:
        outfile.write("\t{0}: {1}\n".format(rnr_class.name, rnr_class.get_stat(stat)))
      outfile.write('\n')

def mage_sort_function(obj):
  if obj.rnr_class.lower() != 'sorcerer' and obj.rnr_class.lower() != 'bard':
    return obj.get_stat('inner_fire')+obj.get_stat('intelligence')
  else:
    return obj.get_stat('charisma') + obj.get_stat('intelligence')

def is_casting_class(obj):
  if obj.rnr_class.lower() in rnr_utils.casting_classes.keys() or 'druid' in obj.rnr_class.lower() or 'battle mage' in obj.rnr_class.lower():
   return True
  else:
    return False

def assess_damage_output(obj):
  #if it is a casting class
  if is_casting_class(obj):
    if obj.rnr_class.lower() != 'sorcerer' and obj.rnr_class.lower() != 'bard':
      return obj.get_stat('inner_fire')
    else:
      return obj.get_stat('charisma')
  else:
    return max(obj.get_stat('dexterity'), obj.get_stat('strength'))

#Generate the race by race rankings.
def rankSpecial(tier=1):
  all_combos = rnr_utils.load_all_race_class_combos(inflate_choice_stats=True,tier=tier)
  with open("stat_output/tier_{0}.txt".format(tier), 'w') as outfile:
    # all_combos.sort(key = attrgetter('inner_fire') + attrgetter('intelligence'), reverse = True)
    all_combos.sort(key=mage_sort_function, reverse=True)
    outfile.write('Mages\n')
    for combo in all_combos:
      if not combo.rnr_class.lower() in rnr_utils.casting_classes.keys() and not 'druid' in combo.rnr_class.lower() and not 'battle mage' in combo.rnr_class.lower():
        continue
      else:
        s = combo.tabbed_string()
        outfile.write(s)
    outfile.write("\n")

    outfile.write('Fighters\n')
    # all_combos.sort(key = max(attrgetter('strength'), attrgetter('dexterity')), reverse = True)
    all_combos.sort(key=lambda obj: max(obj.get_stat('dexterity'),obj.get_stat('strength')), reverse=True)
    for combo in all_combos:
      outfile.write(combo.tabbed_string())
    outfile.write("\n")

    outfile.write('Tanks\n')
    # all_combos.sort(key = max((attrgetter('strength')+attrgetter('vitality')), (attrgetter('dexterity') + attrgetter('vitality'))), reverse = True)
    all_combos.sort(key=lambda obj: max(obj.get_stat('dexterity')+obj.get_stat('vitality'),obj.get_stat('strength')+obj.get_stat('vitality')), reverse=True)
    for combo in all_combos:
      outfile.write(combo.tabbed_string())
    outfile.write("\n")

    for tier in [0,1,2]:
      outfile.write('Tier {0} Health\n'.format(tier))
      # all_combos.sort(key = max((attrgetter('strength')+attrgetter('vitality')), (attrgetter('dexterity') + attrgetter('vitality'))), reverse = True)
      all_combos.sort(key=lambda obj: obj.get_health(tier=tier), reverse=True)
      for combo in all_combos:
        outfile.write('\t{0}: {1}\n'.format(combo.name, combo.get_health(tier=tier)))
      outfile.write("\n")

def outliers(tier=1):
  all_combos = rnr_utils.load_all_race_class_combos(inflate_choice_stats=True,tier=tier)
  with open("stat_output/write_up_tier_{0}.txt".format(tier), 'w') as outfile:
    # all_combos.sort(key = attrgetter('inner_fire') + attrgetter('intelligence'), reverse = True)
    all_combos.sort(key=assess_damage_output, reverse=True)

    combat_bin = dict()
    mage_combat_bin = dict()
    physical_combat_bin = dict()
    greater_than_3 = list()
    less_than_zero = list()
    all_list = list()
    greater_than_3_classes = set()

    for combo in all_combos:
      combat_ability = assess_damage_output(combo)
      if not combat_ability in combat_bin:
        combat_bin[combat_ability] = 0
      combat_bin[combat_ability] += 1

      if is_casting_class(combo):
        if not combat_ability in mage_combat_bin:
          mage_combat_bin[combat_ability] = 0
        mage_combat_bin[combat_ability] +=1
      else:
        if not combat_ability in physical_combat_bin:
          physical_combat_bin[combat_ability] = 0
        physical_combat_bin[combat_ability] +=1

      if combat_ability > 2:
        greater_than_3.append((combo, combat_ability))
        greater_than_3_classes.add(combo.rnr_class)
      
      if combat_ability < 2:
        less_than_zero.append((combo,combat_ability))
      all_list.append((combo,combat_ability))

    ordered_phys = collections.OrderedDict(sorted(physical_combat_bin.items()))
    ordered_mag  = collections.OrderedDict(sorted(mage_combat_bin.items()))
    ordered_all  = collections.OrderedDict(sorted(combat_bin.items()))

    for c_dict, phrase in [(ordered_all, 'all combat readiness\n'),(ordered_mag, 'caster combat readiness\n'),(ordered_phys, 'fighter combat readiness\n')]:
      outfile.write(phrase)
      for key, val in c_dict.items():
        outfile.write('\t{0}, {1}\n'.format(key,val))
    outfile.write("\n")

    outfile.write('3 or greater combat ability\n')
    for item in sorted(greater_than_3, key=lambda x: x[1], reverse=True):
      outfile.write('\t{0} {1}\n'.format(item[0].name, item[1]))
    outfile.write("\n")

    outfile.write('1 or less combat ability\n')
    for item in sorted(less_than_zero, key=lambda x: x[1], reverse=True):
      outfile.write('\t{0} {1}\n'.format(item[0].name, item[1]))
    outfile.write("\n")

    outfile.write('All sorted\n')
    for item in sorted(all_list, key=lambda x: x[1], reverse=True):
      outfile.write('\t{0} {1}\n'.format(item[0].name, item[1]))
    outfile.write("\n")
    
    outfile.write('All sorted\n')
    for item in greater_than_3_classes:
      outfile.write('\t{0}\n'.format(item))
    outfile.write("\n")

# def rankClassType(classes, stats):
#   with open("stat_output/class_type_rankings.txt", 'w') as outfile:
#     for class_type, info in classes.items():
#       outfile.write("{0}\n".format(class_type.upper()))
#       for stat in stats:
#         outfile.write("SORT BY: {0}\n".format(stat))
#         for class_name in sorted(info, key=lambda k: info[k]['stats'][stat]):
#           stat_value = info[class_name]["stats"][stat]
#           outfile.write("\t{0}: {1}\n".format(class_name, stat_value))
#         outfile.write("\n")


def main():

  races = rnr_utils.get_all_race_names()
  classes = rnr_utils.get_all_class_names()

  print("Generating raw combinations...")
  generate_combo_stats(races, classes)
  print("Generating race rankings...")
  rankRaces()
  print("Generating class rankings...")
  rankClasses()
  for tier in [0,1]:
    print('Ranking by type for tier {0}...'.format(tier))
    rankSpecial(tier=tier)
    print('Finding outliers for tier {0}...'.format(tier))
    outliers(tier=tier)
  # print("Ranking classes by type...")
  # rankClassType(classes, all_stat_names)
  # print("Done.")
  # for key, val in all_race_class_combos.items():
  #   if "Gnome" in key:
  #     print(key)
  #     for stat, value in val["stats"].items():
  #       print("\t{0}: {1}".format(stat, value))


  # for val in sorted(all_race_class_combos, key=lambda k: all_race_class_combos[k]['stats']["Charisma"]):
  #   print(val)
  #   for stat, value in all_race_class_combos[val]["stats"].items():
  #     print("\t{0}: {1}".format(stat, value))


if __name__ == "__main__":
    main()