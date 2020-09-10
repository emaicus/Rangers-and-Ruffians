import sys
import os
import json
import math
import json
import random
import markdown_handler
import rnr_utils
rnr_utils.load_Rangers_And_Ruffians_Data()

STAT_STEPS = {
  0 : 2,
  1 : 3,
  2 : 3,
  3 : 4,
  4 : 4,
  5 : 5,
  6 : 5,
  7 : 5,
  8 : 5,
  9 : 5,
  10: 5,
  11: 5,
  12: 5,
  13: 5,
  14: 5,
  15: 5
}

# Best descriptive title I could come up with :P
PLAYERS_MISS_RATE = .25
MONSTERS_MISS_RATE = .25

class rnr_weapon():
  #Base constructor
  def __init__(self, num_primary_dice, type_primary_dice, num_magic_dice=0, type_magic_dice=0, hit_modifier=0):
    self.num_primary_dice = num_primary_dice
    self.type_primary_dice = type_primary_dice
    self.num_magic_dice  = num_magic_dice
    self.type_magic_dice = type_magic_dice
    self.hit_modifier = hit_modifier

  def get_average_damage(self, use_action_point=False):
    dmg = 0
    for dice_num, dice_type in [(self.num_primary_dice, self.type_primary_dice),(self.num_magic_dice, self.type_magic_dice)]:
      for i in range(dice_num):
        dmg += (dice_type // 2) + .5
    if use_action_point:
      dmg += (self.type_primary_dice // 2) + .5
    return dmg

  def make_attack(self, use_action_point=False):
    dmg = 0
    for dice_num, dice_type in [(self.num_primary_dice, self.type_primary_dice),(self.num_magic_dice, self.type_magic_dice)]:
      dmg += rnr_utils.roll_dice(dice_num, dice_type)

    if use_action_point:
      dmg += rnr_utils.roll_dice(1, self.type_primary_dice)

    return dmg

class rnr_combatant():
  def __init__(self, level, race_name, subrace_name, class_name, subclass_name, weapon=None):
    global STAT_STEPS

    self.character = rnr_utils.rnr_character('', race_name, subrace_name, class_name, subclass_name, level)
    self.level = level

    self.max_health = self.character.get_average_health()
    self.current_health = self.max_health

    self.caster = rnr_utils.is_casting_class(self.character.rnr_class_obj)
    self.action_points = 5 + STAT_STEPS[level]
    self.current_action_points = self.action_points

    my_class = self.character.rnr_class_obj
    self.damage_stat = STAT_STEPS[level]

    if weapon is None:
      if self.caster:
        self.weapon = get_average_magic_weapon_for_level(level)
      else:
        self.weapon = get_average_weapon_for_level(level)
    else:
      self.weapon = weapon

  # Makes all attacks available. Returns damage.
  def make_attacks(self, enemy_defense, average=False):
    damage = 0

    if self.caster:
      num_attacks = 1
    else:
      num_attacks = 1 if self.level < 7 else 2

    chance_to_hit = 1 - ((enemy_defense - self.damage_stat - self.weapon.hit_modifier) / 20)
    if chance_to_hit > 1:
      chance_to_hit = 1
    if chance_to_hit < 0:
      chance_to_hit = 0

    for attack in range(num_attacks):
      use_action_point = False
      # Don't allow "action point use" if the combatant is a caster
      if self.current_action_points > 0 and self.caster is False:
        self.current_action_points -= 1
        use_action_point = True

      if average:
        weapon_damage = self.weapon.get_average_damage(use_action_point=use_action_point)
        # Reduce damage by the chance of missing
        damage += ((weapon_damage + self.damage_stat) * chance_to_hit)
      else:
        weapon_damage = self.weapon.make_attack(use_action_point=use_action_point) + self.damage_stat
        attack_roll = rnr_utils.roll_dice(1,20)
        if attack_roll == 20:
          #print("It's a crit!")
          damage += (weapon_damage * 2)
        elif attack_roll + self.damage_stat + self.weapon.hit_modifier >= enemy_defense:
            damage += weapon_damage
    #print(f'Dealt {damage} damage!')
    return damage


MONSTER_PROPERTIES = {
  'Monsters' : {
    'Light Monster' : {
      'hits_to_survive' : 2,
      'rounds_to_KO_player' : 3
    },
    'Medium Monster' : {
      'hits_to_survive' : 4,
      'rounds_to_KO_player' : 2.5
    },
    'Heavy Monster' : {
      'hits_to_survive' : 8,
      'rounds_to_KO_player' : 2
    }
  },
  'Villains' : {
    'Villain' : {
      'rounds_to_survive' : 3,
      'rounds_to_KO_player' : 1.5
    }
  }
}

COMMON_CLASSES = None

SPELL_CADENCE = {
  0 : [0,], # Level 0, 1d6
  1 : [0,], # Level 1, 2d4, 1d6 with effect, 1d8
  2 : [1,], # Level 1, 2d4, 1d6 with effect, 1d8
  3 : [1], # Minor offhand spell brings us up a step.
  4 : [1], # Level 2 Spells. 2d8 damage, 3d6
  5 : [2, 0],
  6 : [2, 0], # Level 1 Offhand Spells
  7 : [3, 0], # Level 3 spells. 2d12, 3d8
  8 : [3, 0],
  9 : [3, 0],
  10 : [4, 1], # 3d12, 4d8
  11 : [4, 1], # 3d12, 4d8
  12 : [5, 2],
  13 : [5, 2],
  14 : [5, 2],
  15 : [5, 2]
}



def get_average_weapon_for_level(level):
  if level == 0:
    return rnr_weapon(1,6, hit_modifier=0)
  elif level == 1 or level == 2:
    return rnr_weapon(1,8, hit_modifier=0)
  elif level == 3 or level == 4:
    return rnr_weapon(1,10, hit_modifier=1)
  elif level == 5:
    return rnr_weapon(1,12, hit_modifier=1)
  elif level == 6 or level == 7:
    return rnr_weapon(1,12, 1, 4, hit_modifier=1)
  elif level == 8 or level == 9:
    return rnr_weapon(1,12, 1, 6, hit_modifier=2)
  elif level == 10 or level == 11:
    return rnr_weapon(1,12, 1, 8, hit_modifier=2)
  elif level == 12 or level == 13:
    return rnr_weapon(1,12, 1, 10, hit_modifier=3)
  elif level == 14 or level == 15:
    return rnr_weapon(1,12, 1, 12, hit_modifier=3)


def get_average_magic_weapon_for_level(level):
  # Levels 0-1, Tier 0
  if level < 2:
    return rnr_weapon(2, 6, hit_modifier=0)
  # Levels 2-4, Tier 1
  elif level < 5:
    return rnr_weapon(4, 6, hit_modifier=1)
  # Levels 5-7, Tier 2
  elif level < 8:
    return rnr_weapon(6, 8, hit_modifier=1)
  # Levels 8-9, Tier 3
  elif level < 10:
    return rnr_weapon(8, 8, hit_modifier=2)
  # Levels 10-12, Tier 4
  elif level < 13:
    return rnr_weapon(9, 10, hit_modifier=2)
  # Levels 13-15, Tier 5
  else:
    return rnr_weapon(20, 6, hit_modifier=2)


def get_average_armor_for_level(level, include_base_armor=False):
  base_armor=5 if include_base_armor else 0
  # Levels 0-2
  if level in range(0,3):
    return base_armor + 1
  # 3-4
  elif level in range(3,5):
    return base_armor + 3
  # Levels 5-7
  elif level in range(5,8):
    return base_armor + 4
  # Levels 7-9
  elif level in range(7,10):
    return base_armor + 6
  # Levels 10-12
  elif level in range(10, 13):
    return base_armor + 7
  # Levels 12-15
  else:
    return base_armor + 9

def get_average_armor_for_monster(level):
  global PLAYERS_MISS_RATE, STAT_STEPS
  hit_modifier = get_average_weapon_for_level(level).hit_modifier
  # +1 is necessary due to "meet or exceed" rule
  return (PLAYERS_MISS_RATE * 20) + hit_modifier + STAT_STEPS[level] + 1

def get_average_monster_attack_bonus_for_level(level):
  global MONSTERS_MISS_RATE
  player_armor = get_average_armor_for_level(level, include_base_armor=True)
  # -1 SHOULD be necessary due to "meet or exceed" rule, but player armor already takes it into account.
  return -(MONSTERS_MISS_RATE * 20) + player_armor

def get_hit_rate(bonus, armor):
  # +.05 is necessary due to "meet or exceed" rule
  return round(1 - ((armor-bonus) / 20) + .05, 2)

def run_game(players, level, required_health, armor, chatty= False, max_rounds=20):
  monster_curr_health = required_health
  combatants = []
  for race_name, subrace_name, class_name, subclass_name in players:
    combatants.append(rnr_combatant(level, race_name, subrace_name, class_name, subclass_name))

  rounds_survived = 0
  while monster_curr_health > 0 and rounds_survived < max_rounds:
    if chatty:
      print('#####################################')
      print(f'Round {rounds_survived + 1}')
      print(f'Monster Health: {monster_curr_health} Monster Armor {armor}')
    for combatant in combatants:
      damage = combatant.make_attacks(average=False, enemy_defense=armor)
      monster_curr_health -= damage
      if chatty:
        print(f'Combatant dealt {damage} damage to the enemy ({monster_curr_health} remaining)')
      if monster_curr_health <= 0:
        break
    rounds_survived += 1
  return rounds_survived if rounds_survived < max_rounds else 10000000

def theoretical_survivability(title, players, num_rounds_to_simulate=5):
  global STAT_STEPS, BUFFER

  BUFFER.start_heading(f'{title}', 4)
  BUFFER.paragraph(f'Assuming 1 Monster vs {len(players)} Player Combat')

  rounds_survived = [ x for x in range(1, num_rounds_to_simulate+1)]
  rounds_survived_strings = [f'{x-1} Rounds Survived' for x in rounds_survived]

  BUFFER.chart_title(['Player Level',] + rounds_survived_strings)
  ret = dict()
  for level in range(15+1):
    ret[level] = [0 for i in range(num_rounds_to_simulate + 1)]

    for race_name, subrace_name, class_name, subclass_name in players:
      combatant = rnr_combatant(level, race_name, subrace_name, class_name, subclass_name)
      for r in range(num_rounds_to_simulate + 1):
        dmg =  combatant.make_attacks(get_average_armor_for_monster(level), average=True)
        if r > 0 and ret[level][r] == 0:
          ret[level][r] += ret[level][r-1]
        ret[level][r] += dmg
    BUFFER.chart_row([level,] + ret[level])
  BUFFER.add_whitespace()
  return ret

def simulated_survivability_tuning(title, players, theoretical_survivability_data, num_rounds_to_simulate=5):
  global PLAYERS_MISS_RATE
  ret = {}
  # Optimal is around 500 (will terminate early in most cases)
  tuning_iterations = 500
  # optimal is around 100
  num_games_per_tuning = 100

  BUFFER.start_heading(f'Tuned {title}', 4)
  BUFFER.chart_title(['Party Level', 'Target Rounds Survived', 'Simulated Rounds Survived', 'Requested Monster Health', 'Improved Monster Health', 'Requested Monster Armor', 'Improved Monster Armor', 'Expected Hit Rate'])

  for level in range(15+1):
    ret[level] = {}
    leveled_combatant = rnr_combatant(level, 'Human', 'Human', 'Fighter', 'Telepath')
    attack_bonus = leveled_combatant.damage_stat + leveled_combatant.weapon.hit_modifier
    for r in range(1, num_rounds_to_simulate+1):
      starting_health = theoretical_survivability_data[level][r]
      starting_defense = get_average_armor_for_monster(level)
      health = theoretical_survivability_data[level][r]
      defense = get_average_armor_for_monster(level)
      common_weapon = get_average_weapon_for_level(level)

      closest_round_count_distance = 100000
      closest_round_count = 1000000
      closest_health = health
      closest_defense = defense
      defense_change = 0
      # For 10 tuning iterations, run 100 games, then tweak then tweak the armor/damage of the monster
      for i in range(tuning_iterations):
        survivability = list()
        for game in range(num_games_per_tuning):
          survivability.append(run_game(players, level, health, defense))

        average_rounds_survived = sum(survivability) / len(survivability)
        difference = r - average_rounds_survived
        if abs(difference) < closest_round_count_distance:
          closest_round_count_distance = abs(difference)
          closest_round_count = average_rounds_survived
          closest_health = health
          closest_defense = defense
        # We need to survive less

        hit_rate = get_hit_rate(attack_bonus, defense)
        epsilon = 0
        if difference > epsilon:
          # Clamp hit rate between 55 and 85% 75 = 15
          if (rnr_utils.roll_dice(1,4) <= 2 or hit_rate > .8) and hit_rate > .7:
            defense += 1
            defense_change += 1
          else:
            health += common_weapon.make_attack()
        # We need to survive longer
        elif difference < -epsilon:
          # Clamp hit rate between 55 and 85%
          if (rnr_utils.roll_dice(1,4) == 4 or hit_rate < .7 ) and hit_rate < .8:
            defense -= 1
            defense_change -= 1
          else:
            health -= common_weapon.make_attack()
        else:
          break
      expected_miss_rate =  get_hit_rate(attack_bonus, closest_defense)# PLAYERS_MISS_RATE + (.05 * defense_change)
      ret[level][r] = {'health' : closest_health, 'defense' : closest_defense, 'expected_player_miss_rate' : expected_miss_rate}
      BUFFER.chart_row([level, r, closest_round_count, starting_health, closest_health, starting_defense, closest_defense, expected_miss_rate])
      print(f'Tuned level {level} round {r} in {i} iterations')
    print(f'Finished tuning level {level}')
  BUFFER.add_whitespace()
  return ret

# DON'T CALL, HELPER
def monster_template(monster_name, rounds_to_survive, rounds_to_ko_player, tuned_survivability):
  global BUFFER, COMMON_CLASSES
  fighter = COMMON_CLASSES['Human Fighter']
  BUFFER.chart_title(['Party Level', f'{monster_name} Health', f'{monster_name} Defense', f'{monster_name} Damage', 'Accuracy Bonus', 'Player Hit Rate'])

  for level in range(15+1):
    leveled_combatant = rnr_combatant(level, 'Human', 'Human', 'Fighter', 'Telepath')
    attack_bonus = leveled_combatant.damage_stat + leveled_combatant.weapon.hit_modifier

    survivability = tuned_survivability[level][rounds_to_survive]
    health = math.ceil(survivability['health'])
    defense = survivability['defense']
    accuracy_bonus = get_average_monster_attack_bonus_for_level(level)

    player_health = rnr_utils.get_average_health_to_level(fighter.character.health_dice, level)
    target = math.ceil(player_health / rounds_to_ko_player)

    num,dice,mod = make_dice(target, use_two=True)
    atk = f'{num}d{dice}' if mod == 0 else f'{num}d{dice} +{mod}'
    attack_str = f'{atk} ({num * (dice//2 + .5) + mod})'

    BUFFER.chart_row([level, health, defense, attack_str, accuracy_bonus, get_hit_rate(attack_bonus, defense)])
  BUFFER.add_whitespace()


# By default, this function maximizes accuracy
def make_dice(target, use_twenty=False, use_two=False, allow_mods=True):
  dice = [4, 6, 8, 10, 12]

  if use_two:
    dice.append(2)

  if use_twenty:
    dice.append(20)

  best_accuracy = 100000
  best_num = best_die = best_mod = 0
  for die in dice:
    n, m = meet_target_using_dice(target, die)
    if not allow_mods:
      m = 0
    difference_cost = abs(target - (n* ((die // 2) + .5) + m))
    dice_cost = n if n > 0 else 10
    mod_cost = 0
    if m > 3:
      mod_cost = 2 ** (m-3)
    accuracy = dice_cost + difference_cost + mod_cost

    # print(f'Target: {n}d{die} ({n*((die//2) + .5)} vs target, {target}) COST: {difference_cost} + {dice_cost} = {accuracy}')
    # We want to use few dice
    # We want to be reasonably accurate.

    # We want a balance of these things.
    # Cost is N for number of dice.
    # difference * 10

    if accuracy < best_accuracy:
      best_accuracy = accuracy
      best_num = n
      best_die = die
      best_mod = m
  return best_num, best_die, best_mod

def meet_target_using_dice(target, dice):
  avg_roll = (dice // 2) + .5
  num = math.floor(target / avg_roll)
  modifier =  math.ceil(target - (num*avg_roll))
  return num, modifier

def generate_dc_matrix(dice_size=20):
  matrix = dict()
  adv_matrix = dict()
  dis_matrix = dict()
  modifiers = [x for x in range(-3, 6)]

  for modifier in modifiers:
    for target in range(2, 26):
      for mat in (matrix, adv_matrix, dis_matrix):
        if not target in mat:
          mat[target] = dict()

      max_roll = target - modifier - 1
      probability = min(1,max(0,max_roll / dice_size))

      matrix[target][modifier] = round(1 - probability, 4)
      adv_matrix[target][modifier] = round(1 - (probability * probability), 4)

      dis_numerator = max(0, (dice_size + 1) - (target - modifier))
      dis_probability = round(min(1,max(0,(dis_numerator/dice_size) ** 2)),4)
      dis_matrix[target][modifier] = dis_probability

  return matrix, adv_matrix, dis_matrix

################################################
#
# MARKDOWN GENERATION FUNCTIONS
#
###############################################

def avg_player_health():
  global BUFFER, COMMON_CLASSES
  sprout_wizard = COMMON_CLASSES['Sprout Wizard'].character.health_dice
  human_fighter = COMMON_CLASSES['Human Fighter'].character.health_dice
  automaton_barbarian = COMMON_CLASSES['Automaton Barbarian'].character.health_dice

  BUFFER.start_heading('Average Player Health', 4)
  BUFFER.chart_title(["Level", 'Sprout Wizard', 'Human Fighter', 'Automaton Barbarian' ])
  for level in range(15 + 1):
    health_vals = list()
    for health_dice in [sprout_wizard, human_fighter, automaton_barbarian]:
      health_vals.append(rnr_utils.get_average_health_to_level(health_dice, level))
    BUFFER.chart_row([level,] + health_vals)

  BUFFER.add_whitespace()

def max_player_health():
  global BUFFER, COMMON_CLASSES
  sprout_wizard = COMMON_CLASSES['Sprout Wizard'].character.health_dice
  human_fighter = COMMON_CLASSES['Human Fighter'].character.health_dice
  automaton_barbarian = COMMON_CLASSES['Automaton Barbarian'].character.health_dice

  BUFFER.start_heading('Maximum Player Health', 4)
  BUFFER.chart_title(["Level", 'Sprout Wizard', 'Human Fighter', 'Automaton Barbarian' ])
  for level in range(15 + 1):
    health_vals = list()
    for health_dice in [sprout_wizard, human_fighter, automaton_barbarian]:
      health_vals.append(rnr_utils.get_max_health_to_level(health_dice, level))
    BUFFER.chart_row([level,] + health_vals)

  BUFFER.add_whitespace()

def average_damage_output(crit=False):
  global COMMON_CLASSES, BUFFER

  compute_average = not crit

  # TODO: Add mages back
  BUFFER.start_heading('Average Player Damage',4)
  BUFFER.chart_title(['Level', 'Melee', 'Melee w/ Action Points', 'Caster'])
  for level in range(15+1):
    fighter = COMMON_CLASSES['Human Fighter']
    wizard = COMMON_CLASSES['Sprout Wizard']
    fighter.current_action_points = 0
    attack_list = list()
    attack_list.append(fighter.make_attacks(0, average=True) )
    fighter.current_action_points = fighter.action_points
    attack_list.append(fighter.make_attacks(0, average=True) )
    attack_list.append(wizard.make_attacks(0, average=True))
    BUFFER.chart_row([level,] + attack_list)

  BUFFER.add_whitespace()

def player_survivability():
  global BUFFER, COMMON_CLASSES

  rounds = [1,2,3,4,5,6]
  round_strs = [f'{x} Hits' for x in rounds ]

  BUFFER.start_heading("Player Survivability",4)
  BUFFER.chart_title(['Level', 'Character Health'] + round_strs )

  # For every level
  for level in range(15 + 1):
    round_list = list()
    health = rnr_utils.get_average_health_to_level(COMMON_CLASSES['Human Fighter'].character.health_dice, level)
    for num_rounds in rounds:
      # Round up so our attack is a little overpowered.
      target = math.ceil(health / num_rounds)

      num,dice,mod = make_dice(target, use_two=True)
      atk = f'{num}d{dice}' if mod == 0 else f'{num}d{dice} +{mod}'
      append_str = f'{atk} ({num * (dice//2 + .5) + mod})'
      round_list.append(append_str)
    BUFFER.chart_row([level, health] + round_list)

  BUFFER.add_whitespace()

def all_monster_info():
  global BUFFER, MONSTER_PROPERTIES
  # survivability prints and also runs simulation.
  large_player_group = [
    ('Human', 'Human', 'Fighter', 'Telepath'),
    ('Human', 'Human', 'Fighter', 'Telepath'),
    ('Sprout', 'Sprout', 'Wizard', 'Wizard'),
    ('Sprout', 'Sprout', 'Wizard', 'Wizard'),
    ('Automaton', 'Automaton', 'Barbarian', 'Path of Rage Barbarian')
  ]

  small_player_group = [
    ('Human', 'Human', 'Fighter', 'Telepath')
  ]

  boss_stats_raw = theoretical_survivability('Boss Survivability', large_player_group, num_rounds_to_simulate=5)
  monster_stats_raw = theoretical_survivability('Monster Survivability', small_player_group, num_rounds_to_simulate=10)

  boss_stats_refined = simulated_survivability_tuning('Boss Survivability', large_player_group, boss_stats_raw, num_rounds_to_simulate=5)
  monster_stats_refined = simulated_survivability_tuning('Monster Survivability', small_player_group, monster_stats_raw, num_rounds_to_simulate=10)


  rounds_to_survive = MONSTER_PROPERTIES['Villains']['Villain']['rounds_to_survive']
  rounds_to_KO_player = MONSTER_PROPERTIES['Villains']['Villain']['rounds_to_KO_player']
  BUFFER.start_heading("Example Boss Templates",4)
  BUFFER.paragraph(f'All bosses are built to survive {rounds_to_survive} rounds of focused combat and to KO a player in {rounds_to_KO_player} rounds.')
  BUFFER.paragraph('It is understood that most bosses should have a number of monster minions.')
  BUFFER.paragraph('Bosses should also have some cool, unique abilities to make them stand out and be more interesting to fight.')
  BUFFER.add_whitespace()
  monster_template("Boss", rounds_to_survive, rounds_to_KO_player, boss_stats_refined)
  BUFFER.add_whitespace()

  hits_to_survive = MONSTER_PROPERTIES['Monsters']['Light Monster']['hits_to_survive']
  rounds_to_KO_player = MONSTER_PROPERTIES['Monsters']['Light Monster']['rounds_to_KO_player']
  BUFFER.start_heading("Example Light Monster Templates",4)
  BUFFER.paragraph(f'All light monsters are built to survive {hits_to_survive} action point hits from a player and to KO a player in {rounds_to_KO_player} hits.')
  BUFFER.paragraph('It is understood that multiple light monsters should be deployed together against a party.')
  BUFFER.paragraph('All monsters should also have some cool, unique abilities to make them stand out and be more interesting to fight.')
  BUFFER.paragraph('To fight a party of 4, about 6 light monsters should be deployed to challenge them.')
  BUFFER.paragraph('Remember, however, not every combat has to be life or death. In fact, light monster encounters can be used to wear down a party before a boss fight.')
  BUFFER.add_whitespace()
  monster_template("Light Monster", hits_to_survive, rounds_to_KO_player, monster_stats_refined)
  BUFFER.add_whitespace()

  hits_to_survive = MONSTER_PROPERTIES['Monsters']['Medium Monster']['hits_to_survive']
  rounds_to_KO_player = MONSTER_PROPERTIES['Monsters']['Medium Monster']['rounds_to_KO_player']
  BUFFER.start_heading("Example Medium Monster Templates",4)
  BUFFER.paragraph(f'All medium monsters are built to survive {hits_to_survive} action point hits from a player and to KO a player in {rounds_to_KO_player} hits.')
  BUFFER.paragraph('It is wise to pair light and medium monsters together as a group.')
  BUFFER.paragraph('All monsters should also have some cool, unique abilities to make them stand out and be more interesting to fight.')
  BUFFER.paragraph('Treat a single medium monster as 2 light monsters, and 1/3 of a villain.')
  # BUFFER.paragraph('To fight a party of 4, about 3 heavy monsters should be deployed to challenge them.')
  BUFFER.add_whitespace()
  monster_template("Medium Monster", hits_to_survive, rounds_to_KO_player, monster_stats_refined)
  BUFFER.add_whitespace()

  hits_to_survive = MONSTER_PROPERTIES['Monsters']['Heavy Monster']['hits_to_survive']
  rounds_to_KO_player = MONSTER_PROPERTIES['Monsters']['Heavy Monster']['rounds_to_KO_player']
  BUFFER.start_heading("Example Heavy Monster Templates",4)
  BUFFER.paragraph(f'All heavy monsters are built to survive {hits_to_survive} action point hits from a player and to KO a player in {rounds_to_KO_player} hits.')
  BUFFER.paragraph('It is wise to pair heavy and heavy monsters together as a group.')
  BUFFER.paragraph('All monsters should also have some cool, unique abilities to make them stand out and be more interesting to fight.')
  # BUFFER.paragraph('Treat a single heavy monster as 2 heavy monsters, and 1/3 of a boss.')
  # BUFFER.paragraph('To fight a party of 4, about 3 heavy monsters should be deployed to challenge them.')
  BUFFER.add_whitespace()
  monster_template("Heavy Monster", hits_to_survive, rounds_to_KO_player, monster_stats_refined)
  BUFFER.add_whitespace()

def dice_info():
  global BUFFER
  matrix, adv_matrix, dis_matrix = generate_dc_matrix()
  mods = [f'+{x}' if x >= 0 else f'-{x}' for x in range(-3,6)]

  for title, mat in [('Difficulty Helper: Straight Roll', matrix), ('Difficulty Helper: Advantage', adv_matrix), ('Difficulty Helper: Disadvantage', dis_matrix)]:
    BUFFER.start_heading(title, 4)
    BUFFER.paragraph('Numbers represent the probability of getting __AT LEAST__ the target.')
    BUFFER.chart_title(['Target',] + mods)


    for target in sorted(list(mat.keys())):
      agg = list()
      for modifier in range(-3,6):
        readable = f'{round(mat[target][modifier] * 100,3)}%'
        agg.append(readable)
      BUFFER.chart_row([target,] + agg)
    BUFFER.add_whitespace()

  BUFFER.start_heading('Difficulty Comparison',4)
  BUFFER.paragraph('Numbers represent the probability of getting __AT LEAST__ the target.')
  BUFFER.chart_title(['Target', 'Disadvantage', 'Straight Roll', 'Advantage'])
  for target in sorted(list(matrix.keys())):
    if target > 20:
      continue
    dis_readable = f'{round(dis_matrix[target][0] * 100,2)}%'
    str_readable = f'{round(matrix[target][0] * 100,2)}%'
    adv_readable = f'{round(adv_matrix[target][0] * 100,2)}%'
    BUFFER.chart_row([target, dis_readable, str_readable, adv_readable])
  BUFFER.add_whitespace()

def potions():
  global BUFFER, COMMON_CLASSES

  BUFFER.start_heading('Potion Reference',4)
  BUFFER.chart_title(['Potion Name', 'Potion Effect'])

  fighter = COMMON_CLASSES['Human Fighter']

  fighter_health = {}
  for i in range(15+1):
    fighter_health[i] = rnr_utils.get_average_health_to_level(fighter.character.health_dice, i)

  size_for_level = dict()

  potions = [
              ('Salve', make_dice(fighter_health[15] / 20)),
              ('Minor Health Potion', make_dice(fighter_health[15] / 12)),
              ('Greater Health Potion', make_dice(fighter_health[15] / 8)),
              ('Major Health Potion', make_dice(fighter_health[15] / 4)),
              ('Epic Health Potion', make_dice(fighter_health[15] / 2))
            ]
  for potion_name, potion_effect in potions:
    n,d,m = potion_effect
    BUFFER.chart_row([potion_name, f'{n}d{d} +{m}'])

  BUFFER.start_heading('Health Potions by Player Level', 4)
  BUFFER.paragraph('Small Potions heal on average 1/8th of a players health. Medium restore 1/4th, Large restore 1/2, and Negligible Effect restore less than 1/8th.')
  BUFFER.chart_title(['Potion', 'Effect', 'Small', 'Medium', 'Large', 'Negligible'])

  for health_potion, effect in potions:
    little_health_restored = []
    eighth_health = []
    quarter_health = []
    half_health = []
    for level in range(16):
      if not level in size_for_level:
        size_for_level[level] = dict()
        size_for_level[level]['small']  = list()
        size_for_level[level]['medium'] = list()
        size_for_level[level]['large']  = list()

      if (effect[0] * ((effect[1]//2) + .5)) + effect[2] > fighter_health[level] * .75:
        continue
      if (effect[0] * ((effect[1]//2) + .5)) + effect[2] >= fighter_health[level] * .5:
        size_for_level[level]['large'].append((health_potion, effect))
        half_health.append(f'{level}')
      elif (effect[0] * ((effect[1]//2) + .5)) + effect[2] >= fighter_health[level] * .25:
        size_for_level[level]['medium'].append((health_potion, effect))
        quarter_health.append(f'{level}')
      elif (effect[0] * ((effect[1]//2) + .5)) + effect[2] >= fighter_health[level] * .125:
        size_for_level[level]['small'].append((health_potion, effect))
        eighth_health.append(f'{level}')
      else:
        little_health_restored.append(f'{level}')
    l = ', '.join(little_health_restored)
    e = ', '.join(eighth_health)
    q = ', '.join(quarter_health)
    h = ', '.join(half_health)
    BUFFER.chart_row([health_potion, f'{effect[0]}d{effect[1]} +{effect[2]}', e,q,h,l ])


  BUFFER.start_heading('Potion Availability by Level', 4)
  BUFFER.chart_title(['Level', 'Small Potions', 'Medium Potions', 'Large Potions'])
  for level in range(16):
    lis = size_for_level[level]
    small = list()
    med = list()
    large = list()

    for name, effect in lis['small']:
      small.append( f'{name}' )
    for name, effect in lis['medium']:
      med.append( f'{name}' )
    for name, effect in lis['large']:
      large.append( f'{name}' )
    BUFFER.chart_row([level, ', '.join(small), ', '.join(med), ', '.join(large)])


def main():
  global COMMON_CLASSES

  COMMON_CLASSES = {
    'Sprout Wizard' : rnr_combatant(15, 'Sprout', 'Sprout', 'Wizard', 'Wizard'),
    'Human Fighter' : rnr_combatant(15, 'Human', 'Human', 'Fighter', 'Telepath'),
    'Automaton Barbarian' : rnr_combatant(15, 'Automaton', 'Automaton', 'Barbarian', 'Path of Rage Barbarian')
  }

  avg_player_health()
  max_player_health()
  #recommended_weapon_handouts()
  average_damage_output()
  #average_damage_output(crit=True)
  player_survivability()
  all_monster_info()
  dice_info()
  potions()
  BUFFER.start_heading("Quick Start",2)
  BUFFER.start_heading("Understanding Your Players",3)
  BUFFER.start_heading("Monster Templates",3)
  BUFFER.start_heading("Roll Difficulty",3)

  BUFFER.start_heading("Advanced Understanding",2)
  BUFFER.start_heading("Deeper Dice Roll Probability",3)
  BUFFER.start_heading("Deeper Player Statistics",3)
  BUFFER.start_heading("Building Monsters from Scratch",3)
  BUFFER.start_heading("Simulation Results",3)

  #################################################################
  #
  # Write the Poohbah's Handbook
  #
  #################################################################

  BUFFER.order_next('Poohbah Handbook')

  BUFFER.order_next('Quick Start')

  BUFFER.order_next('Understanding Your Players')
  # BUFFER.order_next('Recommended Weapon Handouts')
  # BUFFER.order_next('Player Survivability')
  BUFFER.order_next('Potion Reference')
  BUFFER.order_next('Potion Availability by Level')

  BUFFER.order_next('Monster Templates')
  BUFFER.order_next('Example Light Monster Templates')
  BUFFER.order_next('Example Medium Monster Templates')
  BUFFER.order_next('Example Heavy Monster Templates')
  BUFFER.order_next('Example Boss Templates')

  BUFFER.order_next('Roll Difficulty')
  BUFFER.order_next('Difficulty Comparison')

  BUFFER.order_next('Advanced Understanding')
  BUFFER.order_next('Deeper Dice Roll Probability')
  BUFFER.order_next('Difficulty Helper: Straight Roll')
  BUFFER.order_next('Difficulty Helper: Advantage')
  BUFFER.order_next('Difficulty Helper: Disadvantage')

  BUFFER.order_next('Deeper Player Statistics')
  BUFFER.order_next('Average Player Health')
  BUFFER.order_next('Maximum Player Health')
  BUFFER.order_next('Average Player Damage')
  BUFFER.order_next('Health Potions by Player Level')

  BUFFER.order_next('Building Monsters from Scratch')
  BUFFER.order_next('Boss Survivability')
  BUFFER.order_next('Monster Survivability')
  #BUFFER.order_next('Monster Survivability, No Action Point Use')
  BUFFER.order_next('Player Survivability')

  BUFFER.order_next('Simulation Results')
  BUFFER.order_next('Tuned Boss Survivability')
  BUFFER.order_next('Tuned Monster Survivability')
  #BUFFER.order_next('Simulated Monster Survivability, No Action Point Use')

  BUFFER.write_toc()
  BUFFER.write_buffer(flush=True)
  BUFFER.verify_empty_buffer()

  potions()


if __name__ == '__main__':
  BUFFER = markdown_handler.markdown_handler("Poohbah Handbook",file=os.path.join(rnr_utils.BASE_DIRECTORY,'docs','helpful_poohbah_stats.md'))
  main()

