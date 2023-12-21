from .RnRRace import RnRRace
from .RnRClass import RnRClass
from .RnRBackground import RnRBackground
from .RnRWeapon import RnRWeapon
from .RnRMonster import RnRMonster

class RangersAndRuffians():
  ''' Takes in classname and json object, instantiates class.'''
  def __init__(
        self, 
        version: str, 
        race_data: dict, 
        class_data: list, 
        attribution_data: dict, 
        monster_data: dict, 
        pantheon_data: dict, 
        background_data: list, 
        weapon_data: list
  )-> None:
    self.version = version
    self.races = self.load_races(race_data)
    self.classes = self.load_classes(class_data)
    self.attributions = self.load_attributions(attribution_data)
    self.monsters = self.load_monsters(monster_data)
    self.pantheon = self.load_pantheon(pantheon_data)
    self.backgrounds = self.load_backgrounds(background_data)
    self.weapons = self.load_weapons(weapon_data)
  
  def load_races(self, race_data : dict) -> dict:
    races = dict()
    for race_data in race_data:
       races[race_data['name']] = RnRRace(race_data)
    return races
  
  def load_classes(self, class_data: list) -> dict:
    rnr_classes = dict()
    for rnr_class in class_data:
      rnr_classes[rnr_class['name']] = RnRClass(rnr_class)
    return rnr_classes 

  def load_backgrounds(self, background_data: list) -> dict:
    rnr_backgrounds = dict()
    for background in background_data:
      rnr_backgrounds[background['name']] = RnRBackground(background)
    return rnr_backgrounds

  def load_weapons(self, weapon_data: list) -> dict:
    rnr_weapons = dict()
    for weapon in weapon_data:
      rnr_weapons[weapon['name']] = RnRWeapon(weapon)
    return rnr_weapons

  
  def load_attributions(self, attribution_data : dict) -> dict:
    pass 
  
  def load_monsters(self, monster_data : dict) -> dict:
    rnr_monsters = dict()
    for monster in monster_data:
      rnr_monsters[monster['name']] = RnRMonster(monster)
    return rnr_monsters
  
  def load_pantheon(self, pantheon_data: dict) -> dict:
    pass
