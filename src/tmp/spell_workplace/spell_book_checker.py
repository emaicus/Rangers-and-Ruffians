import sys
import os
import json
import yaml
import traceback
import argparse
import statistics
from pathlib import Path
import jsonschema

from rnr_spell import rnr_spell
import rnr_balance

BASE_DIRECTORY = Path(__file__).resolve().parent
SCHEMA_PATH = os.path.join(BASE_DIRECTORY, "spell_schema.json")
SPELLBOOK_PATH = os.path.join(BASE_DIRECTORY, "spells.yml")

try:
  from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
  from yaml import Loader, Dumper

def summoned_creature_check(all_spells):
  print("\nChecking Summoned Creatures...")
  for spell in all_spells:
    if spell.summoned_creature is not None:
      print(f"{spell.name}:")
      for key, value in spell.summoned_creature.items():
        print(f"  {key}: {value}")

def print_balance_values():
  print('Average Attack Damage -- No Misses')
  for damage_type in ['light', 'heavy', 'magic']:
    print(f"{damage_type.title()} Damage")
    for ap_spent in [0, 1, 2]:
      print(f"{ap_spent} AP")
      for tier in ['tier_1', 'tier_2', 'tier_3']:
        for min_or_max in [True, False]:
          print(rnr_balance.get_expected_damage_at_tier(tier, min_or_max, damage_type, ap_spent, False ), end=', ')
      print()
    print()
  
  print('Average Turn Damage -- No Misses')
  for damage_type in ['light', 'heavy', 'magic']:
    print(f"{damage_type.title()} Damage")
    for ap_spent in [0, 1, 2]:
      print(f"{ap_spent} AP")
      for level in rnr_balance.get_tier_level_array():
          print(rnr_balance.avg_turn_dmg(level, damage_type, ap_spent, False ), end=', ')
      print()
    print()
  
  print('Average Turn Damage -- Glancing Blows')
  for damage_type in ['light', 'heavy', 'magic']:
    print(f"{damage_type.title()} Damage")
    for ap_spent in [0, 1, 2]:
      print(f"{ap_spent} AP")
      for level in rnr_balance.get_tier_level_array():
        print(rnr_balance.avg_turn_dmg(level, damage_type, ap_spent ), end=', ')
      print()
    print()
  
  print('Average Balance Turn Damage -- No Misses')
  for ap_spent in [0, 1, 2, 3]:
    print(f"{ap_spent} AP")
    for level in rnr_balance.get_tier_level_array():
      print(rnr_balance.get_balance_dmg(level, ap_spent ), end=', ')
    print()

  print()
  print('Balance Evasion')
  for level in rnr_balance.get_tier_level_array():
    print(rnr_balance.get_balance_evasion(level), end=', ')
  print()
  print()

  print('Balance Health')
  for level in rnr_balance.get_tier_level_array():
    print(rnr_balance.get_balance_health(level), end=', ')
  print()

  print()
  print('Interpolated Evasion')
  for level in range(0,15 +1):
    print(rnr_balance.get_balance_evasion(level), end=', ')
  print()

  print('Interpolated Health')
  for level in range(0,15 +1):
    print(rnr_balance.get_balance_health(level), end=', ')
  print()

def goblin_battle_oh_ha_ha():
  
  goblin_stats = {
    'name': "Goblin",
    'health': 50,
    'evasion': 12,
    'stat_bonus': 1,
    'spell_power': 12,
    'actions_per_turn': 1,
    'moveset': [
      # It is understood that each attack cost 1, but attacks_made can be used to make a multiplier.
      {
        'attacks_made': 1,
        'limit': 1,
        'name': 'pokey-stick',
        'damage': '1d4',
        'description': 'Stick them with the pointy end!',
        'effects': None
      }
    ]
  }
  gobbo = rnr_balance.creature.dict_constructor(goblin_stats)
  print(gobbo.name)
  print(rnr_balance.creature_survivability_at_level(gobbo, 1, 1))
  print(rnr_balance.find_ideal_creature_level(gobbo, 'minion', 1, False))
  print(gobbo.greedy_turn_damage(5, 5))

if __name__ == '__main__':
  print('Parser booting...')

  #print_balance_values()
  goblin_battle_oh_ha_ha()
  
  parser=argparse.ArgumentParser(description="Utility to check spell balance and optionally publish spells.")
  parser.add_argument('--loud', action='store_true',help="Write to command line.")
  args = parser.parse_args()

  schema = dict()
  spellbooks = dict()

  try:
    with open(SCHEMA_PATH, 'r') as schema_file:
      schema = json.load(schema_file)
  except FileNotFoundError:
    print(f"ERROR, could not find {SCHEMA_PATH}")
    sys.exit(1)
  except json.JSONDecodeError:
    print(f"ERROR: Trouble loading {SCHEMA_PATH}")
    traceback.print_exc()
    sys.exit(1)
  except Exception as e:
    traceback.traceback.print_exc()
    sys.exit(1)

  print("Schema loaded...")

  try:
    with open(SPELLBOOK_PATH, 'r') as spellbook_file:
      spellbooks = yaml.load(spellbook_file, Loader=Loader)
  except yaml.YAMLError as exc:
    if hasattr(exc, 'problem_mark'):
      print(f"ERROR: Could not load spells.yml. Line: {exc.problem_mark.line} Column: {exc.problem_mark.column}")
      sys.exit(1)
  except Exception:
    traceback.print_exc()
    sys.exit(1)

  print('Spellbooks loaded from file...')
  print()

  required_spells = {'tier_1': 27, 'tier_2': 17, 'tier_3': 8}

  all_spells = list()
  with open('spell_output.md', 'w') as outfile:
    all_types = set()
    damage_spells = dict()
    for spellbook_name, tiers in spellbooks.items():
      count_spells_in_spellbook = 0
      print(f"Checking: {spellbook_name}")
      num_spells = 0
      spells_by_type = dict()
      for tier, tier_spells in tiers.items():

        if tier not in damage_spells:
          damage_spells[tier] = dict()

        count_spells_in_tier = 0
        atk = 0
        for spell, spell_def in tier_spells.items():
          count_spells_in_spellbook += 1
          count_spells_in_tier += 1
          try:
            jsonschema.validate(spell_def, schema=schema)
            spell = rnr_spell.dict_constructor(spell, spell_def)
            all_spells.append(spell)
            spell_text = spell.get_markdown()
            outfile.write(f"{spell_text}  \n")
            spell.validate_type(loud=True)

            spells_by_type[spell.type] = spells_by_type.get(spell.type, 0) +1
            all_types.add(spell.type)
            
            if 'damage' in spell.type:
              if not spell.cost in damage_spells[tier]:
                damage_spells[tier][spell.cost] = list()

              damage_spells[tier][spell.cost].append(spell)

            if args.loud:
              print(f"{spell_text}  \n")
          except jsonschema.exceptions.ValidationError as e:
            print(f"ERROR: {e.schema_path}, {e.message}")
            sys.exit(1)
        print(f"{count_spells_in_tier} / {required_spells[tier.lower()]}")
      print(count_spells_in_spellbook)
      total = 0

      for spell_type, count in spells_by_type.items():
        print(f"  {spell_type}: {count}")
        total += count 
      print(f"  TOTAL: {total}")
    for t in sorted(all_types):
      print(t)

    loud = False

    print('\nDamage Check!')
    for tier, cost_list in damage_spells.items():
      for cost, spell_list in sorted(cost_list.items()):
        avg_dmg = statistics.mean(list(obj.estimated_damage(tier)[0] for obj in spell_list))
        stdev_dmg = statistics.stdev([obj.estimated_damage(tier)[0] for obj in spell_list]) 

        print(f"{tier} Cost: {cost} -- Count: {len(spell_list)}, Mean: {round(avg_dmg, 2)}, Stdev: {round(stdev_dmg,2)}")
        for spell in sorted(
          spell_list, 
          key=lambda spell: (spell.estimated_damage(tier), spell.get_max_condition_value()),
          reverse=True
        ):
          expected_damage = rnr_balance.get_expected_damage_at_tier(tier.lower(), False, 'magic', cost, spell.is_aoe)
          warning = ""
          estimated_damage = spell.estimated_damage(tier)[0]
          if estimated_damage > (avg_dmg + (2*stdev_dmg)) or estimated_damage > expected_damage * 1.25:
              warning = f"WARNING - HIGH DAMAGE {estimated_damage} vs {expected_damage}"
          elif estimated_damage < (avg_dmg - (2*stdev_dmg)) or estimated_damage < expected_damage * 0.75:
              warning = "WARNING - LOW DAMAGE"

          if loud or warning != '':
            print(f"  {spell.name}: {spell.estimated_damage(tier)} {warning}, {spell.get_condition_names()}")

    summoned_creature_check(all_spells)
