import sys
import os
import json
import math
import json
import random
import markdown_handler

STAT_STEPS = {
  0 : 2,
  1 : 3,
  2 : 3,
  3 : 3,
  4 : 3,
  5 : 3,
  6 : 3,
  7 : 3,
  8 : 4,
  9 : 4,
  10: 4,
  11: 4,
  12: 4,
  13: 4,
  14: 5,
  15: 5
}

RECOMMENDED_WEAPONS = {
  0 : '1d4',
  1 : '1d4 + 1',
  2 : '1d6. Rare 1d4 + 2',
  3 : '1d6 + 1. Rare 1d4 + 3',
  4 : '1d8', # 
  5 : '1d8. Rare 1d6 + 2',
  6 : '1d8 + 1. Rare 1d6 + 3.',
  7 : '1d8 + 1. Rare 1d6 + 3',
  8 : '1d10. Rare 1d8 + 2',
  9 : '1d10 + 1. Rare 1d8 + 3',
  10: '1d12. Rare 1d10 + 2',
  11: '1d12 + 1. Rare 1d10 + 3',
  12: '1d12 + 2',
  13: '1d12 + 3',
  14: '1d12 + 3',
  15: '1d12 + 3'
}

MAGIC_DAMAGE = {
  0 : {
    'damage' : 4,
    'cost' : 0
    },
  1 : {
    'damage' : 8,
    'cost' : 1
    },
  2 : {
    'damage' : 18,
    'cost' : 2
    },
  3 : {
    'damage' : 30,
    'cost' : 2
    },
  4 : {
    'damage' : 48,
    'cost' : 3
    },
  5 : {
    'damage' : 64,
    'cost' : 5
    }
}

STARTING_HEALTH = {
  'Sprout Wizard' : 4,
  'Human Fighter' : 8,
  'Automaton Barbarian' : 12
}

SPELL_CADENCE = {
  0 : [0,], # Level 0, 1d6
  1 : [1,], # Level 1, 2d4, 1d6 with effect, 1d8
  2 : [1,], # Level 1, 2d4, 1d6 with effect, 1d8
  3 : [1, 0], # Minor offhand spell brings us up a step.
  4 : [2, 0], # Level 2 Spells. 2d8 damage, 3d6
  5 : [2, 0], 
  6 : [2, 1], # Level 1 Offhand Spells
  7 : [3, 1], # Level 3 spells. 2d12, 3d8
  8 : [3, 1], 
  9 : [3, 1],
  10 : [4, 1], # 3d12, 4d8
  11 : [4, 1], # 3d12, 4d8
  12 : [4, 2],
  13 : [5, 2],
  14 : [5, 2],
  15 : [5, 2]
}

DMG_STEPS = {
  0 : [{'dice' : 4,'mod' : 0 } ],
  1 : [{'dice' : 4,'mod' : 1 } ], # rare 1d4 + 1 weapons
  2 : [{'dice' : 6,'mod' : 0 } ], # 1d6 weapons and rare 1d4 +2 weapons
  3 : [{'dice' : 6,'mod' : 1 } ], # 1d6 + 1 weapons rare 1d4 + 3 weapons
  4 : [{'dice' : 8,'mod' : 0 } ], # 1d8 weapons
  5 : [{'dice' : 6,'mod' : 2 } ], # 1d8 weapons rare 1d6 + 2 weapons
  6 : [{'dice' : 8,'mod' : 1 } ], # 1d8 weapons + 1 rare 1d6 + 3 weapons
  7 : [{'dice' : 8,'mod' : 1 }, {'dice' : 8,'mod' : 1}], # 1d8 + 1  weapons rare 1d6 + 3 weapons
  8 : [{'dice' : 10,'mod' : 0},{'dice' : 10,'mod' : 0}], # 1d10 weapons. Rare 1d8 + 2 weapons.
  9 : [{'dice' : 10,'mod' : 1},{'dice' : 10,'mod' : 1}], # 1d10 + 1 weapons. Rare 1d8 + 3 weapons
  10: [{'dice' : 12,'mod' : 0},{'dice' : 12,'mod' : 0}], # 1d12 weapons, rare 1d10 + 2 weapons.
  11: [{'dice' : 12,'mod' : 1},{'dice' : 12,'mod' : 1}], # 1d12 + 1 weapons. Rare 1d10 + 3 weapons
  12: [{'dice' : 12,'mod' : 2},{'dice' : 12,'mod' : 2}], # 1d12 + 2 weapons
  13: [{'dice' : 12,'mod' : 3},{'dice' : 12,'mod' : 3}], # 1d12 + 3 weapons
  14: [{'dice' : 12,'mod' : 3},{'dice' : 12,'mod' : 3}], # 1d12 + 3 weapons
  15: [{'dice' : 12,'mod' : 3},{'dice' : 12,'mod' : 3}]  # 1d12 + 3 weapons
}

BUFFER = markdown_handler.markdown_handler("Poohbah Handbook",file=os.path.join('..','docs','helpful_poohbah_stats.md'))


def roll_dice(dice, crit_allowed=True, advantage=False, disadvantage = False, mod=0):
  first_roll  = random.randint(1, dice)
  second_roll = random.randint(1, dice)
  selected_roll = first_roll

  if advantage and not disadvantage:
    selected_roll = max(first_roll, second_roll)
  elif disadvantage and not advantage:
    selected_roll = min(first_roll, second_roll)

  if crit_allowed:
    if selected_roll == dice:
      selected_roll += random.randint(1, dice)
      mod = 2 * mod
  return selected_roll + mod

def run_game(num_combatants, attacks, stat, required_health, armor, chatty=False):
  curr_health = required_health

  rounds_survived = 0
  while curr_health > 0:
    if chatty:
      print('#####################################')
      print(f'Round {rounds_survived + 1}')
      print(f'Monster Health: {curr_health}')
    for i in range(num_combatants):

      for attack in attacks:
        attack_dice = attack['dice']
        attack_mod  = attack['mod']
        damage = roll_dice(attack_dice, mod=attack_mod) - armor + stat
        curr_health -= damage
        if chatty:
          print(f'Combatant {i} dealt {damage} damage to the enemy ({curr_health} remaining)')
        if curr_health <= 0:
          break
      if curr_health <= 0:
        break
    if curr_health > 0:
      rounds_survived += 1
  return rounds_survived

def survivability(title, num_players=1, num_rounds_to_simulate=5, num_games=100, max_armor_bonus=5):
  global DMG_STEPS, STAT_STEPS, BUFFER
  
  BUFFER.start_heading(f'{title}', 4)
  BUFFER.paragraph(f'Assuming 1 Monster vs {num_players} Player Combat')

  rounds_survived = [ x for x in range(1, num_rounds_to_simulate+1)]
  rounds_survived_strings = [f'{x-1} Rounds Survived' for x in rounds_survived]

  BUFFER.chart_title(['Player Level',] + rounds_survived_strings)
  dat = dict()
  for level in range(15+1):
    dat[level] = dict()
    # Compute Damage
    dmg = 0
    for info in DMG_STEPS[level]:
      die = info['dice']
      weapon_mod = info['mod']
      attack = (die / 2) + STAT_STEPS[level] + info['mod']
      dmg +=  attack + .25 * attack
    
    survive_health = list()
    team_dmg = dmg * num_players

    for rounds in rounds_survived:
      # Attack damage + an extra 25% per round
      s_health = (team_dmg + (.01 * team_dmg)) * rounds
      survive_health.append( math.ceil(s_health) )
      dat[level][rounds] = math.ceil(s_health)
    BUFFER.chart_row([level,] + survive_health)
  BUFFER.add_whitespace()


  stats = dict()
  armor_bonus = [x for x in range(max_armor_bonus+1)]
  armor_bonus_str = [f'Rounds Survived with {x} Armor' for x in armor_bonus]
  
  for level, round_data in dat.items():

    stats[level] = dict()
    for rounds_to_survive, required_health in round_data.items():
      stats[level][required_health] = dict()
      for armor in armor_bonus:
        stats[level][required_health][armor] = list()
        for i in range(num_games):

          rounds_survived = run_game(num_players, DMG_STEPS[int(level)], STAT_STEPS[int(level)], required_health, armor, chatty= False)
          stats[level][required_health][armor].append(rounds_survived)

  BUFFER.start_heading(f'Simulated {title}', 4)
  BUFFER.chart_title(['Party Level', 'Monster Health'] + armor_bonus_str)
  
  for level, round_data in stats.items():
    for health, armor_info in round_data.items():
      armor_survivability = list()
      for armor in armor_bonus:
        rounds_survived = armor_info[armor]
        avg_rounds = sum(rounds_survived) / len(rounds_survived)
        armor_survivability.append(avg_rounds)
      BUFFER.chart_row([level, health] + armor_survivability)
  BUFFER.add_whitespace()
  return stats

def make_dice(target):
  dice = [2,4,6,8,10,12]

  # From low to high, see how many dice it takes.
  dmg = 0
  mult = 1

  while dmg < target:
    for die in dice:
      dmg = (mult * (die / 2))
      if dmg >= target:
        return mult, die, 0
      elif dmg + 1 >= target:
        return mult, die, 1
      elif dmg + 2 >= target and die not in [2, 4]:
        return mult, die, 2
      elif dmg + 3 >= target and die not in [2,4,6]:
        return mult, die, 3
      elif target > 25 and dmg + 4 >= target and die not in [2,4,6]:
        return mult, die, 4
      elif target > 25 and dmg + 5 >= target and die not in [2,4,6]:
        return mult, die, 5
    mult += 1
  return mult, die

# If compute_average is false, compute max instead
def choose_attacks(character_level, caster=False, spell_points_to_spend=0, compute_average=True, mage_crit_enabled = False):
  global STAT_STEPS, DMG_STEPS, SPELL_CADENCE, MAGIC_DAMAGE
  
  damage = 0
  have_crit = False

  if caster:
    chosen = list()
    available_spell_levels = SPELL_CADENCE[character_level]
    for attack in range(len(available_spell_levels)):
      chosen_spell_level = available_spell_levels[attack]
      for lvl in range(chosen_spell_level, 0-1, -1):
        if MAGIC_DAMAGE[lvl]['cost'] <= spell_points_to_spend:
          act_dmg = 0
          if compute_average or have_crit:
            act_dmg = MAGIC_DAMAGE[lvl]['damage'] / 2
          else:
            act_dmg = MAGIC_DAMAGE[lvl]['damage']
            have_crit = True
          damage += act_dmg + STAT_STEPS[character_level]
          spell_points_to_spend -= MAGIC_DAMAGE[lvl]['cost']
          break
  else:
    for info in DMG_STEPS[character_level]:
      die = info['dice']
      attack_mod = info['mod']
      if compute_average or have_crit:
        attack = (die / 2) + attack_mod
        if spell_points_to_spend > 0:
          damage += die / 2
          spell_points_to_spend -= 1
      else:
        attack = die + (die / 2) + (2 * attack_mod)
        if spell_points_to_spend > 0:
          damage += die
          spell_points_to_spend -= 1
        have_crit = True
      damage +=  attack

      damage += STAT_STEPS[character_level]
  return math.ceil(damage)

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
  global STARTING_HEALTH, BUFFER
  sprout_wizard = ['Sprout Wizard', STARTING_HEALTH['Sprout Wizard']+2]
  human_fighter = ['Human Fighter', STARTING_HEALTH['Human Fighter']+2]
  automaton_barbarian = ['Automaton Barbarian', STARTING_HEALTH['Automaton Barbarian']+2]

  BUFFER.start_heading('Average Player Health', 4)
  health_data = dict()
  running_health = dict(STARTING_HEALTH)
  BUFFER.chart_title(["Level", sprout_wizard[0], human_fighter[0], automaton_barbarian[0] ])
  for level in range(15 + 1):

    health_vals = list()
    for character, health_dice in [sprout_wizard, human_fighter, automaton_barbarian]:

      if not character in health_data:
        health_data[character] = dict()
      health_data[character][level] = running_health[character]

      health_vals.append(running_health[character])
      running_health[character] += (health_dice // 2) + 2
    BUFFER.chart_row([level,] + health_vals)

  BUFFER.add_whitespace()

def max_player_health():
  global STARTING_HEALTH, BUFFER

  sprout_wizard = ['Sprout Wizard', STARTING_HEALTH['Sprout Wizard']+4]
  human_fighter = ['Human Fighter', STARTING_HEALTH['Human Fighter']+4]
  automaton_barbarian = ['Automaton Barbarian', STARTING_HEALTH['Automaton Barbarian']+4]

  BUFFER.start_heading('Maximum Player Health', 4)
  running_health = dict(STARTING_HEALTH)

  BUFFER.chart_title(["Level", sprout_wizard[0], human_fighter[0], automaton_barbarian[0] ])
  for level in range(15 + 1):

    health_vals = list()
    for character, health_dice in [sprout_wizard, human_fighter, automaton_barbarian]:
      health_vals.append(running_health[character])
      running_health[character] += health_dice  + 4
    BUFFER.chart_row([level,] + health_vals)

  BUFFER.add_whitespace()

def recommended_weapon_handouts():
  global RECOMMENDED_WEAPONS, BUFFER
  BUFFER.start_heading('Recommended Weapon Handouts', 4)
  BUFFER.paragraph('Note: we use +X weapons here, but remember that a +1d4 is on average ~+2, 1d6 is ~+3 etc.')
  BUFFER.chart_title(["Level", "Recommended Weapon Handout"])
  for i in range(15 + 1):
    BUFFER.chart_row([i, RECOMMENDED_WEAPONS[i]])

  BUFFER.add_whitespace()

def average_damage_output(crit=False):
  global STAT_STEPS, BUFFER

  compute_average = not crit

  if not crit:
    BUFFER.start_heading('Average Expected Damage Output Per Round', 4)
    BUFFER.paragraph('Action Points (AP) tend to grant an additional dice of damage.')
    BUFFER.paragraph('For magic users, please recall that many of their spells deal area of effect damage, or else apply a status effect to an enemy.')
  else:
    BUFFER.start_heading('Average Critical Hit Damage Output', 4)
    BUFFER.paragraph('Critical hits are computed as the first (and heaviest) attack is the critical, and subsequent attacks are normal.')
    BUFFER.paragraph('For magic users, please recall that many of their spells deal area of effect damage, or else apply a status effect to an enemy.')
  BUFFER.add_whitespace()

  BUFFER.chart_title(['Level', 'Melee 0SP', 'Melee 1SP', 'Melee 2SP', 'Mage 0SP', 'Mage 1SP', 'Mage 2SP', 'Mage 3SP', 'Mage 4SP', 'Mage 5SP'])
  for level in range(15+1):
    dmg = 0
    spell_points = STAT_STEPS[level] + 5
    attack_list = list()
    attack_list.append(choose_attacks(level, caster=False, spell_points_to_spend=0, compute_average=compute_average))
    attack_list.append(choose_attacks(level, caster=False, spell_points_to_spend=1, compute_average=compute_average))
    attack_list.append(choose_attacks(level, caster=False, spell_points_to_spend=2, compute_average=compute_average))
    attack_list.append(choose_attacks(level, caster=True,  spell_points_to_spend=min(spell_points, 0) , compute_average=compute_average) )
    attack_list.append(choose_attacks(level, caster=True,  spell_points_to_spend=min(spell_points, 1) , compute_average=compute_average) )
    attack_list.append(choose_attacks(level, caster=True,  spell_points_to_spend=min(spell_points, 2) , compute_average=compute_average) )
    attack_list.append(choose_attacks(level, caster=True,  spell_points_to_spend=min(spell_points, 3) , compute_average=compute_average) )
    attack_list.append(choose_attacks(level, caster=True,  spell_points_to_spend=min(spell_points, 4) , compute_average=compute_average) )
    attack_list.append(choose_attacks(level, caster=True,  spell_points_to_spend=min(spell_points, 5) , compute_average=compute_average) )
    BUFFER.chart_row([level,] + attack_list)

  BUFFER.add_whitespace()

# DON'T CALL, HELPER
def generate_fighter_health():
  global BUFFER
  global STARTING_HEALTH
  ret = dict()

  health_dice = STARTING_HEALTH['Human Fighter']
  health = health_dice + 2

  for level in range(15 + 1):
    ret[level] = health
    health += (health_dice // 2) + 2
  return ret

def player_survivability():
  global BUFFER

  rounds = [1,2,3,4,5,6]
  round_strs = [f'{x} Hits' for x in rounds ]

  BUFFER.start_heading("Player Survivability",4)
  BUFFER.chart_title(['Level', 'Character Health'] + round_strs )

  fighter = generate_fighter_health()
  # For every level
  for level in range(15 + 1):
    round_list = list()
    health = fighter[level]
    for num_rounds in rounds:
      # Add 10% to the characters health so that our attack is a little overpowered.
      num,dice,mod = make_dice(health / num_rounds)
      atk = f'{num}d{dice}' if mod == 0 else f'{num}d{dice} +{mod}'
      round_list.append(atk)
    BUFFER.chart_row([level, health] + round_list)

  BUFFER.add_whitespace()

# DON'T CALL, HELPER
def monster_template(monster_name, rounds_to_survive, hits_to_KO_a_player, monster_stats):
  global BUFFER
  BUFFER.chart_title(['Party Level', f'{monster_name} Health', f'{monster_name} Armor', f'{monster_name} Damage'])

  rnr_class = generate_fighter_health()

  for level in range(15 + 1):
    stats = monster_stats[level]
    nearest_val = 1000000
    nearest_health = -1
    nearest_armor = -1
    for health, armor_vals in stats.items():
      for armor, survivability_list in armor_vals.items():

        if level < 2 and armor > 2:
          continue
        if level < 4 and armor > 3:
          continue
        if level < 7 and armor > 4:
          continue

        avg_survivability = sum(survivability_list) / len(survivability_list)
        if abs(avg_survivability - rounds_to_survive) <  nearest_val:
          nearest_val = abs(avg_survivability - rounds_to_survive)
          nearest_health = health
          nearest_armor = armor
    char_health = rnr_class[level]
    num, dice, mod = make_dice(char_health / hits_to_KO_a_player)
    atk = f'{num}d{dice}' if mod == 0 else f'{num}d{dice} +{mod}'
    BUFFER.chart_row([level, nearest_health, nearest_armor, atk])

def all_monster_info():
  global BUFFER
  # survivability prints and also runs simulation.
  boss_stats = survivability('Boss Survivability', num_players=3, num_rounds_to_simulate=5, num_games=100, max_armor_bonus=5)
  monster_stats = survivability('Monster Survivability', num_players=1, num_rounds_to_simulate=5, num_games=10, max_armor_bonus=5)

  rounds_to_survive = 3
  hits_to_KO_a_player = 3
  BUFFER.start_heading("Example Boss Templates",4)
  BUFFER.paragraph(f'All bosses are built to survive {rounds_to_survive} rounds of focused combat and to KO a player in {hits_to_KO_a_player} hits.')
  BUFFER.paragraph('It is understood that most bosses should have a number of monster minions.')
  BUFFER.paragraph('Bosses should also have some cool, unique abilities to make them stand out and be more interesting to fight.')
  BUFFER.add_whitespace()
  monster_template("Boss", rounds_to_survive, hits_to_KO_a_player, boss_stats)
  BUFFER.add_whitespace()

  hits_to_survive = 2
  hits_to_KO_a_player = 4
  BUFFER.start_heading("Example Light Monster Templates",4)
  BUFFER.paragraph(f'All light monsters are built to survive {hits_to_survive} hits from a player and to KO a player in {hits_to_KO_a_player} hits.')
  BUFFER.paragraph('It is understood that multiple light monsters should be deployed together against a party.')
  BUFFER.paragraph('All monsters should also have some cool, unique abilities to make them stand out and be more interesting to fight.')
  BUFFER.paragraph('To fight a party of 4, about 6 light monsters should be deployed to challenge them.')
  BUFFER.paragraph('Remember, however, not every combat has to be life or death. In fact, light monster encounters can be used to wear down a party before a boss fight.')
  BUFFER.add_whitespace()
  monster_template("Light Monster", hits_to_survive, hits_to_KO_a_player, monster_stats)
  BUFFER.add_whitespace()

  hits_to_survive = 4
  hits_to_KO_a_player = 3
  BUFFER.start_heading("Example Heavy Monster Templates",4)
  BUFFER.paragraph(f'All heavy monsters are built to survive {hits_to_survive} hits from a player and to KO a player in {hits_to_KO_a_player} hits.')
  BUFFER.paragraph('It is wise to pair heavy and heavy monsters together as a group.')
  BUFFER.paragraph('All monsters should also have some cool, unique abilities to make them stand out and be more interesting to fight.')
  BUFFER.paragraph('Treat a single heavy monster as 2 heavy monsters, and 1/3 of a boss.')
  BUFFER.paragraph('To fight a party of 4, about 3 heavy monsters should be deployed to challenge them.')
  BUFFER.add_whitespace()
  monster_template("Heavy Monster", hits_to_survive, hits_to_KO_a_player, monster_stats)
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
  global BUFFER

  BUFFER.start_heading('Potion Reference',4)
  BUFFER.chart_title(['Potion Name', 'Potion Effect'])
  
  fighter = generate_fighter_health()
  target = fighter[15]

  size_for_level = dict()

  potions = [ 
              ('Salve',make_dice(target / 20)), 
              ('Minor Health Potion', make_dice(target / 12)),
              ('Greater Health Potion', make_dice(target / 8)),
              ('Major Health Potion', make_dice(target / 4)),
              ('Epic Health Potion', make_dice(target / 2))
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

      if ((effect[0] * effect[1]) / 2) + effect[2] > fighter[level]:
        continue
      if ((effect[0] * effect[1]) / 2) + effect[2] >= fighter[level] / 2:
        size_for_level[level]['large'].append((health_potion, effect))
        half_health.append(f'{level}')
      elif ((effect[0] * effect[1]) / 2) + effect[2] >= fighter[level] / 4:
        size_for_level[level]['medium'].append((health_potion, effect))
        quarter_health.append(f'{level}')
      elif ((effect[0] * effect[1]) / 2) + effect[2] >= fighter[level] / 8:
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
  global STAT_STEPS, RECOMMENDED_WEAPONS, DMG_STEPS

  avg_player_health()
  max_player_health()
  recommended_weapon_handouts()
  average_damage_output()
  average_damage_output(crit=True)
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
  BUFFER.order_next('Recommended Weapon Handouts')
  BUFFER.order_next('Player Survivability')
  BUFFER.order_next('Potion Reference')
  BUFFER.order_next('Potion Availability by Level')

  BUFFER.order_next('Monster Templates')
  BUFFER.order_next('Example Light Monster Templates')
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
  BUFFER.order_next('Average Expected Damage Output Per Round')
  BUFFER.order_next('Average Critical Hit Damage Output')
  BUFFER.order_next('Health Potions by Player Level')

  BUFFER.order_next('Building Monsters from Scratch')
  BUFFER.order_next('Boss Survivability')
  BUFFER.order_next('Monster Survivability')
  BUFFER.order_next('Player Survivability')

  BUFFER.order_next('Simulation Results')
  BUFFER.order_next('Simulated Boss Survivability')
  BUFFER.order_next('Simulated Monster Survivability')

  BUFFER.write_toc()
  BUFFER.write_buffer(flush=True)
  BUFFER.verify_empty_buffer()

  potions()




  


 


if __name__ == '__main__':
  main()