from pathlib import Path
from .RnRAbility import RnRAbility

class RnRRace():
  #Base constructor
  def __init__(self, race_data):
    self.name = race_data['name']
    self.health_dice = race_data['health_dice']
    self.base_movement = race_data['base_movement']
    self.handbook = race_data['handbook']
    self.parent_class = race_data.get('parent_class', self.name)
    self.art_data = None

    self.abilities = list()
    for ability in race_data['abilities']:
      self.abilities.append(RnRAbility(ability))

  
  
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
  

  def get_markdown(self, level=None, art_data=None, printable=False):
    subsection_level = None if level is None else level + 1
    ability_level = None if level is None else level + 2
    race_text = ''

    race_text += f'<div class="printable-content" id="printable-{self.name.lower()}">  \n' if printable else ''
    race_text += f'__{self.name}__  \n' if level == None else '#' * level + f' {self.name}  \n'
    race_text += f'<button onclick="printContent(\'printable-{self.name.lower()}\')">Print {self.name}</button>  \n  \n' if printable else ''

    if art_data is not None:
      race_text += f"<img src='{art_data['path']}' class=\"raceClassImage\" />\n\n"
      race_text += f"<span class=\"attribution\">{art_data['attribution']}</span>"

    for para in self.handbook['introduction']:
      race_text += f"{para}  \n  \n"
    race_text += '  \n'

    race_text += f"{'#' * subsection_level} {self.handbook['you_may']['title']}  \n"
    for option in self.handbook['you_may']['options']:
      race_text += f"* {option}  \n"
    race_text += '  \n'
    
    race_text += f"{'#' * subsection_level} {self.handbook['assumptions']['title']}  \n"
    for option in self.handbook['assumptions']['options']:
      race_text += f"* {option}  \n"
    race_text += '  \n'

    race_text += f"{'#' * subsection_level} Physical Features  \n"
    for feature in self.handbook['looks']:
      title = feature['title']
      options = feature['options']
      race_text += f"* __{title}__ {options}  \n"
    race_text += '  \n'

    race_text += f"{'#' * subsection_level} Stats and Abilities  \n"
    race_text += f'__Health Dice:__ {self.health_dice} __Movement:__ {self.base_movement}ft   \n'
    for ability in self.abilities:
      race_text += f'<div class="rnr-ability" id="ability-{ability.name.lower()}">  \n' if printable else ''
      race_text += ability.get_markdown(ability_level) + '   \n'
      race_text += f'</div>  \n' if printable else ''

    race_text += '</div>  \n' if printable else ''
        
    return race_text