'''
RNR class object.
'''
import json

class rnr_class():
  ''' Takes in classname and json object, instantiates class.'''
  def __init__(self, rnr_classname, rnr_classdata):

    self.name = rnr_classname
    self.stat_recommendation = rnr_classdata['recommended_stats']
    self.handbook = rnr_classdata.get('handbook', {})
    self.health_dice = rnr_classdata['health_dice']
    self.abilities = rnr_classdata['abilities']
    self.expertise = rnr_classdata['expertise']
  
  
  def get_markdown(self):
    class_text = f'# {self.name}  \n'
    class_text += "## Recommended Stats  \n"
    for stat in ["Strength", "Dexterity", "Intelligence","Inner_Fire",  "Perception", "Charisma"]:
      class_text += f"*  __{stat.replace('_', ' ')}:__ {self.stat_recommendation[stat]}  \n"

    class_text += "  \n"

    class_text += "## Health and Expertise  \n"
    class_text += f"{self.name}s use {self.health_dice} as their class health dice. "
    class_text += f"{self.expertise}  In such casess, you may add your expertise bonus as well as any relevant stats to you ability checks or saves.\n"

    class_text += "## Abilities  \n"
    for ability_obj in sorted(self.abilities, key=lambda d: d['name']):
        ability_name = ability_obj['name']
        cost = ability_obj.get('cost', None)
        action_type = ability_obj.get('action_type', None)
        damage_scaling = ability_obj.get('damage_scaling', None)
        condition_name = ability_obj.get('condition', None)
        description = ability_obj.get('description', None)
        options = ability_obj.get('options', list())

        class_text += f'### {ability_name}  \n'

        if cost is not None and cost != 0:
          class_text += f'__Cost:__ {cost}. '
        if action_type is not None:
          class_text += f'__{action_type}__'
        class_text += "  \n"

        class_text += f'{description}  \n'

        for option in options:
          class_text += f"*  {option}  \n"
        
        if len(options) > 0:
          class_text += "  \n"

        if damage_scaling is not None:
          class_text += f'This ability deals {damage_scaling["tier_1"]} damage at character levels 0-4, {damage_scaling["tier_2"]} at levels 5-9, and {damage_scaling["tier_3"]} at levels 10-15.'
        class_text += "  \n"
    return class_text