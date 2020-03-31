import os
import json
import yaml
import statistics 

REQUIRED = ['cost', 'target', 'num_targets', 'description', 'balance_type', 'duration', 'combat_duration', 'school']
ALL_FIELDS = ['cost', 'target', 'num_targets', 'duration', 'combat_duration', 'action_type', 'charisma_cost', 'major_damage_dice',
              'major_damage_type', 'minor_damage_dice', 'minor_damage_type', 'minor_healing_dice',
              'major_healing_dice', 'casting_time', 'range', 'components', 'balance_type', 'effects', 'description']
VALID_TARGETS = ['friendly', 'enemy', 'entity', 'object', 'self', 'space', 'animal', 'region', 'school']

DURATION_MAPPINGS = {
  'save' : 2,
  'battle' : 3,
  'concentration' : 2
}

TARGET_MAPPINGS = {
  'aoe' : 2,
  'line' : 2,
  'battle' : 4
}
# A damage multiplier or the string debuff.
DAMAGE_TYPE_MAPPINGS = {
  'elemental' :  'debuff',
  'poison' :  1.5,
  'fire' :  1.5,
  'force' : 'debuff',
  'ice' :  'debuff',
  'dark' :  'debuff',
  'light' : 1.5,
  'lightning' : 'debuff'
}


ESTIMATED_VALUE = {
  'minor utility' : 0,
  'greater utility' : 1,
  'major utility' : 2,
  'minor buff' : 1,
  'greater buff' : 2,
  'major buff' : 3,
  'minor debuff' : 0,
  'greater debuff' : 1,
  'major debuff' : 2,
  'minor restoration' : 1,
  'greater restoration' : 2,
  'major restoration' : 3, 
  'minor summoning' : 1,
  'greater summoning' : 2,
  'major summoning' : 3,
  'minor healing' : 1,
  'greater healing' : 2,
  'major healing' : 3,
  'minor damage' : 0,
  'greater damage' : 0,
  'major damage' : 0
}


def validate_spellbook(spellbook):
  errors = list()
  for tier, spells in spellbook.items():
    for spell, spell_info in spells.items():

      for key in REQUIRED:
        if not key in spell_info:
          errors.append(f'{spell} is missing {key}')

      all_fields = dict()
      for key in ALL_FIELDS:
        all_fields[key] = spell_info.get(key, None)
      for key in spell_info.keys():
        if not key in ALL_FIELDS:
          errors.append(f'{spell}: unknown key {key}')

      if all_fields['balance_type'] is not None:
        balance_type = all_fields['balance_type']
        if not balance_type in list(ESTIMATED_VALUE.keys()):
          errors.append(f"{spell}: bad balance type {balance_type}")
        else:
          if 'damage' in balance_type:
            dmg_str = 'minor_damage_dice' if all_fields['minor_damage_dice'] is not None else 'major_damage_dice'
            if all_fields[dmg_str] is None:
              errors.append(f"{spell} is of damage type, but has no damage dice.")
              continue
      if all_fields['target'] is not None:
        if not all_fields['target'] in VALID_TARGETS:
          errors.append(f"{spell}: invalid target {all_fields['target']}")
      if all_fields['num_targets'] is not None:
        if not all_fields['num_targets'] in list(TARGET_MAPPINGS.keys()):
          if not isinstance(all_fields['num_targets'], int):
            errors.append(f"{spell}: bad num_targets {all_fields['num_targets']}")
      if all_fields['combat_duration'] is not None:
        duration = all_fields['combat_duration']
        if duration not in ['save', 'battle', 'concentration']:
          if not isinstance(duration, int):
            errors.append(f"{spell}: bad combat_duration {duration}")
      if all_fields['major_damage_type'] is not None:
        if all_fields['major_damage_type'] not in list(DAMAGE_TYPE_MAPPINGS.keys()):
          errors.append(f"{spell}: bad major damage type {all_fields['major_damage_type']}")
      if all_fields['minor_damage_type'] is not None:
        if all_fields['minor_damage_type'] not in list(DAMAGE_TYPE_MAPPINGS.keys()):
          errors.append(f"{spell}: bad major damage type {all_fields['minor_damage_type']}")
      if all_fields['combat_duration'] is not None:
        if not all_fields['combat_duration'] in list(DURATION_MAPPINGS.keys()):
          if not isinstance(all_fields['combat_duration'], int):
            errors.append(f"{spell}: bad combat_duration {all_fields['combat_duration']}")
  for error in errors:
    print(error)
  return errors

def spellbook_statistics(name, spellbook):
  type_by_tier = dict()
  print(f"Stats for {name}")

  for tier, spells in spellbook.items():
    type_by_tier[tier] = dict()
    for spell, spell_info in spells.items():
      balance_type = spell_info['balance_type']
      if not balance_type in type_by_tier[tier]:
        type_by_tier[tier][balance_type] = list()
      type_by_tier[tier][balance_type].append(spell)

  for tier, info in type_by_tier.items():
    print(f"  {tier}")
    for balance_type, spells in info.items():
      print(f"    {balance_type}: {len(spells)}", end='')
      for spell in sorted(spells):
        print(f" {spell}", end=',')
      print()

def compute_estimated_damage_dice(info):
  damage_dice = 0
  num_targets = 0
  debuffs = 0
  multiplier = 1
  dmg_class = None

  for dice_type in ['major', 'minor']:
    dmg_dice_str = f'{dice_type}_damage_dice'
    dmg_type_str = f"{dice_type}_damage_type"
    
    if dmg_dice_str in info:
      dmg_class = dice_type
      damage_dice += info[dmg_dice_str]
      if dmg_type_str in info:
        if isinstance(DAMAGE_TYPE_MAPPINGS[info[dmg_type_str]], str):
          debuffs += 1
        else:
          multiplier = DAMAGE_TYPE_MAPPINGS[info[dmg_type_str]]

  duration = info['combat_duration'] if isinstance(info['combat_duration'], int) else DURATION_MAPPINGS[info['combat_duration']]

  if 'effects' in info:
    debuffs += len(info['effects'])

  targets = info['num_targets']
  if info['target'] == 'space' and duration > 1:
    duration = 2
    targets = TARGET_MAPPINGS['aoe']
  num_targets = TARGET_MAPPINGS[targets] if isinstance(targets, str) else targets
  damage_dice = damage_dice * num_targets * duration * multiplier
  debuffs *= num_targets
  return int(damage_dice), debuffs, dmg_class

def estimate_damage_value(name, info):
  dice, debuffs, dmg_class =  compute_estimated_damage_dice(info)
  print(f"{name}: {dmg_class} dice {dice} debuffs {debuffs}")
  
  if dmg_class == 'minor':
    dice = int(dice * .75)
  #aggregate = float(max(0, ( dice + ( float(debuffs * .5) ) - 1.5 )))
  aggregate = float( dice + float(debuffs * .5) )
  return aggregate


def estimated_value(name, info):
  balance_type = info['balance_type']
  estimated_cost = ESTIMATED_VALUE[balance_type]
  spell_cost = info['cost']
  modifier = 0

  if 'debuff' in balance_type and not '1' in info['target']:
    estimated_cost += 1

  if 'summoning' in balance_type and not '1' in info['target']:
    estimated_cost += 1

  if 'damage' in balance_type:
    dmg_estimates = {
      0: 1,
      1: 2.5,
      2: 5,
      3: 10,
      4: 20,
      5: 40,
      6: 80
    }
    aggregate = estimate_damage_value(name, info)
    for key, val in dmg_estimates.items():
      if aggregate <= val:
        return key
  return estimated_cost

def balance_spellbook(spellbook):
  spell_book_data = dict()
  for tier, spells in spellbook.items():
    for spell, spell_info in spells.items():
      if not 'damage' in spell_info['balance_type']:
        continue
      actual_cost = spell_info['cost']
      expected_cost = estimated_value(spell, spell_info)
      if actual_cost < expected_cost:
        print(f'{spell} performs better than expected (actual: {actual_cost}, expected: {expected_cost})')
      if expected_cost < actual_cost:
        print(f'{spell} performs worse than expected (actual: {actual_cost}, expected: {expected_cost})')

def balance_damage_spells(data):
  # map of cost to damage dice value and name.
  inferences = dict()
  stats = dict()
  for i in range(0, 7):
    inferences[i] = list()
    stats[i] = list()

  for spellbook, tiers in data.items():
    for tier, spells in tiers.items():
      for name, info in spells.items():
        if 'damage' not in info['balance_type']:
          continue
        cost = info['cost']
        computed_cost = estimate_damage_value(name, info)
        inferences[cost].append((name, computed_cost))
        stats[cost].append(computed_cost)

  for assigned_cost, spell_list in inferences.items():
    print(f'values of spells assigned a cost of {assigned_cost}')
    for name, computed_cost in sorted(spell_list, key=lambda x: x[1], reverse=True):
      print(f"  {name}: {computed_cost}")

  for i in range(0,7):
    stdev = 'n/a'
    if len(stats[i]) > 1:
      stdev = statistics.stdev(stats[i])
    print(f'For cost {i}, avg was {sum(stats[i]) / len(stats[i])} and stdev was {stdev}')

def spell_schools(data):
  schools = dict()
  for spellbook, tiers in data.items():
    for tier, spells in tiers.items():
      for name, info in spells.items():
        school_parts = info['school'].split('-')
        agg = school_parts[0]
        for part in school_parts[1:]:
          if agg not in schools:
            schools[agg] = 0
          schools[agg] += 1
          agg = f"{agg}-{part}"
        if agg not in schools:
          schools[agg] = 0
        schools[agg] += 1
  for key, val in schools.items():
    print(f"{key}: {val}")



if __name__ == '__main__':
  with open("formatted_spells.yml", 'r') as infile:
    data = yaml.load(infile)

  for spellbook in ["the_druid's_guidebook",]:
    if len(validate_spellbook(data[spellbook])) == 0:
      spellbook_statistics(spellbook, data[spellbook])
      balance_spellbook(data[spellbook])

  print()
  balance_damage_spells(data)
  print()
  spell_schools(data)