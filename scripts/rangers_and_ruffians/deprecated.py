def which_icons(rnr_class : str):
  icons = list()

  #Everyone has health
  icons.append(('hearts.svg', 'Health'))

  # #Necromancers, Monks, and Sorcerers don't have spell_points. Cleric and paladin get special.
  # if rnr_class in core.magical_classes and rnr_class not in ['necromancer', 'sorcerer', 'monk','cleric', 'paladin']:

  #Clerics and Paladins get special action points.
  if rnr_class.lower() in ['cleric', 'paladin']:
    icons.append(('prayer.svg', 'Action Points'))
  else:
    icons.append(('ink-swirl.svg', 'Action Points'))

  #Sorcerers have influence points
  if rnr_class.lower() == 'sorcerer':
    icons.append(('magic-swirl.svg', 'Influence'))

  #necromancers have souls
  if rnr_class.lower() == 'necromancer':
    icons.append(('tombstone.svg', 'Souls'))

  #highborn have gumption
  if rnr_class.lower() == 'highborn':
    icons.append(('swords-power.svg', 'Gumption'))

  # #archers have magic arrows
  # if rnr_class == 'archer':
  #   icons.append(('quiver.svg', 'Magic Quiver'))

  #Bards have spell coins
  if rnr_class.lower() == 'bard':
    icons.append(('swap-bag.svg', 'Spell Coins'))

  #Everyone has spell power, armor, and magic armor.
  icons.append(('fire-spell-cast.svg', 'Spell Power'))
  icons.append(('shield.svg', 'Armor'))
  icons.append(('bolt-shield.svg', 'Mage Armor'))
  icons.append(('moebius-trefoil.svg', 'Level Up'))
  return icons