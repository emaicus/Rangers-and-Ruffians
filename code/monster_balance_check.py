import rnr_utils
import generate_helpful_poohbah_stats
import json
import os

HUMAN_FIGHTER = rnr_utils.load_combos_given_list([('Human','Human')], [('Fighter','Telepath')], 0)[0]
HEALTH = generate_health(HUMAN_FIGHTER.health_dice)

def generate_health(health_dice):
  ret = dict()
  health = health_dice + 2

  for level in range(15 + 1):
    ret[level] = health
    health += (health_dice // 2) + 2
  return ret

def compute_average_action_point_hit_damage(primary_die, secondary_die):


def validate_creature(monster, health, average_damage_output, expected_type):
  global HEALTH

  print(f'{monster}, HP: {health} Estimated ADPR {average_damage_output}')


  for level in range(0,16):
    # First determine how many action point hits it takes the player to kill the monster
    attacks = rnr_utils.NEW_DMG_STEPS[level]

    for attack in attacks:
      primary_die = 
    # Then determine how many hits it takes the monster to kill the player.

    # See if they fall into any of the specifications.


if __name__ == '__main__':
  rnr_utils.INSTALL_RANGERS_AND_RUFFIANS()
  rnr_utils.printLogo()
  with open(os.path.join(rnr_utils.INSTALL_DIRECTORY, 'book_of_known_beasts.json'), 'r') as infile:
    data = json.load(infile)

  for monster_type, monster_type_data in data.items():
    if monster_type != 'humanoids':
      continue
    for monster_category, monsters in monster_type_data['types'].items():
      if monster_category != 'Bogmen':
        continue
      for monster, stats in monsters['types'].items():
        if monster != 'Bogman':
          continue
        average_damage_output = stats['average_damage_per_round']
        expected_type = stats['type']
        health = stats['health']
        validate_creature(monster, health, average_damage_output, expected_type)