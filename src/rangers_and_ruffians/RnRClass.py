from pathlib import Path
from .RnRAbility import RnRAbility

class RnRClass():
  ''' Takes in classname and json object, instantiates class.'''
  def __init__(self, rnr_classdata):

    self.name = rnr_classdata['name']
    self.stat_recommendation = rnr_classdata['recommended_stats']
    self.handbook = rnr_classdata['handbook']
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
  
  def get_all_abilities(self) -> list: 
    all_abilities = list()
    if self.is_mage:
      for _, spells in self.spells.items():
        all_abilities += spells
    else:  
      all_abilities += self.abilities
    return all_abilities

  
  
  def get_markdown(self, level=None, art_data=None):
    subsection_level = None if level is None else level + 1
    ability_level = None if level is None else level + 2
    
    class_text = f'__{self.name}__  \n' if level == None else '#' * level + f' {self.name}  \n'
    if art_data is not None:
      class_text += f"<img src='{art_data['path']}' class=\"raceClassImage\" />\n\n"
      class_text += art_data['attribution']

    for section in self.handbook:
      if section['display_title']:
        class_text += f"{'#' * subsection_level} {section['title']}  \n"
      class_text += f"{section['text']}  \n"
      class_text += "  \n  \n"

    class_text += f"{'#' * subsection_level} Recommended Stats  \n"
    for stat in ["Strength", "Dexterity", "Intelligence","Inner_Fire",  "Perception", "Charisma"]:
      class_text += f"*  __{stat.replace('_', ' ')}:__ {self.stat_recommendation[stat]}  \n"

    class_text += "  \n"

    class_text += f"{'#' * subsection_level}  Health and Expertise  \n"
    class_text += f"{self.name}s use {self.health_dice} as their class health dice. "
    class_text += f"{self.expertise}  \n"

    if len(self.abilities) > 0:
      class_text += f"{'#' * subsection_level} Abilities  \n  \n"
      class_text += f"<img src='{art_data['skill_tree_path']}' class=\"raceClassImage\" />  \n  \n"
      for ability in sorted(self.abilities, key=lambda a: a.name):
        class_text += ability.get_markdown(ability_level)
      class_text+= '  \n'

    if len(self.spells) > 0:
      class_text += f"{'#' * subsection_level}  Spells  \n"
      for tier, spells in self.spells.items():
        class_text += f"{'#' * subsection_level} {tier.replace('_', ' ')}  \n"
        for spell in spells:
          class_text += f'{spell.get_markdown(ability_level)}  \n'
        class_text += '  \n'
      class_text+= '  \n'

    return class_text