import yaml
import json
import os
import copy

# Used to tear apart the old pantheon, shouldn't be needed any longer.
def pre_process():
  with open('base_cleric.yml', 'r') as infile:
    base_cleric = yaml.load(infile)
  with open('../pantheon.yml', 'r') as infile:
    pantheon = yaml.load(infile)

  # output = dict()
  # output['description'] = base_cleric['description']
  # output['subclasses'] = dict()

  # for diety, data in pantheon.items():
  #   if not data['cleric']:
  #     continue

  new_pantheon = copy.deepcopy(pantheon)
  ability_output = dict()
  encountered_abilities = set()
  for deity, data in pantheon.items():
    if 'abilities' not in data:
      continue

    for level, abilities in data['abilities'].items():
      if not isinstance(abilities, dict):
        print(f"{deity} {level} abilities not a dict")
        continue
      replacement_list = list()
      for key in abilities.keys():
        replacement_list.append(key)
        if key in encountered_abilities:
          print(f"Found multiple {key}. Check that they are identical.")
          continue
        ability_output[key] = abilities[key]
      new_pantheon[deity]['abilities'][level] = list(replacement_list)
  with open('new_pantheon.yml', 'w') as outfile:
    yaml.dump(new_pantheon, outfile, default_flow_style=False)
  with open('discovered_abilities.yml', 'w') as outfile:
    yaml.dump(ability_output, outfile, default_flow_style=False)


if __name__ == '__main__':
  # with open('base_cleric.yml', 'r') as infile:
  #   base_cleric = yaml.load(infile)['Cleric']
  # with open('../pantheon.yml', 'r') as infile:
  #   pantheon = yaml.load(infile)

  # output = dict()
  # output['description'] = base_cleric['description']
  # output['subclasses'] = dict()

  # for diety, cleric_augmentation in pantheon.items():
  #   print(diety)
  #   if not cleric_augmentation['cleric']:
  #     print(f'{diety} has no clerics')
  #     continue
  #   # Get the generic cleric
  #   this_cleric = copy.deepcopy(base_cleric['subclasses']['Cleric'])
  #   this_cleric['description'] = cleric_augmentation['cleric_description']
  #   # Just in case I increase the levels again.
  #   for level in range(0, 100):
  #     level_str = f'level_{level}'
  #     if level_str not in this_cleric['levels'] or level_str not in cleric_augmentation['abilities']:
  #       continue
  #     if not 'abilities' in this_cleric['levels'][level_str] or this_cleric['levels'][level_str]['abilities'] is None:
  #       this_cleric['levels'][level_str]['abilities'] = list()
  #     this_cleric['levels'][level_str]['abilities'] += cleric_augmentation['abilities'][level_str]
  #   cleric_name = f"Cleric of {cleric_augmentation['cleric_tag']}"
  #   output['subclasses'][cleric_name] = copy.deepcopy(this_cleric)

  # true_output = dict()
  # true_output['Cleric'] = output
  # with open('clerics.yml', 'w') as outfile:
  #   yaml.dump(true_output, outfile, default_flow_style=False)
  with open('better_discovered_abilities.yml', 'r') as infile:
    discovered = yaml.load(infile)
  with open('../abilities.yml', 'r') as infile:
    all_abilities = yaml.load(infile)
  all_abilities_set = set(list(all_abilities.keys()))
  discovered_set = set(list(discovered.keys()))

  both = all_abilities_set.intersection(discovered_set)
  for val in both:
    print(val)

  