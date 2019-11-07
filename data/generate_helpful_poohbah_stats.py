import sys
import os
import json
import math
import json
import random

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

DMG_STEPS = {
  0 : [4,],
  1 : [5,], # rare 1d4 + 1 weapons
  2 : [6,], # 1d6 weapons and rare 1d4 +2 weapons
  3 : [7,], # 1d6 + 1 weapons rare 1d4 + 3 weapons
  4 : [8,], # 1d8 weapons
  5 : [8,], # 1d8 weapons rare 1d6 + 2 weapons
  6 : [9,], # 1d8 weapons + 1 rare 1d6 + 3 weapons
  7 : [9, 9], # 1d8 + 1  weapons rare 1d6 + 3 weapons
  8 : [10, 10], # 1d10 weapons. Rare 1d8 + 2 weapons.
  9 : [11, 11], # 1d10 + 1 weapons. Rare 1d8 + 3 weapons
  10: [12, 12], # 1d12 weapons, rare 1d10 + 2 weapons.
  11: [13, 13], # 1d12 + 1 weapons. Rare 1d10 + 3 weapons
  12: [14, 14], # 1d12 + 2 weapons
  13: [15, 15], # 1d12 + 3 weapons
  14: [15, 15], # 1d12 + 3 weapons
  15: [15, 15]  # 1d12 + 3 weapons
}

def print_markdown_heading(heading, level):
  if level <= 0 or level >= 6:
    print("ERROR cannot print heading level {level}")
    sys.exit(1)
  heading = f"{'#' * level} {heading}"
  print(heading)
  print()

def clear_markdown_buffer():
  print()

def print_markdown_line(line):
  print(line)

def print_markdown_chart_row(fields):
  bookend = '|'
  str_fields = [str(x) for x in fields]
  middle = ' | '.join(str_fields)
  print(f'{bookend} {middle} {bookend}')

def print_markdown_chart_title(fields):
  print_markdown_chart_row(fields)

  p = ' | '
  for i in range(len(fields)):
    p += '--------|'
  print(p)

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
        damage = roll_dice(attack, mod=stat) - armor
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
  global DMG_STEPS, STAT_STEPS
  
  print_markdown_heading(f'{title}', 2)
  print_markdown_line(f'Assuming 1 Monster vs {num_players} Player Combat')
  clear_markdown_buffer()

  rounds_survived = [ x for x in range(1, num_rounds_to_simulate+1)]
  rounds_survived_strings = [f'{x-1} Rounds Survived' for x in rounds_survived]

  print_markdown_chart_title(['Player Level',] + rounds_survived_strings)
  dat = dict()
  for level in range(15+1):
    dat[level] = dict()
    # Compute Damage
    dmg = 0
    for die in DMG_STEPS[level]:
      attack = (die / 2) + STAT_STEPS[level]
      dmg +=  attack + .25 * attack
    
    survive_health = list()
    team_dmg = dmg * num_players

    for rounds in rounds_survived:
      # Attack damage + an extra 25% per round
      s_health = (team_dmg + (.01 * team_dmg)) * rounds
      survive_health.append( math.ceil(s_health) )
      dat[level][rounds] = math.ceil(s_health)
    print_markdown_chart_row([level,] + survive_health)
  clear_markdown_buffer()


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

  print_markdown_heading(f'Simulated {title} Over {num_games} Games', 2)

  print_markdown_chart_title(['Party Level', 'Monster Health'] + armor_bonus_str)
  for level, round_data in stats.items():
    for health, armor_info in round_data.items():
      armor_survivability = list()
      for armor in armor_bonus:
        rounds_survived = armor_info[armor]
        avg_rounds = sum(rounds_survived) / len(rounds_survived)
        armor_survivability.append(avg_rounds)
      print_markdown_chart_row([level, health] + armor_survivability)
  clear_markdown_buffer()
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


def main():
  global STAT_STEPS, RECOMMENDED_WEAPONS, DMG_STEPS
  sprout_wizard = ('Sprout Wizard', 4)
  human_fighter = ('Human Fighter', 8)
  automaton_barbarian = ('Automaton Barbarian', 12)

  health = {
    'Sprout Wizard' : 6,
    'Human Fighter' : 10,
    'Automaton Barbarian' : 14
  }
  



  print_markdown_heading("Useful Poohbah Statistics", 1)


  ##########################################
  #
  # AVERAGE HEALTH
  #
  ##########################################

  print_markdown_heading('Average Player Health Values', 2)
  health_data = dict()
  running_health = dict(health)
  print_markdown_chart_title(["Level", sprout_wizard[0], human_fighter[0], automaton_barbarian[0] ])
  for level in range(15 + 1):

    health_vals = list()
    for character, health_dice in [sprout_wizard, human_fighter, automaton_barbarian]:

      if not character in health_data:
        health_data[character] = dict()
      health_data[character][level] = running_health[character]

      health_vals.append(running_health[character])
      running_health[character] += (health_dice // 2) + 2
    print_markdown_chart_row([level,] + health_vals)

  clear_markdown_buffer()

  ##########################################
  #
  # AVERAGE HEALTH
  #
  ##########################################

  print_markdown_heading('Maximum Player Health Values', 2)
  running_health = dict(health)

  print_markdown_chart_title(["Level", sprout_wizard[0], human_fighter[0], automaton_barbarian[0] ])
  for level in range(15 + 1):

    health_vals = list()
    for character, health_dice in [sprout_wizard, human_fighter, automaton_barbarian]:
      health_vals.append(running_health[character])
      running_health[character] += health_dice  + 4
    print_markdown_chart_row([level,] + health_vals)

  clear_markdown_buffer()

  ##########################################
  #
  # Recommended Weapons
  #
  ##########################################


  print_markdown_heading('Recommended Weapon Handouts', 2)
  print_markdown_line('Note: we use +X weapons here, but remember that a +1d4 is on average ~+2, 1d6 is ~+3 etc.')
  clear_markdown_buffer()
  print_markdown_chart_title(["Level", "Recommended Weapon Handout"])
  for i in range(15 + 1):
    print_markdown_chart_row([i, RECOMMENDED_WEAPONS[i]])

  clear_markdown_buffer()


  ##########################################
  #
  # AVG Expected Damage Output
  #
  ##########################################


  print_markdown_heading('Average Expected Damage Output Per Round', 2)
  print_markdown_line('Expected Damage output is computed based on recommended weapon handouts + 25\% additional damage to compensate for abilities.')
  clear_markdown_buffer()

  print_markdown_chart_title(['Level', 'Expected Damage Output'])
  for level in range(15+1):
    dmg = 0
    for die in DMG_STEPS[level]:
      attack = (die / 2) + STAT_STEPS[level]
      dmg +=  attack + (.25 * attack)
    print_markdown_chart_row([level, math.ceil(dmg)])
  
  clear_markdown_buffer()

  ##########################################
  #
  # MAX Expected Damage Output
  #
  ##########################################


  print_markdown_heading('Average Critical Hit Damage Output', 2)
  print_markdown_line('Expected Damage output is computed based on recommended weapon handouts critting + 25\% additional damage to compensate for abilities.')
  clear_markdown_buffer()

  print_markdown_chart_title(['Level', 'Expected Crit Damage Output'])
  for level in range(15+1):
    dmg = 0
    for die in DMG_STEPS[level]:
      attack = die  + (.5 * die) + STAT_STEPS[level]
      dmg +=  attack + .25 * attack
    print_markdown_chart_row([level, math.ceil(dmg)])
  clear_markdown_buffer()


  ##########################################
  #
  # Boss Survivability
  #
  ##########################################

  boss_stats = survivability('Boss Survivability', num_players=3, num_rounds_to_simulate=5, num_games=100, max_armor_bonus=5)
  monster_stats = survivability('Monster Survivability', num_players=1, num_rounds_to_simulate=5, num_games=10, max_armor_bonus=5)

  ##########################################
  #
  # Player Survivability
  #
  ##########################################


  rounds = [1,2,3,4,5,6]
  round_strs = [f'{x} Hits' for x in rounds ]

  print_markdown_heading("Character Survivability",2)
  print_markdown_chart_title(['Level', 'Character Health'] + round_strs )

  # For every level
  rnr_class = health_data['Human Fighter']
  for level in range(15 + 1):
    char_health = rnr_class[level]
    round_list = list()
    for num_rounds in rounds:
      # Add 10% to the characters health so that our attack is a little overpowered.
      num,dice,mod = make_dice(char_health / num_rounds)
      atk = f'{num}d{dice}' if mod == 0 else f'{num}d{dice} +{mod}'
      round_list.append(atk)
    print_markdown_chart_row([level, char_health] + round_list)

  clear_markdown_buffer()

  print_markdown_heading("Example Boss Templates by Level",2)
  print_markdown_line('All bosses are built to survive 3 rounds of focused combat and to KO a player in 3 hits.')
  print_markdown_line('It is understood that most bosses should have a number of monster minions.')
  print_markdown_line('Bosses should also have some cool, unique abilities to make them stand out and be more interesting to fight.')
  clear_markdown_buffer()

  print_markdown_chart_title(['Party Level', 'Boss Health', 'Boss Armor', 'Boss Damage'])

  for level in range(15 + 1):
    stats = boss_stats[level]
    nearest_val = 1000000
    nearest_health = -1
    nearest_armor = -1
    for health, armor_vals in stats.items():
      for armor, survivability_list in armor_vals.items():

        if level < 4 and armor > 3:
          continue
        if level < 7 and armor > 4:
          continue

        avg_survivability = sum(survivability_list) / len(survivability_list)
        if abs(avg_survivability - 3) <  nearest_val:
          nearest_val = abs(avg_survivability - 3)
          nearest_health = health
          nearest_armor = armor
    char_health = rnr_class[level]
    num, dice, mod = make_dice(char_health / 3)
    atk = f'{num}d{dice}' if mod == 0 else f'{num}d{dice} +{mod}'
    print_markdown_chart_row([level, nearest_health, nearest_armor, atk])

  
  print_markdown_heading("Example Light Monster Templates by Level",2)
  print_markdown_line('All light monsters are built to survive 2 hits from a player and to KO a player in 4 hits.')
  print_markdown_line('It is understood that multiple light monsters should be deployed together against a party.')
  print_markdown_line('All monsters should also have some cool, unique abilities to make them stand out and be more interesting to fight.')
  print_markdown_line('To fight a party of 4, about 6 light monsters should be deployed to challenge them.')
  print_markdown_line('Remember, however, not every combat has to be life or death. In fact, light monster encounters can be used to wear down a party before a boss fight.')
  clear_markdown_buffer()

  print_markdown_chart_title(['Party Level', 'Monster Health', 'Monster Armor', 'Monster Damage'])

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
        if abs(avg_survivability - 2) <  nearest_val:
          nearest_val = abs(avg_survivability - 2)
          nearest_health = health
          nearest_armor = armor
    char_health = rnr_class[level]
    num, dice, mod = make_dice(char_health / 4)
    atk = f'{num}d{dice}' if mod == 0 else f'{num}d{dice} +{mod}'
    print_markdown_chart_row([level, nearest_health, nearest_armor, atk])


  print_markdown_heading("Example Heavy Monster Templates by Level",2)
  print_markdown_line('All heavy monsters are built to survive 4 hits from a player and to KO a player in 3 hits.')
  print_markdown_line('It is wise to pair heavy and heavy monsters together as a group.')
  print_markdown_line('All monsters should also have some cool, unique abilities to make them stand out and be more interesting to fight.')
  print_markdown_line('Treat a single heavy monster as 2 heavy monsters, and 1/3 of a boss.')
  print_markdown_line('To fight a party of 4, about 3 heavy monsters should be deployed to challenge them.')
  clear_markdown_buffer()
  print_markdown_chart_title(['Party Level', 'Monster Health', 'Monster Armor', 'Monster Damage'])

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
        if abs(avg_survivability - 4) <  nearest_val:
          nearest_val = abs(avg_survivability - 4)
          nearest_health = health
          nearest_armor = armor
    char_health = rnr_class[level]
    num, dice, mod = make_dice(char_health / 3)
    atk = f'{num}d{dice}' if mod == 0 else f'{num}d{dice} +{mod}'
    print_markdown_chart_row([level, nearest_health, nearest_armor, atk])




if __name__ == '__main__':
  main()