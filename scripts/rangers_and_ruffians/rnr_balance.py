import yaml
import os
import sys
import traceback
from pathlib import Path
import math

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

'''
RNR Spell object.
'''

BALANCE_DATA = None
BASE_DIRECTORY = Path(__file__).resolve().parent
DATA_PATH = os.path.join(BASE_DIRECTORY, "balance_values.yml")

try:
  with open(DATA_PATH, 'r') as condition_file:
    BALANCE_DATA = yaml.load(condition_file, Loader=Loader)
except yaml.YAMLError as exc:
  if hasattr(exc, 'problem_mark'):
    print(f"ERROR: Could not load status_effects.yml. Line: {exc.problem_mark.line} Column: {exc.problem_mark.column}")
    traceback.print_exc()
    sys.exit(1)
except Exception:
  traceback.print_exc()
  sys.exit(1)

class rnr_weapon():
  def __init__(self, primary_die, secondary_die):
    self.primary_count, self.primary_sides = convert_dice(primary_die)
    self.secondary_count, self.secondary_sides = convert_dice(secondary_die)
  
  def avg_dmg(self):
     return die_half(self.primary_count, self.primary_sides) + die_half(self.secondary_count, self.secondary_sides)

  def max_dmg(self):
    return (self.primary_count * self.primary_sides) + (self.secondary_count * self.secondary_sides)

class rnr_creature_move():
  def __init__(self, name, damage, description, effects, attacks_made, limit, recharge):
    self.name = name
    self.damage = damage
    self.description = description
    self.effects = effects
    self.attacks_made = attacks_made
    self.limit = limit
    self.recharge = recharge 
  
  @classmethod
  def dict_constructor(cls, dict_data):
    name = dict_data['name']
    damage = dict_data['damage']
    description = dict_data['description']
    effects = dict_data.get('effects', None)
    attacks_made = dict_data.get('attacks_made', 1)
    limit = dict_data.get('limit', 100)
    recharge = dict_data.get('recharge', False)

    return cls(name, damage, description, effects, attacks_made, limit, recharge)

  def get_damage(self, stat_bonus):
    num_dmg = die_half(*convert_dice(self.damage)) + stat_bonus
    return self.attacks_made * num_dmg

class creature():
  def __init__(self, name, health, evasion, stat_bonus, spell_power, actions_per_turn, moveset):
    self.name = name
    self.health = health 
    self.evasion = evasion
    self.stat_bonus = stat_bonus
    self.actions_per_turn = actions_per_turn
    self.spell_power = spell_power
    self.moveset = list()

    for move in moveset:
      self.moveset.append(rnr_creature_move.dict_constructor(move))

  @classmethod
  def dict_constructor(cls, dict_data):
    dict_data = dict_data
    
    name = dict_data['name']
    health = dict_data['health']
    evasion = dict_data['evasion']
    stat_bonus = dict_data['stat_bonus']
    spell_power = dict_data['spell_power']
    actions_per_turn = dict_data['actions_per_turn']
    moveset = dict_data['moveset']

    return cls(name, health, evasion, stat_bonus, spell_power, actions_per_turn, moveset)
  
  # Return the average turn damage dealt by the creature if it takes the greediest strategy.
  def greedy_turn_damage(self, enemy_evasion, enemy_spell_power):
    actions_remaining = self.actions_per_turn
    total_damage = 0
    ranked_moves = sorted(self.moveset, key=lambda x:x.get_damage(self.stat_bonus), reverse=True)

    for move in ranked_moves:
      print(f"Considering {move.name}")
      # Have we taken the required moves?
      if actions_remaining <= 0:
        print('No actions remaining. Breaking.')
        break

      # If this move is recharge or isn't allowed, skip it.
      if move.recharge or move.limit <= 0:
        print('This move has recharge or has a move limit of zero. Skipping.')
        continue
      
      # Take this action as many times as we can (greedy)
      times_taken = min(move.limit, actions_remaining)
      print(f'Taking the move {times_taken} times')
      total_damage += times_taken * move.get_damage(self.stat_bonus)
      actions_remaining -= times_taken

    return total_damage

  # The number of turns survived under an amount of damage with glancing blows
  def survivability_vs_damage(self, damage, hit_bonus, include_crits=False):
    damage_taken = glancing_blow(damage, self.evasion, hit_bonus, include_crits)
    return self.health / damage_taken

def get_balance_value(key):
  global BALANCE_DATA
  if key in BALANCE_DATA:
    return BALANCE_DATA[key]
  else:
    raise ValueError(f'Invalid balance value: {key}')

def get_balance_level(tier, is_min):
  # Determine if we're dealing with early or late play within a tier
  period = 'min' if is_min else 'max'
  return get_balance_value('tier_level_definitions')[tier][period]

def get_tier_from_level(level):
  for tier in ['tier_1', 'tier_2', 'tier_3']:
    min_level = get_balance_level(tier, True)
    max_level = get_balance_level(tier, False)
    if level >= min_level and level <= max_level:
      return tier
  raise ValueError(f'Invalid level: {level}')

# This function is useful for quick printing of min and max values
def get_tier_level_array():
  min_and_max_array = list()
  for _, min_and_max in get_balance_value('tier_level_definitions').items():
    min_and_max_array.append(min_and_max['min'])
    min_and_max_array.append(min_and_max['max'])
  return min_and_max_array

# For use only with values with a min and max.
def _interpolate(query_string, level):
  # Get the tier we're in so that we can get balance values  
  tier = get_tier_from_level(level)
  # Find the maximum and minimum levels in our tier
  min_level = get_balance_level(tier, True)
  max_level = get_balance_level(tier, False)
  # Compute how far through the tier we are.
  level_fraction = (level - min_level) / (max_level - min_level)
  # Get the min and max balance values for the tier
  min_value = get_balance_value(query_string)[tier]['min']
  max_value = get_balance_value(query_string)[tier]['max']

  # Return the interpolated value. 
  interpolated_value = math.ceil(min_value + ((max_value - min_value) * level_fraction))
  return interpolated_value

def get_balance_weapon_at_tier(tier: str, is_min: bool, type_of_damage: str):
  if type_of_damage not in ['light', 'heavy', 'magic']:
     raise ValueError(f'Invalid value: {type_of_damage}')
  
  period = 'min' if is_min else 'max'
  # Load the appropriate weapon -- heavy or light
  if type_of_damage == 'light':
     weapon_str = 'standard_weapon_dmg_dice'
  elif type_of_damage == 'heavy':
    weapon_str = 'heavy_weapon_dmg_dice'
  else: 
    weapon_str = 'focus_dmg'
  
  weapon_primary = get_balance_value(weapon_str)[tier][period]
  weapon_secondary  = '0d0' if type_of_damage == 'magic' else get_balance_value('weapon_effect_dice')[tier][period]
  return rnr_weapon(weapon_primary, weapon_secondary)

def get_balance_ap_damage_at_tier(tier, type_of_damage, ap_spent, is_aoe):
  if type_of_damage not in ['light', 'heavy', 'magic']:
     raise ValueError(f'Invalid value: {type_of_damage}')

  magic_string = '_ap_aoe_spell_dice' if is_aoe else '_ap_spell_dice'

  ap_string = f"{ap_spent}{magic_string}" if type_of_damage == 'magic' else 'ap_dmg'
  base_ap_dmg = get_balance_value(ap_string)[tier]
  ap_num, ap_sides = convert_dice(base_ap_dmg)
  ap_damage = (die_half(ap_num, ap_sides))

  # Non magic AP Damage is multiplicative. ap_spent should be 0, 1, or 2.
  if type_of_damage != 'magic':
    ap_damage *= ap_spent
  
  return ap_damage

def get_expected_damage_at_tier(tier, is_min, type_of_damage, ap_spent, is_aoe):
  if type_of_damage not in ['light', 'heavy', 'magic']:
     raise ValueError(f'Invalid value: {type_of_damage}')
  
  period = 'min' if is_min else 'max'

  # The avg stat value varies within a tier.
  stat_value = get_balance_value('balance_stat_value')[tier][period]
  
  
  # Get the weapon for this tier
  weapon = get_balance_weapon_at_tier(tier, is_min, type_of_damage)
  
  # Get the ability/spell damage for this tier
  ap_dmg = get_balance_ap_damage_at_tier(tier, type_of_damage, ap_spent, is_aoe)

  # Conditional damage is 1d6 x the number of conditional damage sources.
  conditional_damage = 0 if type_of_damage == 'magic' else die_half(1, 6) * get_balance_value('balance_conditional_damage_sources')[tier][period]

  # print(weapon.avg_dmg())
  # print(stat_value)
  # print(ap_damage)
  # print(conditional_damage)
  aoe_scaler = 2 if is_aoe else 1
  return (weapon.avg_dmg() + stat_value + ap_dmg + conditional_damage) * aoe_scaler
  
def get_expected_damage(level, type_of_damage, ap_spent, is_aoe):
  # Get the tier we're in so that we can get balance values  
  tier = get_tier_from_level(level)
  # Find the maximum and minimum levels in our tier
  min_level = get_balance_level(tier, True)
  max_level = get_balance_level(tier, False)
  # Compute how far through the tier we are.
  level_fraction = (level - min_level) / (max_level - min_level)
  # Get the min and max balance values for the tier
  min_value = get_expected_damage_at_tier(tier, True, type_of_damage, ap_spent, is_aoe)
  max_value = get_expected_damage_at_tier(tier, False, type_of_damage, ap_spent, is_aoe)

  # Return the interpolated value. 
  interpolated_damage = math.ceil(min_value + ((max_value - min_value) * level_fraction))
  return interpolated_damage

def avg_turn_dmg(level, type_of_damage, ap_spent, is_aoe):
  if ap_spent not in range(0,4):
    raise ValueError(f'Invalid value: {ap_spent}')

  zero_ap_dmg = get_expected_damage(level, type_of_damage, 0, is_aoe)
  one_ap_dmg = get_expected_damage(level, type_of_damage, 1, is_aoe)
  two_ap_dmg = get_expected_damage(level, type_of_damage, 2, is_aoe)


  if ap_spent == 0:
    return zero_ap_dmg + zero_ap_dmg
  elif ap_spent == 1:
     return one_ap_dmg + zero_ap_dmg
  elif ap_spent == 2:
     return two_ap_dmg + zero_ap_dmg
  elif level == 'tier_3' and type_of_damage == 'magic' and ap_spent == 3:
     nova_dmg = get_expected_damage(level, type_of_damage, 3, is_aoe)
     return nova_dmg + zero_ap_dmg
  else: #ap_spent == 3
     return two_ap_dmg + one_ap_dmg
    
def get_balance_dmg(level, ap_spent):
   light = avg_turn_dmg(level, 'light', ap_spent, False)
   heavy = avg_turn_dmg(level, 'heavy', ap_spent, False)
   magic = avg_turn_dmg(level, 'magic', ap_spent, False)

   return round((light + heavy + magic) / 3, 2)

def get_balance_armor(level, is_heavy, has_shield):
  # Heavy armor and shields both grant a static bonus, applied based on is_heavy and has_shield.
  heavy_bonus = get_balance_value('heavy_armor_bonus') if is_heavy else 0
  shield = get_balance_value('shield_bonus') if has_shield else 0
  # We interpolate the light armor value at this point in the tier, then apply the bonuses
  interpolated_armor = _interpolate('light_armor', level)
  return interpolated_armor + heavy_bonus + shield

def get_balance_evasion(level):
  base_evasion = get_balance_value('base_evasion')
  
  # Take half the shield bonus for balance reasons
  shield_bonus = get_balance_value('shield_bonus') / 2
  # Grab the interpolated values for both heavy and light armor, then take the average.
  light_armor = base_evasion + get_balance_armor(level, False, False) + shield_bonus
  heavy_armor = base_evasion + get_balance_armor(level, True, False) + shield_bonus
  return math.ceil((light_armor + heavy_armor)/2)

def get_balance_health(level):
  # Just return the interpolated player health value.
  return math.ceil(_interpolate('balance_player_health', level))

def get_balance_stat_value(level):
  return math.ceil(_interpolate('balance_stat_value', level))

def glancing_blow(damage, enemy_evasion, hit_bonus, include_crits):
  # Because RnR evasion is 'meet or exceed' we have to add +1 to the hit fraction.
  # For example, if an enemy has 10 evasion, there are actually 11 ways to hit them: 10, 11, 12, etc.
  hit_frac = (enemy_evasion - hit_bonus + 1) / 20
  # Clamp the % hit between 0 and 100%
  hit_frac = min(max(hit_frac, 1), 0)
  miss_frac = 1 - hit_frac 

  if not include_crits:
    return (hit_frac * damage) + (miss_frac * (damage / 2))
  else:
    # Critical hits ALWAYS hit on a nat 20 (5% chance), even if hit_frac is 0.
    crit_chance = 0.05
    # If we had a > 5% chance of hitting, 5% of it is converted to crit.
    # If it was impossible to hit, 5% of the impossibility is converted to a crit.
    if hit_frac != 0:
      hit_frac -= hit_frac
    else: 
      miss_frac -= crit_chance
    return (crit_chance * (damage * 2)) + (hit_frac * damage) + (miss_frac * (damage / 2))
  

# A definition of challenge rating: 
# core_survivability(level): For how many rounds can the creature survive against a party of four players at a given level.
# core_survivability_level(creature): Given a creature, which level player can kill it within tolerances? Find the closest.
# core_damage(level): How many rounds does it take a creature to defeat a party of four players at a given level?
# core_damage_level(creature): Give a creature, which level player can it kill within tolerances? Find the closest.

def creature_survivability_at_level(creature: creature, level: int, ap_spent: int, include_crits=False):
  damage = get_balance_dmg(level, ap_spent)
  hit_bonus = get_balance_stat_value(level)
  return creature.survivability_vs_damage(damage, hit_bonus, include_crits)

#def creature_damage_level(creature: creature, level: int, )

def find_ideal_creature_level(creature: creature, intended_creature_type: str, ap_spent: int, include_crits=False):
  if not intended_creature_type in ['minion', 'heavy', 'villain']:
    raise ValueError(f'Invalid balance value: {intended_creature_type}')
  
  intended_survivabilty = get_balance_value('creature_survivability')[intended_creature_type]

  best_delta = math.inf 
  best_level = -1
  closest_survivability = math.inf
  for level in range(0,16):
    survivability = creature_survivability_at_level(creature, level, ap_spent, include_crits)
    delta = abs(intended_survivabilty - survivability)
    if delta < best_delta:
      best_delta = delta
      best_level = level
      closest_survivability = survivability
  return best_level, closest_survivability

def survivability_in_turns(damage, health):
   return health / damage

def convert_dice(dice):
   num, sides = dice.split('d')
   return float(num), float(sides)

def die_half(num, sides):
  return num * ((sides / 2) + .5)