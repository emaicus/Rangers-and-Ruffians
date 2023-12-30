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
        version_suffix: str,
        race_data: dict, 
        class_data: list, 
        attribution_data: dict, 
        monster_data: dict, 
        pantheon_data: dict, 
        background_data: list, 
        weapon_data: list
  )-> None:
    self.version = version
    self.version_suffix = version_suffix
    self.races = self.load_races(race_data)
    self.classes = self.load_classes(class_data)
    self.attributions = attribution_data
    self.monsters = self.load_monsters(monster_data)
    self.pantheon = self.load_pantheon(pantheon_data)
    self.backgrounds = self.load_backgrounds(background_data)
    self.weapons = self.load_weapons(weapon_data)
  
  def get_full_version(self):
    return f'{self.version} {self.version_suffix}'

  def load_races(self, race_data : dict) -> list:
    races = list()
    for race_data in race_data:
       races.append(RnRRace(race_data))
    return races
  
  def load_classes(self, class_data: list) -> list:
    rnr_classes = list()
    for rnr_class in class_data:
      rnr_classes.append(RnRClass(rnr_class))
    return rnr_classes 

  def load_backgrounds(self, background_data: list) -> list:
    rnr_backgrounds = list()
    for background in background_data:
      rnr_backgrounds.append(RnRBackground(background))
    return rnr_backgrounds

  def load_weapons(self, weapon_data: list) -> list:
    rnr_weapons = list()
    for weapon in weapon_data:
      rnr_weapons.append(RnRWeapon(weapon))
    return rnr_weapons
  
  def load_monsters(self, monster_data : dict) -> list:
    rnr_monsters = list()
    for monster in monster_data:
      rnr_monsters.append(RnRMonster(monster))
    return rnr_monsters
  
  def load_pantheon(self, pantheon_data: dict) -> dict:
    pass

  def generate_markdown_art_attribution(self, art : str) -> str:
    rights = self.attributions.get(art, None)

    if rights is None:
      raise KeyError(f'Could not find "{art}" in the global attributions dictionary.')

    title           = self.attributions[art]['title']
    url             = self.attributions[art]['url']
    artist          = self.attributions[art]['artist']
    license_acronym = self.attributions[art]['license_acronym']
    license_url     = self.attributions[art]['license_url']
    return f'_"[{title}"]({url}) by {artist} is licensed under [{license_acronym}]({license_url})_  \n'
