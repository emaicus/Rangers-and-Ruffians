def abbreviate_stat(stat, upper=True):
  stat = stat.lower()
  if stat == 'dexterity':
    ret = 'dex'
  elif stat == 'strength':
    ret = 'str'
  elif stat == 'intelligence':
    ret = 'int'
  elif stat == 'inner fire' or stat == 'inner_fire':
    ret = 'inf'
  elif stat == 'perception':
    ret = 'per'
  elif stat == 'charisma':
    ret = 'cha'
  elif stat == 'luck':
    ret = 'luk'
  else:
    print('ERROR: BAD STAT {stat}')
    return None

  if upper:
    ret = ret.upper()
  return ret

def standard_stat_order():
  return list(['Strength', 'Dexterity', 'Intelligence', 'Inner_Fire', 'Charisma', 'Perception', 'Luck'])

def get_max_health_to_level(health_dice, level):
  health = 0
  for i in range(0, level):
    health += health_dice + 4
  return health

def get_average_health_to_level(health_dice, level):
  health = health_dice + 2.5
  for i in range(1, level):
    health += (health_dice // 2) + .5 + 2.5
  return health