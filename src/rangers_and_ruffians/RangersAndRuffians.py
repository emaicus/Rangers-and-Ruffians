from .RnRRace import RnRRace
from .RnRClass import RnRClass

class RangersAndRuffians():
  ''' Takes in classname and json object, instantiates class.'''
  def __init__(self, version: str, race_data: dict, class_data: list, attribution_data: dict, monster_data: dict, pantheon_data: dict)-> None:
    self.version = version
    self.races = self.load_races(race_data)
    self.classes = self.load_classes(class_data)
    self.attributions = self.load_attributions(attribution_data)
    self.monsters = self.load_monsters(monster_data)
    self.pantheon = self.load_pantheon(pantheon_data)
  
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
  
  def load_attributions(self, attribution_data : dict) -> dict:
    pass 
  
  def load_monsters(self, monster_data : dict) -> dict:
    pass 
  
  def load_pantheon(self, pantheon_data: dict) -> dict:
    pass
