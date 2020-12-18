import yaml
import json
import sys
import os


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

class rnr_race():
    #Base constructor
    def __init__(stats, abilities):



def run_combat()


if __name__ == '__main__':
    run_combat(combatants)