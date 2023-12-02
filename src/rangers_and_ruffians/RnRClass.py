from pathlib import Path
from .RnRAbility import RnRAbility

class RnRClass():
  ''' Takes in classname and json object, instantiates class.'''
  def __init__(self, rnr_classdata):

    self.name = rnr_classdata['name']
    self.stat_recommendation = rnr_classdata['recommended_stats']
    self.handbook = rnr_classdata.get('handbook', {})
    self.health_dice = rnr_classdata['health_dice']
    self.expertise = rnr_classdata['expertise']
    self.is_mage = 'skill_tree' not in rnr_classdata
    self.abilities = list()
    
    self.skill_tree_abilities = list()
    self.skill_tree = None
    self.spells = dict()
    if self.is_mage:
      for tier, spells in rnr_classdata['spells'].items():
        if not tier in self.spells:
          self.spells[tier] = list()
        for spell in spells:
          self.spells[tier].append(RnRAbility(spell))
    else:  
      self.skill_tree = rnr_classdata['skill_tree']['tree_path']
      for ability in rnr_classdata['skill_tree']['abilities']:
        self.abilities.append(RnRAbility(ability))


  # def serialize(self, male=False, verbose=False, skip_art=False):
  #   global GLOBAL_SITE_ART_PATH, GLOBAL_ART_DICTIONARY

  #   serial = {}
  #   serial['name'] = self.name
  #   serial['evasion'] = self.evasion
  #   serial['stat_recommendation'] = self.stat_recommendation
  #   serial['handbook'] = self.handbook
  #   serial['health_dice_bonus'] = self.health_dice_bonus
  #   serial['abilities'] = self.abilities
  #   serial['expertise'] = self.expertise

  #   gender_string = 'male' if male else 'female'

  #   if not skip_art:
  #     absolute_art_folder = Path(GLOBAL_SITE_ART_PATH, 'class')
  #     relative_art_folder = Path('static', 'images', 'class')

  #     image_path, attribution = core.get_gendered_art(relative_art_folder, absolute_art_folder, self.name.lower(), male)

  #     img_name = image_path.split('/')[-1].split('.')[0]
  #     rights = GLOBAL_ART_DICTIONARY.get(f'{img_name}_{gender_string}', None)
  #     if rights is None:
  #       rights = GLOBAL_ART_DICTIONARY.get(f'{img_name}', None)

  #     serial['rights'] = rights
  #     serial["path_to_image"] = image_path
  #   return serial
  
  def get_markdown(self):
    class_text = f'# {self.name}  \n'
    class_text += "## Recommended Stats  \n"
    for stat in ["Strength", "Dexterity", "Intelligence","Inner_Fire",  "Perception", "Charisma"]:
      class_text += f"*  __{stat.replace('_', ' ')}:__ {self.stat_recommendation[stat]}  \n"

    class_text += "  \n"

    class_text += "## Health and Expertise  \n"
    class_text += f"{self.name}s use {self.health_dice} as their class health dice. "
    class_text += f"{self.expertise}  \n"

    class_text += "## Abilities  \n"
    for ability in sorted(self.abilities, key=lambda a: a.name):
      class_text += ability.get_markdown()
    return class_text