import yaml
import re
import os

def build_dice(match_obj):
  ret = ''
  if match_obj.group(0):
    ret = f'{match_obj.group(0)}'
  ret = f'{ret}d{match_obj.group(1)}'
  if match_obj.group(2):
    ret = f'{ret} {match_obj.group(2)}'
  return ret


with open(os.path.join('..', 'spells.yml'), 'r') as data_file:
  data = yaml.load(data_file)

new_data = dict()

for spellbook, tiers in data.items():
  new_data[spellbook] = dict()
  for tier, spells in tiers.items():
    new_data[spellbook][tier] = dict()
    for spell, old_info in spells.items():
      new_info = dict()
      new_info['description'] = old_info['description']
      if 'charisma_cost' in old_info:
        new_info['charisma_cost'] = old_info['charisma_cost']
      if not 'cost' in old_info:
        print(f'no cost in {spell}')
      new_info['cost'] = old_info['cost']
      description = old_info['description']
      if 'concentrat' in description.lower():
        new_info['duration'] = "concentration Candidate"
      if 'offhand' in description.lower():
        new_info['action_type'] = "Offhand Action Candidate"
      if 'reaction' in description.lower():
        new_info['action_type'] = "Reaction Candidate"

      # If we find a dice
      dice = re.search('(\d+)?d(\d+)([\+\-]\d+)?', description)
      if dice:
        if 'heal' in description.lower():
          new_info['balance_type'] = 'healing candidate'
          new_info['major_healing_dice'] = build_dice(dice)
        elif ('do' in description.lower() or 'deal' in description.lower()) and 'damage' in description.lower():
          new_info['balance_type'] = 'damage candidate'
          new_info['major_damage_dice'] = build_dice(dice)

      if 'save' in description.lower():
        new_info['effects'] = dict()
        new_info['effects']['candidate'] = True
      new_data[spellbook][tier][spell] = new_info

with open('tmp_spells.yml', 'w') as outfile:
  yaml.dump(new_data, outfile, default_flow_style=False)

