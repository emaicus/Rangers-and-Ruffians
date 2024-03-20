from pathlib import Path
from .RnRAbility import RnRAbility

class RnRClass():
  ''' Takes in classname and json object, instantiates class.'''
  def __init__(self, rnr_classdata):

    self.name = rnr_classdata['name']
    self.stat_recommendation = rnr_classdata['recommended_stats']
    self.handbook = rnr_classdata['handbook']
    self.rule_sections = rnr_classdata.get('rule_sections', [])
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

  def serialize(self):
    serial = dict()
    serial['name'] = self.name 
    serial['recommended_stats'] = self.stat_recommendation 
    serial['handbook'] = self.handbook 
    serial['rule_sections'] = self.rule_sections
    serial['health_dice'] = self.health_dice 
    serial['expertise'] = self.expertise
    serial['is_mage'] = self.is_mage

    if not self.is_mage:
      serial['skill_tree'] = dict()
      serial['skill_tree']['tree_path'] = self.skill_tree
      serial['skill_tree']['abilities'] = list()
      for ability in self.abilities:
       serial['skill_tree']['abilities'].append(ability.serialize())
    else: 
      serial['spells'] = dict()
      for tier, spells in self.spells.items():
        serial['spells'][tier] = list()
        for spell in spells:
          serial['spells'][tier].append(spell.serialize())
    return serial
  
  def get_markdown(self, level=None, art_data=None, printable=False):
    subsection_level = None if level is None else level + 1
    ability_level = None if level is None else level + 2
    class_text = ''
    
    class_text += f'<div class="printable-content" id="printable-{self.name.lower()}">  \n' if printable else ''
    class_text += f'__{self.name}__  \n' if level == None else '#' * level + f' {self.name}  \n'
    class_text += f'<button onclick="printContent(\'printable-{self.name.lower()}\')">Print {self.name}</button>  \n  \n' if printable else ''

    if art_data is not None:
      class_text += f"<img src='{art_data['path']}' class=\"raceClassImage\" />\n\n"
      class_text += f"<span class=\"attribution\">{art_data['attribution']}</span>"

    class_text += f'  \n<div class="handbook-section"   id="handbook-{self.name.lower()}">\n' if printable else ''

    for section in self.handbook:
      if section['display_title']:
        class_text += f"{'#' * subsection_level} {section['title']}  \n"
      class_text += f"{section['text']}  \n"
      class_text += "  \n  \n"
    
    class_text += f'</div>  \n' if printable else ''

    class_text += f"{'#' * subsection_level} Recommended Stats  \n"

    class_text += f'<div class="display-stat-section"   id="display-stats-{self.name.lower()}">\n' if printable else ''
    for stat in ["Strength", "Dexterity", "Intelligence","Inner_Fire",  "Perception", "Charisma"]:
      class_text += f"*  __{stat.replace('_', ' ')}:__ {self.stat_recommendation[stat]}  \n"
    class_text += f'</div>\n' if printable else ''

    class_text += f'<div class="printable-stat-section"   id="printable-stats-{self.name.lower()}">\n' if printable else ''
    for stat in ["Strength", "Dexterity", "Intelligence","Inner_Fire",  "Perception", "Charisma"]:
      class_text += f" __{stat.replace('_', ' ')}:__ {self.stat_recommendation[stat]} "
    class_text += f'  \n </div>\n' if printable else ''

    class_text += "  \n"

    class_text += f"{'#' * subsection_level}  Health and Expertise  \n"
    class_text += f"{self.name}s use {self.health_dice} as their class health dice. "
    class_text += f"{self.expertise}  \n"

    if len(self.abilities) > 0:
      class_text += f"{'#' * subsection_level} Abilities  \n  \n"
      class_text += f"<img src='{art_data['skill_tree_path']}' class=\"skilltree\" />  \n  \n"
      for ability in sorted(self.abilities, key=lambda a: a.name):
        class_text += f'<div class="rnr-ability" id="ability-{ability.name.lower()}">  \n' if printable else ''
        class_text += ability.get_markdown(ability_level)
        class_text += f'</div>  \n' if printable else ''
      class_text+= '  \n'

    if len(self.spells) > 0:
      class_text += f"{'#' * subsection_level}  Spells  \n"
      for tier, spells in self.spells.items():
        class_text += f"{'#' * subsection_level} {tier.replace('_', ' ')}  \n"
        for spell in spells:
          class_text += f'<div class="rnr-ability" id="ability-{spell.name.lower()}">  \n' if printable else ''
          class_text += f'{spell.get_markdown(ability_level)}  \n'
          class_text += f'</div>  \n' if printable else ''
        class_text += '  \n'
      class_text+= '  \n'
    
    class_text += '</div>  \n' if printable else ''

    return class_text