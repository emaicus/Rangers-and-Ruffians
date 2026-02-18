from pathlib import Path
from .RnRAbility import RnRAbility
import typing

class RnRClass():
  ''' Takes in classname and json object, instantiates class.'''
  def __init__(self, rnr_classdata):

    self.name = rnr_classdata['name']
    self.class_type = rnr_classdata['class_type']
    self.stat_recommendation = rnr_classdata['recommended_stats']
    self.handbook = rnr_classdata['handbook']
    self.rule_sections = rnr_classdata.get('rule_sections', [])
    self.health_schedule = rnr_classdata.get('health_schedule', {})
    self.is_mage = 'abilities_by_level' not in rnr_classdata
    self.abilities_by_level = dict()
    self.all_abilities = list()
    self.paths = rnr_classdata.get("paths", {})

    self.spells = dict()
    if self.is_mage:
      for tier, tier_spells in rnr_classdata['spells'].items():
        if not tier in self.spells:
          self.spells[tier] = list()
        for s in tier_spells:
          instantiated_spell = RnRAbility(s)
          self.spells[tier].append(instantiated_spell)
          self.all_abilities.append(instantiated_spell)
    else:  
      self.abilities_by_level = rnr_classdata['abilities_by_level']
      for level, paths in rnr_classdata['abilities_by_level'].items():
        self.abilities_by_level[level] = dict() 

        for path, abilities in paths.items():
          self.abilities_by_level[level][path] = list()

          for a in abilities:
            instantiated_ability = RnRAbility(a)
            self.abilities_by_level[level][path].append(instantiated_ability)
            self.all_abilities.append(instantiated_ability)
  
  def get_all_abilities(self) -> list: 
    return self.all_abilities

  def serialize(self):
    serial = dict()
    serial['name'] = self.name
    serial['class_type'] = self.class_type
    serial['recommended_stats'] = self.stat_recommendation 
    serial['handbook'] = self.handbook 
    serial['rule_sections'] = self.rule_sections
    serial['is_mage'] = self.is_mage
    serial['health_schedule'] = self.health_schedule
    serial['paths'] = self.paths

    if not self.is_mage:
      serial['abilities_by_level'] = dict()
      for level, paths in self.abilities_by_level.items():
        serial['abilities_by_level'][level] = dict()
        for path, abilities in paths.items():
          serial['abilities_by_level'][level][path] = list()
          for ability in abilities:
            serial['abilities_by_level'][level][path].append(ability.serialize())
    else: 
      serial['spells'] = dict()
      for tier, spells in self.spells.items():
        serial['spells'][tier] = list()
        for spell in spells:
          serial['spells'][tier].append(spell.serialize())
    return serial
  
  def get_markdown(self, level=None, art_data: dict | None=None, printable=False) -> str:
    subsection_level = 0 if level is None else level + 1
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

    class_text += f"{'#' * subsection_level}  Health  \n"
    class_text += f"{self.name}s start with {self.health_schedule['starting_health']} health and gain {self.health_schedule['standard_level_health_bonus']} health per level.\n"
    if self.health_schedule['standard_level_health_bonus'] != self.health_schedule['tier_increase_health_bonus']:
      class_text += f"  \nWhen you reach levels 6 and 11, instead gain {self.health_schedule['tier_increase_health_bonus']} health."

    # if len(self.abilities) > 0:
    #   class_text += f"{'#' * subsection_level} Abilities  \n  \n"
    #   if art_data is not None:
    #     class_text += f"<img src='{art_data['skill_tree_path']}' class=\"skilltree\" />  \n  \n"
    #   for ability in sorted(self.abilities, key=lambda a: a.name):
    #     class_text += f'<div class="rnr-ability" id="ability-{ability.name.lower()}">  \n' if printable else ''
    #     class_text += ability.get_markdown(ability_level)
    #     class_text += f'</div>  \n' if printable else ''
    #   class_text+= '  \n'

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