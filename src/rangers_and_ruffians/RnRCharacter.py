class RnRCharacter():
  def __init__(self, character_name, race_name, class_name, level, male=False):
    rnr_race_obj = rnr_race.basic_constructor(race_name)
    rnr_class_obj = rnr_class.basic_constructor(class_name)

    self.abilities = rnr_race_obj.abilities + rnr_class_obj.abilities
    self.stats = rnr_class_obj.stat_recommendation
    self.health_dice = rnr_race_obj.health_die_pieces + rnr_class_obj.health_dice_bonus
    self.character_name = f'{race_name} {class_name}' if character_name == '' else character_name
    self.gender = 'male' if male==True else 'female'
    self.race = rnr_race_obj.name
    self.rnr_class = rnr_class_obj.name
    self.rnr_race_obj = rnr_race_obj
    self.rnr_class_obj = rnr_class_obj
    self.level = level

  def serialize(self, verbose=False):
    serial = self.base_serialize(verbose)
    serial['race'] = self.race.lower()
    serial['class'] = self.rnr_class.lower()
    serial['health'] = self.get_health()
    serial['health_dice'] = self.health_dice
    serial['character_name'] = self.character_name
    serial['gender'] = self.gender
    serial['level'] = self.level
    return serial

  def new_character_sheet_serialize(self, verbose=False):
    serial = dict()
    serial['race'] = self.race
    serial['class'] = self.rnr_class
    serial['stats'] = self.stats
    serial['base_abilities'] = self.abilities
    serial['levels'] = self.rnr_class_obj.abilities
    serial['icons'] = which_icons(self.race, self.rnr_class)
    return serial

  def get_average_health(self):
    return get_average_health_to_level(self.health_dice, self.level)

  def get_max_health(self):
    return get_max_health_to_level(self.health_dice, self.level)