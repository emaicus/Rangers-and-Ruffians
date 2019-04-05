import rnr_utils
import random

class combatant:
  def __init__(self, rnr_character, weapon_level):
    self.name = rnr_character.name
    self.abilities = rnr_character.abilities
    self.stats = rnr_character.stats
    self.character = rnr_character
    self.max_health = rnr_character.get_health()
    self.current_health = rnr_character.get_health()
    self.weapon_level = weapon_level
  
  def dead(self):
    if self.current_health <= 0:
      return True
    else:
      return False
  
  def heal(amt):
    self.current_health = min(self.max_health, self.current_health+amt)

class status:
  def __init__(self, duration, disadvantage=False,advantage=False,damage=0,stat_modification={}):
    self.duration = duration
    self.length_so_far = 0
    self.disadvantage = disadvantage
    self.advantage = advantage
    self.damage = damage
    self.stat_modification = dict(stat_modification)

class combat_ability:
  def __init__(self,)


def load_combatants():
  teams = dict()
  teams['party'] = list()
  teams['enemy'] = list()
  elf_ranger = combatant(rnr_utils.rnr_character('', 'elf', 'ranger', 1),6)
  teams['party'].append(elf_ranger)
  human_barbarian = combatant(rnr_utils.rnr_character('', 'human', 'barbarian', 1),6)
  teams['enemy'].append(human_barbarian)
  return teams

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

def roll_dice(max_value, advantage=False,attack=False):
  roll = random.randint(1, max_value)
  if advantage:
    print('rolling with advantage')
    roll = max(roll, random.randint(1,max_value))
  if attack and roll == max_value:
    print('rolled a crit!')
    roll += random.randint(1,max_value)
  print('rolled a total of {0}'.format(roll))
  return roll

def attack(player, enemy):
  damage = roll_dice(player.weapon_level,attack=True) + max(player.stats['Dexterity'], player.stats['Strength'])
  enemy.current_health -= damage
  print("After {0}'s attack, {1} was left with {2} health".format(player.name, enemy.name, enemy.current_health))

def take_turn(player, teams, my_team):
  print("It is {0}'s turn".format(player.name))
  opponents = get_entities_not_on_team(my_team, teams)
  allies = get_entities_on_team(my_team, teams)
  attack(player, random.choice(opponents) )

def battle(teams):
  while True:
    for team in teams:
      enemies = get_entities_not_on_team(team, teams, only_living=True)
      if len(enemies) == 0:
        print('team {0} wins!'.format(team))
        return
      for player in get_entities_on_team(team, teams, only_living=True):
        take_turn(player, teams, team)

def print_combatants(teams):
  print('THE COMBATANTS ARE:')
  for team, players in teams.items():
    print('For team {0}:'.format(team))
    for player in players:
      print('\t{0}, with {1} health and a d{2} weapon'.format(player.name, player.max_health, player.weapon_level))

def main():
  teams = load_combatants()
  print_combatants(teams)
  battle(teams)

if __name__ == '__main__':
  main()