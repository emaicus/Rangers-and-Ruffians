import rnr_utils
import random
import sys

#What features do we want?
# Healers.
# Attacks that leach.
# Timed combat abilities.

ATTACKS = {
  "mage" : {
    0 : [{'dice' : '1d6'},],
    1 : [{'dice' : '1d8'},],
    2 : [{'dice' : '1d8'},],
    3 : [{'dice' : '2d8'},],
    4 : [{'dice' : '2d8'}, {'dice' : '1d6'}],
    5 : [{'dice' : '4d8'}, {'dice' : '1d6'}],
    6 : [{'dice' : '4d8'}, {'dice' : '1d8'}],
    7 : [{'dice' : '8d8'}, {'dice' : '1d8'}],
    8 : [{'dice' : '8d8'}, {'dice' : '2d8'}],
    9 : [{'dice' : '6d20'}, {'dice' : '2d8'}],
    10 : [{'dice' : '6d20'}, {'dice' : '2d8'}]
  },
  "fighter" : {
    0 : [{'dice' : '1d6'},],
    1 : [{'dice' : '1d8'},],
    2 : [{'dice' : '1d8'},],
    3 : [{'dice' : '1d8'},],
    4 : [{'dice' : '1d8'},{'dice' : '1d8'}],
    5 : [{'dice' : '1d10'},{'dice' : '1d10'}],
    6 : [{'dice' : '1d14'},{'dice' : '1d14'}],
    7 : [{'dice' : '1d14'},{'dice' : '1d14'},{'dice' : '1d14'}],
    8 : [{'dice' : '1d16'},{'dice' : '1d16'},{'dice' : '1d16'}],
    9 : [{'dice' : '1d16'},{'dice' : '1d16'},{'dice' : '1d16'}],
    10 : [{'dice' : '1d18'},{'dice' : '1d18'},{'dice' : '1d18'}]
  }
}

class combatant:
  #Attacks is an array of strings of the form xdx (e.g. 2d6)
  # def __init__(self, rnr_character, attacks):
  #   self.name = rnr_character.name
  #   self.abilities = rnr_character.abilities
  #   self.stats = rnr_character.stats
  #   self.character = rnr_character
  #   self.max_health = rnr_character.get_health()
  #   self.current_health = rnr_character.get_health()
  #   self.attacks = attacks

  def __init__(self, name, abilities, stats, max_health, attacks, caster, attack_function):
    self.name = name
    self.abilities = abilities
    self.stats = stats
    self.max_health = max_health
    self.current_health = max_health
    self.attacks = attacks
    self.caster=caster
    self.attack_function = attack_function
    self.status_effects = list()
  
  def dead(self):
    if self.current_health <= 0:
      return True
    else:
      return False
  
  def heal(amt):
    self.current_health = min(self.max_health, self.current_health+amt)

  def add_status_effect(self, effect):
    for status_effect in self.status_effects:
      if status_effect.name == effect.name:
        return
    self.status_effects.append(effect)

  def process_status_effects(self, silent=False):
    updated_effects_list = list()
    have_advantage = False
    have_disadvantage = False
    stat_changes = dict()
    for effect in self.status_effects:      
      if effect.advantage:
        have_advantage = True
      if effect.disadvantage:
        have_disadvantage = True

      if effect.damage_dice != '':
        dmg = roll_dice(effect.damage_dice, silent=silent)
        if not silent:
          print('Took {0} damage from {1}'.format(dmg, effect.name))
        self.current_health -= dmg
      if effect.healing_dice != '':
        heal = roll_dice(effect.healing_dice, silent=silent)
        if not silent:
          print('Healed {0} damage from {1}'.format(heal, effect.name))
        self.current_health -= heal

      for key, val in effect.stat_modification.items():
        if not key in stat_changes:
          stat_changes[key] = 0
        stat_changes[key] += val  

      effect.length_so_far += 1
      if effect.length_so_far >= effect.duration:
        updated_effects_list.append(effect)
    self.status_effects = updated_effects_list

    if have_advantage and have_disadvantage:
      have_advantage = have_disadvantage = False

    return have_advantage, have_disadvantage, stat_changes

class status_effect:
  def __init__(self, name, duration, target_foes=True, disadvantage=False,advantage=False,damage_dice="",healing_dice="",stat_modification={}):
    self.name = name
    self.target_foes = target_foes
    self.duration = duration
    self.length_so_far = 0
    self.disadvantage = disadvantage
    self.advantage = advantage
    self.damage_dice = damage_dice
    self.healing_dice = healing_dice
    self.stat_modification = dict(stat_modification)

  def to_string(self):
    ret = '{0}: lasts {1} turn(s), targets '.format(self.name.title(), self.duration)
    if self.target_foes:
      ret += 'enemies '
    else:
      ret += 'allies '

    if self.damage_dice != '':
      ret += 'does {0} damage '.format(self.damage_dice)
    if self.healing_dice != '':
      ret += 'heals {0} health '.format(self.healing_dice)

    first = True
    for key, val in self.stat_modification.items():
      if first:
        ret += 'causes '
      ret += '{0} {1}'.format(val, key)
    if self.advantage == True:
      ret += 'and gives the target advantage'
    if self.disadvantage == True:
      ret += ' and gives the target disadvantage'
    return ret

def generate_starting_offensive_abilities():
  return [
  quick_status_effect_block('poison_barb', damage_dice='1d4', duration=3 ),
  quick_status_effect_block('knock off balance', disadvantage=True ),
  quick_status_effect_block('burn', damage_dice='1d4', duration=3 ),
  quick_status_effect_block('frighten', disadvantage=True ),
  quick_status_effect_block('frenzy', damage_dice='1d10', advantage=True, duration=2 )
]

'''
Attack Selection Functions
'''
def greedy_attack(entities, targets=1):
  if targets > len(entities):
    return entities
  elif len(entities) == 0:
    return None
  entities.sort(key=lambda x: x.current_health)
  return entities[:targets]

def random_attack(entities, targets=1):
  if targets > len(entities):
    return entities
  elif len(entities) == 0:
    return None
  return random.sample(entities, targets)

def rnr_entity_to_combatant(c,attacks, attack_function):
  caster = True if c.rnr_class in rnr_utils.casting_classes else False
  return combatant(c.name, c.abilities, c.stats, c.get_health(), attacks, caster, attack_function)

def quick_stat_block(vitality=0, strength=0, dexterity=0, inner_fire=0):
  return {
    "Vitality" : vitality,
    "Strength" : strength,
    "Dexterity" : dexterity,
    "Inner_Fire" : inner_fire
  }

def quick_status_effect_from_block(block):
  return status_effect(block['name'], block['duration'], target_foes=block['target_foes'],
                       disadvantage=block['disadvantage'], advantage=block['advantage'], damage_dice=block['damage_dice'],
                       healing_dice=block['healing_dice'], stat_modification=block['stat_modification'])

'''
1 duration means immediate effect on the opponent's next turn.
'''
def quick_status_effect_block(name, duration=1, target_foes=True, disadvantage=False, advantage=False, damage_dice='', healing_dice='', stat_modification={}):
  return {
    "name" : name,
    "duration" : duration,
    "target_foes" : target_foes,
    "disadvantage" : disadvantage,
    "advantage" : advantage,
    "damage_dice" : damage_dice,
    "healing_dice" : healing_dice,
    "stat_modification" : stat_modification
  }

def get_health(level, vit):
  summed_level = sum(range(level+1))
  modifier = vit * (level + 1)
  return 15 + summed_level + modifier

#tuples contain race, class, level.
def load_character_team(tuples):
  team = list()
  for race, rnr_class, level, attack_function in tuples:
    character = rnr_utils.rnr_character('', race, rnr_class, level)
    attacks = ATTACKS['mage'][level] if rnr_class in rnr_utils.casting_classes else ATTACKS['fighter'][level]
    team.append(rnr_entity_to_combatant(character, attacks, attack_function))
  return team

def load_horde(health, name, count, stats, attacks, caster, attack_function=random_attack):
  stat_block = quick_stat_block(vitality=stats.get('Vitality',0),strength=stats.get('Strength',0),dexterity=stats.get('Dexterity',0),inner_fire=stats.get('Inner_Fire',0))
  horde = list()
  for i in range(count):
    my_name = '{0} {1}'.format(name, i)
    horde.append(combatant( my_name, [], stat_block, health, attacks, caster, attack_function))
  return horde  

def get_entities_not_on_team(my_team, teams, only_living=True):
  entities = list()
  for team in teams.keys():
    if team == my_team:
      continue
    entities += get_entities_on_team(team, teams,only_living)
  return entities

def get_entities_on_team(team, teams, only_living=True):
  entities = list()
  for entity in teams[team]:
    if not entity.dead():
      entities.append(entity)
  return entities

def roll_dice(dice_string, advantage=False, disadvantage=False, can_crit=False, silent=False):
  num_dice, dice_size = dice_string.split('d')
  num_dice = int(num_dice)
  dice_size = int(dice_size)
  total = 0
  for die in range(num_dice):
    total += roll_single_dice(dice_size, advantage=advantage, disadvantage=disadvantage, can_crit=can_crit, silent=silent)
  if not silent:
    print('rolled a total of {0}'.format(total))
  return total

def roll_single_dice(max_value, advantage=False, disadvantage=False, can_crit=False, silent=False):
  roll = random.randint(1, max_value)
  
  if advantage:
    if not silent:
      print('rolling with advantage')
    roll = max(roll, random.randint(1,max_value))
  elif disadvantage:
    if not silent:
      print('rolling with disadvantage')
      roll = min(roll, random.randint(1, max_value))

  if can_crit and roll == max_value:
    if not silent:
      print('rolled a crit!')
    roll += random.randint(1,max_value)
  
  if not silent:
    print('rolled a {0}'.format(roll))
  
  return roll

'''
Returns false on a save
'''
def does_the_effect_work(caster, defender,silent=False):
  spell_power = 10 + (caster.stats['Inner_Fire'] * 2)
  saving_throw = roll_single_dice(20,silent=True) + defender.stats['Inner_Fire']
  success = False if saving_throw >= spell_power else True
  if not silent:
    print("{0} rolled a {1} against {2}'s spell power {3}: did the spell work? {4}".format(defender.name, saving_throw, caster.name, spell_power, success))
  return success

def make_attack(player, attack, enemies, advantage, disadvantage, stat_modification, silent=False):
  best_stat = get_best_stat_name(player.caster, player.stats)
  damage_stat = player.stats.get(best_stat, 0)
  stat_mod = stat_modification.get(best_stat, 0)

  attack_damage = attack['dice']
  effect = attack.get('status_effect', None)

  can_crit = True if int(attack_damage.split('d')[0]) == 1 else False

  total_damage = roll_dice(attack_damage, advantage, disadvantage, can_crit, silent=silent) + damage_stat
  if not silent:
    print('did {0} damage after adding {1} damage stat'.format(total_damage, damage_stat))
  for enemy in enemies:
    enemy.current_health -= total_damage

    if effect != None:
      if does_the_effect_work(player, enemy,silent):
        enemy.add_status_effect(quick_status_effect_from_block(effect))
    if not silent:
      print("After {0}'s attack, {1} was left with {2} health".format(player.name, enemy.name, enemy.current_health))

def take_turn(player, teams, my_team, silent=False):
  if not silent:
    print("It is {0}'s turn".format(player.name))
  advantage, disadvantage, stat_modification = player.process_status_effects(silent=silent)
  
  opponents = get_entities_not_on_team(my_team, teams)
  allies = get_entities_on_team(my_team, teams)
  
  for atk in player.attacks:
    next_target = player.attack_function(opponents, atk.get('targets', 1))
    if next_target == None:
      break
    make_attack(player, atk, next_target, advantage, disadvantage, stat_modification, silent )

def battle(teams,silent=False):
  rounds = 0
  while True:
    rounds += 1
    for team in teams:
      enemies = get_entities_not_on_team(team, teams, only_living=True)
      if len(enemies) == 0:
        if not silent:
          print('team {0} wins!'.format(team))
          print_survivors(teams,silent)
        return team, rounds
      for player in get_entities_on_team(team, teams, only_living=True):
        take_turn(player, teams, team,silent=silent)

def print_combatants(teams, silent=False):
  if not silent:
    print('THE COMBATANTS ARE:')
    for team, players in teams.items():
      print('For team {0}:'.format(team))
      for player in players:
        print('\t{0}, with {1} health and the following attacks: {2}'.format(player.name, player.max_health, player.attacks))
  # else:
  #   print('combatants:')
  #   for team, players in teams.items():
  #     print('{0}: '.format(team), end='')
  #     for player in players:
  #       print('{0}'.format(player.name),end=' ')
  #   print()

def print_survivors(teams,silent=False):
  if not silent:
    for team, players in teams.items():
      for player in players:
        if not player.dead():
          print('\t{0}: {1},'.format(player.name, player.current_health))

def the_goblin_test(fuzz_factor):
  victory_dict = dict()
  for level in range(0,11):
    victory_dict[level] = dict()
    for goblin_count in range(1,10):
      victory_dict[level][goblin_count] = 0
      for fuzz in range(fuzz_factor):
        teams = dict()
        teams['hetzer_company'] = load_character_team( [ ('elf','paladin',level), ('human', 'knight', level), ('orc', 'archer', level), ('gnome', 'monk', level), ('catterwol', 'rogue', level), ('human','ranger',level) ])
        teams['goblin_horde']   = load_horde(goblin_count, 'goblin', 10, {'dexterity' : 2}, ["1d6",], False) 
        print_combatants(teams,silent=True)
        victor = battle(teams,silent=True)
        if victor == 'hetzer_company':
          victory_dict[level][goblin_count] +=1
  for level in victory_dict.keys():
    for key, val in victory_dict[level].items():
      print('level {0}, {1} goblins, win percentage: {2}'.format(level, key, val/fuzz_factor))

def get_best_stat_name(caster, stats):
  if caster:
    return 'Inner_Fire'
  else:
    return 'Dexterity' if stats['Dexterity'] > stats['Strength'] else 'Strength'

def get_best_stat(caster, stats):
  return stats[get_best_stat_name(caster, stats)]

def load_hetzer_company(level, attack_function=random_attack):
  return 'Hetzer Company', load_character_team( 
    [ ('elf','paladin',level, attack_function), 
      ('human', 'knight', level, attack_function), 
      ('orc', 'archer', level, attack_function), 
      ('halfling', 'sorcerer', level, attack_function), 
      ('catterwol', 'rogue', level, attack_function), 
      ('human','ranger',level, attack_function) ]
  )

def load_archibold(level, attack_function=random_attack):
  return 'Archibold, The Wizard', load_character_team( [ ('human','wizard',level, attack_function) ] )

def load_gillthunder(level, attack_function=random_attack):
  return 'Gillthunder', load_character_team( [ ('human','knight',level, attack_function) ] )

def load_race_class(level,race,rnr_class,attack_function=random_attack):
  return '{0} {1}'.format(race.title(), rnr_class.title()), load_character_team( [race,rnr_class,level,attack_function] )

def load_lich_busters(level,  attack_function=random_attack):
  return 'Lich Busters', load_character_team( 
    [('sprout','druid',level, attack_function), 
      ('elf', 'battle_mage', level, attack_function), 
      ('human', 'paladin', level, attack_function) ]
  )

def load_abyss(level,  attack_function=random_attack):
  return "Archi B's Posse", load_character_team( 
    [('human','wizard',level, attack_function), 
    ('orc', 'gunslinger', level, attack_function), 
    ('gnome', 'monk', level, attack_function), 
    ('lizkin', 'necromancer', level, attack_function), 
    ('elf', 'paladin', level, attack_function), 
    ('human', 'cleric', level, attack_function)]
  )

def generate_boss(name, count, health, stats, caster, attacks):
  return load_horde(health, name, count, stats, attacks, caster)

def upgrade_dice(die):
  if die == 4:
    return 6
  elif die==6:
    return 8
  elif die==8:
    return 10
  elif die==10:
    return 12
  elif die==12:
    return 20
  else:
    print('ERROR: Bad upgrade dice d{0}'.format(die))
    sys.exit(1)

def downgrade_dice(die):
  if die==6:
    return 4
  elif die==8:
    return 6
  elif die==10:
    return 8
  elif die==12:
    return 10
  elif die == 20:
    return 12
  else:
    print('ERROR: Bad downgrade dice d{0}'.format(die))
    sys.exit(1)

def compute_damage_per_round(attacks, count=1,stats=None, caster=False):
  if stats!=None:
    mod = get_best_stat(caster, stats)
  else:
    mod = 0

  min_dpr = average_dpr = max_dpr = 0 
  for attack in attacks:
    split = attack['dice'].split('d')
    number = int(split[0])
    size = int(split[1])
    for i in range(number):
      min_dpr += 1
      average_dpr += size // 2
      max_dpr += size + size//2
    min_dpr += mod
    average_dpr += mod
    min_dpr += mod
  return min_dpr * count, average_dpr * count, max_dpr * count

def upgrade_number_of_dice(dice_str):
  tmp = dice_str.split('d')
  return '{0}d{1}'.format(int(tmp[0])+1, tmp[1])

def downgrade_number_of_dice(dice_str):
  tmp = dice_str.split('d')
  return '{0}d{1}'.format(int(tmp[0])-1, tmp[1])

def upgrade_type_of_dice(dice_str):
  tmp = dice_str.split('d')
  return '{0}d{1}'.format(tmp[0], upgrade_dice(int(tmp[1])))

def downgrade_type_of_dice(dice_str):
  tmp = dice_str.split('d')
  return '{0}d{1}'.format(tmp[0], downgrade_dice(int(tmp[1])))
#crude consolidation function
def auto_consolidate_dice(inpt):
  quick_map = {
    '3d4' : '2d6',
    '4d4' : '2d8',
    '4d6' : '3d8',
    '4d8' : '3d10',
    '5d8' : '4d10',
    '5d10' : '4d12',
    '6d12' : '3d20'
  }
  ret = quick_map[inpt] if inpt in quick_map else inpt
  print('ret', ret)
  return ret


def better_upgrade_boss(team_level, team_size, count, health, stats, attacks, caster, win_percentage, desired_win_chance, rounds_of_combat, desired_rounds_of_combat, allow_count_change=True):

  attack_upgrade_desirability = {4:6,6:5, 8:4, 10:3, 12:2, 20:0}

  party_min_dmg, party_avg_dmg, party_max_dmg = compute_damage_per_round(ATTACKS['fighter'][team_level], count=team_size)
  boss_min_dmg, boss_avg_dmg, boss_max_dmg = compute_damage_per_round(attacks, count=count, stats=stats, caster=caster) 

  print('party min dmg {0}, party avg dmg {1}, party_max_dmg {2}'.format(party_min_dmg, party_avg_dmg, party_max_dmg))
  target_health = party_avg_dmg * desired_rounds_of_combat
  max_health = (party_max_dmg * desired_rounds_of_combat)
  min_health = (party_avg_dmg * desired_rounds_of_combat) // 2

  print('min_health {0}, target_health: {1}, max_health: {2}'.format(min_health, target_health, max_health))


  # The larger the difference, the more we are loosing.
  # e.g. desired is .4, win is .5, the party is winning .1 too much.
  difference = win_percentage - desired_win_chance 

  #DONE: damage, stats, health, count
  #TODO: minions, targets, effects, spell_power.

  best_stat = get_best_stat(caster, stats)

  #address things in order. 

  possible = list()

  if roll_single_dice(4,silent=True) != 4:
    #If health is too low, we should add it as a possible upgrade
    if rounds_of_combat < desired_rounds_of_combat and health < max_health:
      possible.append('health')
    #If the party is winning WAY too much
    if difference > .3 and allow_count_change:
      possible.append('count')
    #If we are winning by a decent margin
    if difference > .15:
      possible.append('damage')
    else:
      possible.append('stats')
  else:
    possible = list(['stats', 'health', 'damage'])
    if allow_count_change:
      possible.append('count')
    print('shaking it up.')

  upgrade = random.choice(possible)

  if upgrade == 'health':
    print('increasing health from {0} to {1}'.format(health, health+10))
    health += 10
  elif upgrade == 'stats':
    best_stat = get_best_stat_name(caster, stats)
    print('increasing {0} from {1} to {2}'.format(best_stat, stats[best_stat], stats[best_stat]+1))
    stats[best_stat] += 1
  elif upgrade == 'damage':
    lowest_damage = 0
    lowest_position=-1
    i = 0
    no_effect = None
    have_effect = list()
    for attack in attacks:
      if not 'status_effect' in attack:
        no_effect = i
      else:
        have_effect.append(i)
      _, average, _ = compute_damage_per_round(list([attack]))
      if average < lowest_damage:
        lowest_damage = average
        lowest_position = i
      i+=1
    low = attacks[lowest_position]['dice'].split('d')
    low_dmg = int(low[0]) * int(low[1])

    if (difference > .1 and roll_single_dice(6,silent=True) == 6) or (difference > .5 and roll_single_dice(2,silent=True) == 2):
      print('increasing number of targets')
      if not 'targets' in attacks[lowest_position]:
        attacks[lowest_position]['targets'] = 2
      else:
        attacks[lowest_position]['targets'] += 1
    elif len(have_effect) == 0 or (roll_single_dice(10,silent=True) == 10 and no_effect != None):
      effect = random.choice(generate_starting_offensive_abilities())
      print('Added new effect {0}'.format(effect['name']))
      if not 'status_effect' in attacks[lowest_position]:
        attacks[lowest_position]['status_effect'] = effect
      else:
        attacks[no_effect]['status_effect'] = effect
    elif len(have_effect) > 0 and roll_single_dice(6,silent=True) == 6:
      up_effect =  random.choice(have_effect)
      up_options = list(['duration', 'damage'])
      if attacks[up_effect]['status_effect']['disadvantage'] == False:
        up_options.append('disadvantage')
      effect_upgrade = random.choice(up_options)

      if effect_upgrade == 'duration':
        attacks[up_effect]['status_effect']['duration'] += 1
        print('upgraded effect duration')
      elif effect_upgrade == 'disadvantage':
        attacks[up_effect]['status_effect']['disadvantage'] = True
      else:
        print('dice ', attacks[up_effect]['status_effect']['damage_dice'])
        if attacks[up_effect]['status_effect'].get('damage_dice', '') == '':
          attacks[up_effect]['status_effect']['damage_dice'] = '1d4'
        elif attacks[up_effect]['status_effect']['damage_dice'].split('d')[1] != '12':
          attacks[up_effect]['status_effect']['damage_dice'] = auto_consolidate_dice(upgrade_type_of_dice(attacks[up_effect]['status_effect']['damage_dice']))
        else:
          attacks[up_effect]['status_effect']['damage_dice'] = auto_consolidate_dice(upgrade_number_of_dice(attacks[up_effect]['status_effect']['damage_dice']))
    elif len(attacks) < 2 and low_dmg >= 12:
      attacks.append({'dice':'1d4'})
      print('adding a d4 attack.')
    elif int(low[0]) < 4:
      attacks[lowest_position]['dice'] = auto_consolidate_dice(upgrade_number_of_dice(attacks[lowest_position]['dice']))
      print('upgraded damage dice {0}'.format(attacks[lowest_position]))
    elif int(low[1]) != 12 and int(low[1]) != 20:
      attacks[lowest_position]['dice'] = auto_consolidate_dice(upgrade_type_of_dice(attacks[lowest_position]['dice']))
      print('upgraded damage dice {0}'.format(attacks[lowest_position]))
    else:
      attacks.append({'dice':'1d4'})
      print('adding a d4 attack.')
  else:
    if not allow_count_change:
      print("woah! trying to change count when we can't!")
      sys.exit(1)
    print('increasing count')
    count +=1
  return count, health, stats, attacks

def better_downgrade_boss(team_level, team_size, count, health, stats, attacks, caster, win_percentage, desired_win_chance, rounds_of_combat, desired_rounds_of_combat, allow_count_change=True):

  attack_upgrade_desirability = {4:6,6:5, 8:4, 10:3, 12:2, 20:0}

  party_min_dmg, party_avg_dmg, party_max_dmg = compute_damage_per_round(ATTACKS['fighter'][team_level], count=team_size)
  boss_min_dmg, boss_avg_dmg, boss_max_dmg = compute_damage_per_round(attacks, count=count, stats=stats, caster=caster) 

  print('party min dmg {0}, party avg dmg {1}, party_max_dmg {2}'.format(party_min_dmg, party_avg_dmg, party_max_dmg))
  target_health = party_avg_dmg * desired_rounds_of_combat
  max_health = (party_max_dmg * desired_rounds_of_combat)
  min_health = (party_avg_dmg * desired_rounds_of_combat) // 2

  print('min_health {0}, target_health: {1}, max_health: {2}'.format(min_health, target_health, max_health))


  # The larger the difference, the more we are winning.
  # e.g. desired is .4, win is .3, we are winning .1 too much.
  difference = desired_win_chance - win_percentage

  #DONE: damage, stats, health, count
  #TODO: minions, targets, effects, spell_power.

  best_stat = get_best_stat(caster, stats)

  #address things in order. 

  possible = list()

  if roll_single_dice(4,silent=True) != 4:
    #If health is too low, we should add it as a possible upgrade
    if rounds_of_combat > desired_rounds_of_combat and health > min_health:
      possible.append('health')

    #If we are winning WAY too much
    if difference > .3 and allow_count_change and count > 1:
      possible.append('count')
    #If we are winning by a decent margin
    if difference > .15:
      possible.append('damage')
    else:
      possible.append('stats')
  else:
    possible = list(['stats', 'health', 'damage'])
    if allow_count_change and count > 1:
      possible.append('count')
    print('shaking it up.')

  downgrade = random.choice(possible)

  if downgrade == 'health':
    print('decreasing health from {0} to {1}'.format(health, health-10))
    health -= 10
  elif downgrade == 'stats':
    best_stat = get_best_stat_name(caster, stats)
    print('decreasing {0} from {1} to {2}'.format(best_stat, stats[best_stat], stats[best_stat]-1))
    stats[best_stat] -= 1
  elif downgrade == 'damage':
    highest_damage = 0
    highest_position=-1
    i = 0
    have_effect = list()
    for attack in attacks:
      if 'status_effect' in attack:
        have_effect.append(i)
      _, average, _ = compute_damage_per_round(list([attack]))
      if average > highest_damage:
        highest_damage = average
        highest_position = i
      i+=1
    low = attacks[highest_position]['dice'].split('d')

    if len(have_effect) > 0 and roll_single_dice(10,silent=True) == 6:
      down_effect = random.choice(have_effect)
      down_options = list()
      if attacks[down_effect]['status_effect']['duration'] > 1:
        down_options.append('duration')
      if attacks[down_effect]['status_effect']['disadvantage'] == True:
        down_options.append('disadvantage')
      if attacks[down_effect]['status_effect'].get('damage_dice', '') == '':
        down_options.append('damage')

      if not len(down_options) == 0:
        effect_downgrade = random.choice(down_options)

      if len(down_options) == 0:
        attacks[down_effect].pop('status_effect', None)
      elif effect_downgrade == 'duration':
        attacks[down_effect]['status_effect']['duration'] -= 1
        print('decreased effect duration')
      elif effect_downgrade == 'disadvantage':
        attacks[down_effect]['status_effect']['disadvantage'] = False
        print('removed disadvantage')
      else:
        if attacks[down_effect]['status_effect']['damage_dice'].split('d')[0] != '1':
          attacks[down_effect]['status_effect']['damage_dice'] = auto_consolidate_dice(downgrade_number_of_dice(attacks[down_effect]['status_effect']['damage_dice']))
        elif attacks[down_effect]['status_effect']['damage_dice'].split('d')[1] != '4':
          attacks[down_effect]['status_effect']['damage_dice'] = auto_consolidate_dice(downgrade_type_of_dice(attacks[down_effect]['status_effect']['damage_dice']))
        else:
          attacks[down_effect].pop('status_effect', None)
    elif int(low[1]) != 4:
      attacks[highest_position]['dice'] = auto_consolidate_dice(downgrade_type_of_dice(attacks[highest_position]['dice']))
      print('downgraded damage of dice'.format(attacks[highest_position]))
    elif int(low[0]) != 1:
      attacks[highest_position]['dice'] = auto_consolidate_dice(downgrade_number_of_dice(attacks[highest_position]['dice']))
      print('downgraded number of dice'.format(attacks[highest_position]))
    elif len(attacks) != 1:
      tmp_atk = attacks.pop(highest_position)
    else:
      print('Error, cannot remove attack {0}'.format(attacks[highest_position]))
  else:
    print('decreasing count')
    count -=1
  return count, health, stats, attacks



def boss_check(team_level, team_creation_function, name, count, health, stats, caster, attacks, desired_win_chance=.4, desired_round_of_combat=5, allow_count_change=True, player_attack_function=random_attack):
  precision = .05
  avg_rounds = 0
  print('Testing the {0}.'.format(name))
  win_percentage = 100
  team_name, _ = team_creation_function(team_level, player_attack_function)
  while True:
    if win_percentage >= desired_win_chance - precision and win_percentage <= desired_win_chance + precision and avg_rounds < desired_round_of_combat + (desired_round_of_combat/4) and avg_rounds > desired_round_of_combat - (desired_round_of_combat/4):
      print_fancy_enemy(count, name, health, stats, attacks, win_percentage, avg_rounds)
      break
    victory = 0
    avg_rounds = 0
    iterations = 50
    for i in range(iterations):
      teams = dict()
      teams['boss'] = generate_boss(name, count, health, stats, caster, attacks)
      _, teams[team_name] = team_creation_function(team_level, random_attack)
      # print_combatants(teams)
      victor, rounds = battle(teams,silent=True)
      avg_rounds += rounds
      #sys.exit(1)
      if victor == team_name:
        victory += 1
    avg_rounds /= iterations
    win_percentage = victory / iterations
    if win_percentage > desired_win_chance + precision:
      print('The fight was too easy for the {0} ({1})'.format(team_name, win_percentage))
      count, health, stats, attacks = better_upgrade_boss(team_level, len(teams[team_name]), count, health, stats, attacks, caster, win_percentage, desired_win_chance, avg_rounds, desired_round_of_combat, allow_count_change=allow_count_change)
    else: #win_percentage < desired_win_chance - precision:
      print('The fight was too hard for the {0} ({1})'.format(team_name, win_percentage))
      count, health, stats, attacks = better_downgrade_boss(team_level, len(teams[team_name]), count, health, stats, attacks, caster, win_percentage, desired_win_chance,avg_rounds, desired_round_of_combat,allow_count_change=allow_count_change)
    print()

def print_fancy_enemy(count, name, health, stats, attacks, win_percentage, rounds_of_combat):
  print('How about trying this version of the encounter? ({0} party win rate, {1} rounds)'.format(win_percentage, rounds_of_combat))
  print('{0} {1}s'.format(count, name))
  print('Each has {0} health, and the following stat block:'.format(health))
  for stat, val in stats.items():
    print('\t{0}: {1}'.format(stat, val))
  print('And can do the following attacks:')
  for attack in attacks:
    plural = 'enemy' if attack.get('targets',1) == 1 else 'enemies'
    print('\t{0} attack which targets {1} {2}'.format(attack['dice'], attack.get('targets',1), plural), end=' ')
    if 'status_effect' in attack:
      effect_str = quick_status_effect_from_block(attack['status_effect']).to_string()
      print('and has the status effect: {0}'.format(effect_str), end='')
    print()


def main():
  #boss_check(7, load_hetzer_company, 'beholder', 1, 300, quick_stat_block(inner_fire=5), True, ['4d8', '4d8', '2d20'], allow_count_change=False)
  #boss_check(1, load_hetzer_company, 'goblin', 6, 15, quick_stat_block(dexterity=1), False, ['1d6'], allow_count_change=True)
  # boss_check(3, load_lich_busters, 'grass_demon', 1, 60, quick_stat_block(dexterity=1), False, [
  #               {'dice' : '2d6', 'targets':3, 'status_effect' : quick_status_effect_block('stomp', disadvantage=True)},
  #               {'dice' : '1d6', 'targets':1, 'status_effect' : quick_status_effect_block('poison_barb', damage_dice='1d10', duration=3 )}
  #               ], desired_round_of_combat=4, allow_count_change=False)
  #boss_check(5, load_hetzer_company, 'elder_knight', 2, 200, quick_stat_block(strength=5), False, [{'dice':'4d12'},], allow_count_change=True)
  #boss_check(10, load_abyss, 'goblin', 1, 10, quick_stat_block(inner_fire=3, dexterity=2), False, [{'dice':'1d6', 'status_effect' : quick_status_effect_block('disadvantage', disadvantage=True)}], allow_count_change=True)
  # boss_check(5, load_abyss, 'horde', 8, 50, quick_stat_block(strength=5), False, 
  #   [
  #     {'dice' : '2d10', 'targets':1, 'status_effect' : quick_status_effect_block('swarm', disadvantage=True)}
  #   ], desired_round_of_combat=7, allow_count_change=True)
  #boss_check(1, load_archibold, 'goblin', 1, 10, quick_stat_block(dexterity=1), False, [{'dice' : '1d6'}], allow_count_change=True)
  #boss_check(10, load_gillthunder, 'goblin', 1, 10, quick_stat_block(dexterity=1), False, [{'dice' : '1d6'}], allow_count_change=True)
  boss_check(7, load_hetzer_company, 'Strahd', 1, 200, quick_stat_block(strength=5,dexterity=5,inner_fire=3), False, 
    [
      {'dice':'4d10'},
      {'dice':'6d6', 'status_effect' : quick_status_effect_block('drain', disadvantage=True, stat_modification=quick_stat_block(strength=-3,dexterity=-3,inner_fire=-1))}
    ], allow_count_change=False, desired_round_of_combat=5)


if __name__ == '__main__':
  main()
