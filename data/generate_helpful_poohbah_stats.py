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

  running_health = dict(health)
  print_markdown_chart_title(["Level", sprout_wizard[0], human_fighter[0], automaton_barbarian[0] ])
  for level in range(15 + 1):

    health_vals = list()
    for character, health_dice in [sprout_wizard, human_fighter, automaton_barbarian]:
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

  survivability('Boss Survivability', num_players=3, num_rounds_to_simulate=5, num_games=1000, max_armor_bonus=5)
  survivability('Monster Survivability', num_players=1, num_rounds_to_simulate=5, num_games=1000, max_armor_bonus=5)

  # print_markdown_heading('Theoretical Boss Survivability', 2)
  # print_markdown_line('Assuming 1 Monster V 4 Player Combat')
  # print_markdown_line('We make the assumption that, per turn, 1 of the players is unable to hit the boss.')
  # clear_markdown_buffer()

  # rounds_survived = [ 1, 2, 3, 4, 5 ]
  # rounds_survived_strings = [f'{x-1} Rounds Survived' for x in rounds_survived]

  # print_markdown_chart_title(['Player Level',] + rounds_survived_strings)
  # dat = dict()
  # for level in range(15+1):
  #   dat[level] = dict()
  #   # Compute Damage
  #   dmg = 0
  #   for die in dmg_steps[level]:
  #     attack = (die / 2) + stat_steps[level]
  #     dmg +=  attack + .25 * attack
    
  #   survive_health = list()
  #   team_dmg = dmg * 3
    
  #   for rounds in rounds_survived:
  #     # Attack damage + an extra 25% per round
  #     s_health = (team_dmg + (.01 * team_dmg)) * rounds
  #     survive_health.append( math.ceil(s_health) )
  #     dat[level][rounds] = math.ceil(s_health)
  #   print_markdown_chart_row([level,] + survive_health)
  # clear_markdown_buffer()


  # stats = dict()
  # games_played = 1000
  # armor_bonus = [0,1,2,3,4,5]
  # armor_bonus_str = [f'Rounds Survived with {x} Armor' for x in armor_bonus]
  
  # for level, round_data in dat.items():

  #   stats[level] = dict()
  #   for rounds_to_survive, required_health in round_data.items():
  #     stats[level][required_health] = dict()
  #     for armor in armor_bonus:
  #       stats[level][required_health][armor] = list()
  #       for i in range(games_played):

  #         rounds_survived = run_game(3, dmg_steps[int(level)], stat_steps[int(level)], required_health, armor, chatty= False)
  #         stats[level][required_health][armor].append(rounds_survived)

  # print_markdown_heading(f'Simulated Average Rounds Survived by Monsters Over {games_played} Games', 2)



  # print_markdown_chart_title(['Party Level', 'Monster Health'] + armor_bonus_str)
  # for level, round_data in stats.items():
  #   for health, armor_info in round_data.items():
  #     armor_survivability = list()
  #     for armor in armor_bonus:
  #       rounds_survived = armor_info[armor]
  #       avg_rounds = sum(rounds_survived) / len(rounds_survived)
  #       armor_survivability.append(avg_rounds)
  #     print_markdown_chart_row([level, health] + armor_survivability)
  # clear_markdown_buffer()

  ##########################################
  #
  # Monster Survivability
  #
  ##########################################



if __name__ == '__main__':
  main()