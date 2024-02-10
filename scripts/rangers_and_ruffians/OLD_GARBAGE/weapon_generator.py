import sys
import os
import math 
import random
import json

def roll_attack(primary, secondary, modifier):
  first  = random.randint(1,primary)
  # if we crit
  if first == primary:
    first += random.randint(1,primary)
  second = 0 if secondary <= 0 else random.randint(1,secondary)
  return first + second + modifier

def prettify_weapon(weapon):
  ret = f"1d{weapon['primary']}"
  if weapon['secondary'] > 0:
    ret = f"{ret} + 1d{weapon['secondary']}"
  if weapon['modifier'] > 0:
    ret = f"{ret} + {weapon['modifier']}"
  return ret

def generate_weapon(weapon, one_at_random=True):

  weapon_by_dice_or_greater_relationship = {
    4  : ["Shortsword", "Dagger", "Sabre", "Throwing Axe", "Flail", "Club", "Whip", "Spear", "Pistol", "Shortbow", "War Pick", "Bo Staff", "Throwing Darts", "Rapier"],
    6  : ["Bastard Sword", "Handaxe", "Javelin", "Long Knife", "Rifle", "Longbow", "War Hammer", "Katana"],
    8  : ["Greatsword", "Swordstaff", "Greataxe"],
    10 : ["Claymore"],
    12 : []
  }

  weapons_by_dice = dict()
  running = list()
  for die in [4,6,8,10,12]:
    running += weapon_by_dice_or_greater_relationship[die]
    weapons_by_dice[die] = list(running)


  # Pre, Post, Damage Type
  secondary_die_effects = [
    ["Bitter ", " of Frost", "Frost"],
    ["Blazing ", "", "Fire"],
    ["", " of Lightning", "Lightning"],
    ["Radiant ", "", "Holy"],
    ["Dark ", "", "Shadow"],
    ["Draining ", "", "Vampiric"]
  ]

  modifier_descriptions = {
    0 : "",
    1 : "Keen ",
    2 : "Honed ",
    3 : "Enhanced ",
    4 : "Imbued ",
    5 : "Legendary "
  }

  # artifact_effects = [
  #   {
  #     "pre" : "Sentient",
  #     "description" : "This weapon has a personality."
  #   },
  #   {
  #     "pre" : "Walling",
  #     "description" : "Expend two action points to create a 30ft. wall of {}"
  #   },
  #   {
      
  #   }
  # ]

  primary, secondary, modifier = weapon['primary'], weapon['secondary'], weapon['modifier']

  if one_at_random:
    weapon_type = random.choice(weapons_by_dice[primary])
    pre_secondary, post_secondary, secondary_dmg_type = ['','',''] if secondary == 0 else random.choice(secondary_die_effects)
    modifier_description = modifier_descriptions[modifier]
    secondary_dice_string = '' if secondary == 0 else f"+ 1d{secondary} {secondary_dmg_type} damage"
    modifier_dmg_string = '' if modifier == 0 else f' + {modifier}'
    return f"{modifier_description}{pre_secondary}{weapon_type}{post_secondary}. 1d{primary} primary damage {secondary_dice_string}{modifier_dmg_string}"




  

def first_cull_function(weapon, pval):
  tier = {
    'burgeoning' : [0,1,2,3,4],
    'heroic' : [5,6,7,8],
    'master' : [9,10,11,12],
    'legendary' : [13,14,15]
  }

  pval_str = ''
  primary = weapon['primary']
  secondary = weapon['secondary']
  modifier = weapon['modifier']

  skip = False
  if pval in tier['burgeoning']:
    pval_str = 'burgeoning'
    if secondary > 0:
      skip = True
  elif pval in tier['heroic']:
    pval_str = 'heroic'
    if modifier > 3:
      skip = True
  elif pval in tier['master']:
    pval_str = 'master'
    if secondary == 4:
      skip = True
  elif pval in tier['legendary']:
    pval_str = 'legendary'
    if secondary < 8:
      skip = True
  else:
    print(f"ERROR: cull received bad pval {pval}")
    sys.exit(1)
  # if skip:
  #     print(f'    SKIPPING pval {pval_str} {prettify_weapon(weapon)}')
  return skip


if __name__ == '__main__':
  primary_dice = {
    1 : [4,],
    2 : [6,],
    3 : [8,],
    4 : [10,],
    5 : [12,]
  }

  secondary_dice = {
    0 : [0,],
    1 : [4,],
    2 : [6,],
    3 : [8,],
    4 : [10,],
    5 : [12,]
  }

  modifiers = {
    0 : [0,],
    1 : [1,],
    2 : [2,],
    3 : [3,],
    4 : [4,],
    5 : [5,]
  }

  weapons = dict()

  for pval, mult_primary_die in primary_dice.items():
    for primary_die in mult_primary_die:
      for sval, mult_secondary_die in secondary_dice.items():
        for secondary_die in mult_secondary_die:
          if primary_die < secondary_die:
            continue
          for mval, mult_modifier in modifiers.items():
            for modifier in mult_modifier:
              val = pval + sval + mval - 1
              if not val in weapons:
                weapons[val] = list()
              primary_die/2
              secondary_die/2
              avg_dmg = math.ceil((primary_die/2) + (secondary_die/2) + modifier)
              weapons[val].append({'primary':primary_die, 'secondary':secondary_die, 'modifier':modifier, 'expected_avg':avg_dmg})

  cull = first_cull_function

  print('Actual has been proven to approach expected at 10,000. Reducing to 1,000 for speed.')
  for pval, weapon_list in weapons.items():
    print(pval)
    for weapon in weapon_list:
      if cull(weapon, pval):
        continue
      tests = 10000
      computed_avg = 0
      for i in range(tests):
        computed_avg += roll_attack(weapon['primary'], weapon['secondary'], weapon['modifier'])
      computed_avg /= tests
      #print(f"  {prettify_weapon(weapon)}. {weapon['expected_avg']} vs {computed_avg}")
      print(f"  {generate_weapon(weapon)}")
  



