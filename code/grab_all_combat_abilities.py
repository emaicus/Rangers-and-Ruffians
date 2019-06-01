import yaml
import rnr_utils

if __name__ == '__main__':
  rnr_utils.load_Rangers_And_Ruffians_Data()
  combat_abilities = dict()
  for key, value in rnr_utils.ability_dict.items():
    if value["type"] == 'combat':
      combat_abilities[key] = value
    with open('combat_abilities.yml', 'w') as outfile:
      yaml.dump(combat_abilities, outfile, default_flow_style=False)