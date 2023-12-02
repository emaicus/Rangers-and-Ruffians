import json
import traceback
from pathlib import Path
#from .rnr_balance import *

CODE_DIRECTORY = Path(__file__).resolve()
BASE_DIRECTORY = CODE_DIRECTORY.parent.parent.parent
INSTALL_DIRECTORY = BASE_DIRECTORY.joinpath('INSTALLED_DATA')

EFFECTS = None

class StatusEffect():
  def __init__(self, name):
    global EFFECTS
    if EFFECTS is None:
      try:
        print('loading')
        with open(INSTALL_DIRECTORY.joinpath('status_effects.json'), 'r') as infile:
          EFFECTS = json.load(infile)
        print('loaded')
      except Exception:
        print('Status Effects file not found.')
        print(traceback.format_exc())


    value = seek_effect(name)


    self.name = name
    self.balance = value['balance'] 
    self.numeric_balance = 1 #int(rnr_balance.get_balance_value('effect_ranking')[balance])
    self.about = value['about']

  def get_markdown(self):
    return self.about

def seek_effect(name):
  global EFFECTS
  if name == 'custom':
    return {
      'name': 'custom',
      'balance': 'good',
      'about': ''
    }

  for effect in EFFECTS:
    if effect['name'].lower() == name:
      return effect 
  
  raise ValueError(f"Effect with name '{name}' not found.")

class RnRAbility():
  def __init__(self, ability_data):

    self.name = ability_data['name']
    self.type = ability_data['type']
    self.cost = ability_data['cost']

    # Duration is either an integer or a string
    duration = ability_data['duration']
    self.duration = duration if isinstance(duration, int) else duration.title()

    # Casting time is either an integer or a string
    casting_time = ability_data.get('casting_time', None) 
    self.casting_time = casting_time if casting_time is None or isinstance(casting_time, int) else casting_time.title()
  
    # Range is either an integer or a string
    spell_range = ability_data['range']
    self.range = spell_range if isinstance(spell_range, int) else spell_range.title()

    # Determine if the spell is aoe based on radius and type.
    self.radius = ability_data.get('radius', None)
    self.is_aoe = self.radius is not None and self.type not in ['summoning', 'transformation']

    self.description = ability_data['description']
    
    # Autocomplete requirements
    requirements = ability_data.get('requirements', dict())
    self.requirements = dict()
    self.requirements['movement'] = requirements.get('movement', False)
    self.requirements['verbal'] = requirements.get('verbal', False)
    self.requirements['components'] = requirements.get('components', list())

    # Fill in empty damage variables.
    self.damage = ability_data.get('damage_scaling', None)
    if self.damage is not None:
      if 'multi_attack' not in self.damage:
        self.damage['multi_attack'] = 1
      if 'scaled_by' not in self.damage:
        self.damage['scaled_by'] = dict()
      if 'damage_shape' in self.damage:
        if self.damage['damage_shape'] in ['cone', 'line', 'chain']:
          self.is_aoe = True
      self.damage['scaled_by']['weapon'] = self.damage['scaled_by'].get('weapon', True)
      self.damage['scaled_by']['stat'] = self.damage['scaled_by'].get('stat', True)

    self.upcast = ability_data.get('upcast', None)
    self.summoned_creature = ability_data.get('summoned_creature', None)
    
    # Fill in 'Action' when action_type is not specified.
    self.action_type = ability_data.get('action_type', "Action")
    
    # If there are effects, construct any required conditions
    self.effect = ability_data.get('effect', None)
    if self.effect is not None: 
      conditions = self.effect['conditions']  
      my_conditions = list()
      for condition in conditions:
        my_conditions.append(StatusEffect(condition))
      self.effect['conditions'] = my_conditions
    
    self.options = ability_data.get('options', None)
    self.spellbook = 'unknown'

  #simple constructor
  @classmethod
  def dict_constructor(cls, spell_name, spellbook, dict_data):
    dict_data = dict_data
    
    name = spell_name
    spellbook = spellbook
    spell_type = dict_data['type']
    cost = dict_data['cost']
    duration = dict_data['duration']
    casting_time = dict_data.get('casting_time', None) 
    spell_range = dict_data['range']
    radius = dict_data.get('radius', None)
    description = dict_data['description']
    requirements = dict_data.get('requirements', dict())
    damage = dict_data.get('damage_scaling', None)
    upcast = dict_data.get('upcast', None)
    summoned_creature = dict_data.get('summoned_creature', None)
    action_type = dict_data.get('action_type', "Action")
    effect = dict_data.get('effect', None)
    options = dict_data.get('options', None)

    return cls(name, spellbook, spell_type, cost, duration, casting_time, spell_range, radius, description, requirements, damage, upcast,
               summoned_creature, action_type, effect, options, dict_data=dict_data)

  def get_markdown(self):

    spell_text = f"### {self.name}\n"
    spell_text += f"__{self.type.title()}{', ' + self.action_type if self.action_type is not None and self.action_type not in ['Action', 'Inherited', 'modifies_ability'] else ''}__  \n"
    
    # Determine range display, don't print 'inherited'
    range_unit = 'Feet' if isinstance(self.range, int) else ''
    range_string =  f' __Range:__ {self.range} {range_unit}' if self.range != 'Inherited' else ''
    
    # Determine action point display. Properly print 'Action Point' or 'Action Points'
    cost_unit = 'Action Point' if self.cost == 1 else 'Action Points'
    cost_str = f"{self.cost} {cost_unit}" if self.cost != 0 else "None"

    # Determine distance string. Properly print 'Turns' if a number of turns was specified. Don't print inherited.
    duration_unit = ''
    if isinstance(self.duration, int):
      duration_unit = 'Turn' if self.duration == 1 else 'Turns'

    duration_str = f' __Duration:__ {self.duration} {duration_unit}' if self.duration != 'Inherited' else ''
    
    # Build the next line of the spell_text.
    spell_text += f"__Cost:__ {cost_str}{duration_str}{range_string}  \n"

    if self.radius is not None or self.casting_time is not None:
      spell_text += f"__Casting Time:__ {self.casting_time} " if self.casting_time is not None else ""
      spell_text += f"__Radius:__ {self.radius}{' ft.' if isinstance(self.radius, int) else ''} " if self.radius is not None else ""
      
      spell_text += "  \n"

    requirements_arr = [key.lower()[0] for key, value in self.requirements.items() if value and key in ('movement', 'verbal')]
    requirements_arr += self.requirements['components']

    if len(requirements_arr) > 0:
      spell_text +=f"__Components:__ _{', '.join(requirements_arr)}_  \n"


    spell_text += self.description
    condition_list = list()

    if self.effect is not None:
      condition_list = self.effect['conditions']

      spell_text += f" {self.effect['description']} {self.effect['save'] if self.effect['save'] is not None else ''} "

      if 'options' in self.effect:
        spell_text += "  \n"
        for option in self.effect['options']:
          spell_text += f"* {option}  \n"
        spell_text += '\n'
  
    for condition in condition_list:
      spell_text += f"{condition.get_markdown()} "

    spell_text += f" {self.upcast if self.upcast is not None else ''} "
    spell_text += '  \n'
    
    
    if self.options is not None:
      for options in self.options:
        spell_text += f"* {options}  \n"

    if not self.damage is None:
      # Check weapon scaling. Add a special line if this spell doesn't scale.
      if 'scaled_by' in self.damage:
        weapon_scaling = self.damage['scaled_by'].get('weapon', False)
        if weapon_scaling == False:
          spell_text += '__This spell is not affected by Focus damage bonuses.__  \n'
  
      i = 0
      for tier in ['tier_1', 'tier_2', 'tier_3']:
        if tier in self.damage:
          dmg_str = 'Healing' if self.damage['damage_type'] == 'healing' else 'Damage'
          spell_text += f"__{tier.replace('_', ' ').title()} {dmg_str}:__ {self.damage[tier]} {self.damage['damage_type'].title() if dmg_str != 'Healing' else ''}   \n"
      spell_text += '\n'

      
    
    if self.summoned_creature is not None:
      if isinstance(self.summoned_creature, str):
        spell_text += f"_Summoned Creature:_ {self.summoned_creature}  \n"
      else:
        #spell_text += f"_Summoned Creature:_  \n"
        for key, val in self.summoned_creature.items():
          spell_text += f"__{key.replace('_', ' ').title() + ' ' if not 'all' in key.lower() else ''}Summon:__ {val}  \n"
    
    spell_text += "  \n"



    return spell_text

  def validate_type(self, loud=False):
    if loud and self.intuited_type() != self.type:
      print(f'{self.name}: intuited type {self.intuited_type()} != {self.type}')
    
    return self.intuited_type() == self.type

  def intuited_type(self):
    intuited_type = 'utility'

    if self.effect is not None:
      if self.effect['type'] == 'debuff':
        intuited_type = "debuff"
      if self.effect['type'] == "buff":
        intuited_type = "buff"
    
    if self.damage is not None:
      if self.damage['damage_type'] == "healing":
        intuited_type = "healing"
      elif self.damage['multi_attack'] != 1:
        intuited_type = "multi-attack damage"
      else: 
        intuited_type = 'damage'
    
    if self.summoned_creature is not None:
      if self.range != 'self' and self.effect is None:
        intuited_type = 'summoning'
      else:
        intuited_type = 'transformation'

    if self.is_aoe and intuited_type != 'utility':
      intuited_type = "aoe " + intuited_type

    return intuited_type
  
  def estimated_damage(self, tier, single_target=False):
    pass
    # tier = tier.lower()

    # if self.damage is None:
    #   return 0, 0, 0, 0, 0, 0
    
    # if tier not in self.damage:
    #   return 0, 0, 0, 0, 0, 0
    # aoe = 2 if self.is_aoe else 1
    # max_damage = 0
    # avg_damage = 0
    # for attack in range(self.damage['multi_attack']):
    #   single_attack_avg_damage = 0
    #   single_attack_max_damage = 0
    #   if 'd' not in self.damage[tier]:
    #     single_attack_avg_damage += int(self.damage[tier])
    #     single_attack_max_damage += int(self.damage[tier])
    #   else:
    #     die, sides = map(int, self.damage[tier].split('d'))
    #     single_attack_avg_damage += rnr_balance.die_half(die, sides)
    #     single_attack_max_damage += die * sides
           
    #   focus = rnr_balance.get_balance_weapon_at_tier(tier, False, 'magic')
      
    #   inner_fire = rnr_balance.get_balance_value('balance_stat_value')[tier]['max'] if self.damage['scaled_by']['stat'] else 0
    #   single_attack_avg_damage += focus.avg_dmg() + inner_fire
    #   single_attack_max_damage += focus.max_dmg() + inner_fire

    #   avg_damage += single_attack_avg_damage * aoe      
    #   max_damage += single_attack_max_damage * aoe

    # return avg_damage, max_damage, single_attack_avg_damage, self.type, self.cost, self.damage['damage_type']
  
  def get_max_condition_value(self):
    if self.effect is None:
      return -999

    return max([condition.numeric_balance for condition in self.effect['conditions']])
  
  def get_condition_names(self):
    if self.effect is None:
      return list()

    return [condition.name for condition in self.effect['conditions']]






