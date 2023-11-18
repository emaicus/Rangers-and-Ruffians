'''
RNR race object.
'''
import json

class rnr_race():
  #Base constructor
  def __init__(self, name, health_dice_bonus, base_movement, abilities, handbook, is_a):
    self.name = name
    self.health_dice_bonus =  health_dice_bonus
    self.base_movement =  base_movement
    self.abilities = abilities
    self.handbook = handbook
    self.is_a = is_a if is_a is not None else name  

  #simple constructor
  @classmethod
  def basic_constructor(cls, race_name, race_data):
    return cls(race_name, race_data['health_dice_bonus'], race_data['base_movement'], 
                race_data['abilities'], race_data['handbook'], race_data.get('is_a', None))


  def get_markdown(self):
    race_text = f'## {self.name}  \n'
    race_text += f'__Health Dice Bonus:__ {self.health_dice_bonus} __Movement:__ {self.base_movement}ft  \n'
    for ability_obj in self.abilities:
        ability_name = ability_obj['name']
        cost = ability_obj.get('cost', None)
        damage_scaling = ability_obj.get('damage_scaling', None)
        condition_name = ability_obj.get('condition', None)
        description = ability_obj.get('description', None)

        race_text += f'* __{ability_name}__: '

        if cost is not None and cost != 0:
          race_text += f'(_Cost:_ {cost}) '

        race_text += f'{description} '

        if damage_scaling is not None:
          race_text += f'This ability deals {damage_scaling["tier_1"]} damage at character levels 0-4, {damage_scaling["tier_2"]} at levels 5-9, and {damage_scaling["tier_3"]} at levels 10-15.'
        race_text += "  \n"
    return race_text

        # if condition_name is not None:
        #   race_text += f'{condition_name}'