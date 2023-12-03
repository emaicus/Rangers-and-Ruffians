from pathlib import Path
from .RnRAbility import RnRAbility

class RnRRace():
  #Base constructor
  def __init__(self, race_data):
    self.name = race_data['name']
    self.health_dice = race_data['health_dice']
    self.base_movement = race_data['base_movement']
    self.handbook = race_data['handbook']
    self.is_a = race_data.get('is_a', None)

    self.abilities = list()
    # for ability in race_data['abilities']:
    #   self.abilities.append(RnRAbility(ability))

  
  
  # def serialize(self, rnr_game : RangersAndRuffians, male=False, skip_art=False):
  #   global GLOBAL_SITE_ART_PATH

  #   underscore_char = ' '
  #   serial = dict()
  #   serial['name'] = self.name
  #   serial['health_dice_bonus'] = self.health_dice_bonus
  #   serial['base_movement'] = self.base_movement
  #   #serial['abilities'] = self.abilities
  #   serial['handbook'] = self.handbook
  #   serial['is_a'] = self.is_a

  #   if not skip_art:
  #     gender_string = 'male' if male else 'female'
  #     absolute_art_folder = Path(GLOBAL_SITE_ART_PATH, 'race')
  #     relative_art_folder = Path('static', 'images', 'race')

  #     image_path, attribution = core.get_gendered_art(relative_art_folder, absolute_art_folder, self.name.replace(' ','_').lower(), male)

  #     img_name = image_path.split('/')[-1].split('.')[0]
  #     serial['rights'] = rnr_game.annotations.get(f'{img_name}_{gender_string}', None)
  #     serial["path_to_image"] = image_path

  #   serial['health_die_pieces'] = self.health_die_pieces
  #   return serial
  

  def get_markdown(self):
    race_text = f'## {self.name}  \n'
    race_text += f'__Health Dice Bonus:__ {self.health_dice_bonus} __Movement:__ {self.base_movement}ft  \n'
    for ability_obj in self.abilities:
      race_text += ability_obj.get_markdown() + '  /n'
        
    return race_text