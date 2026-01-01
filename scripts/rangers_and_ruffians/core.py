import json
import sys
import os
import yaml
import traceback
import time
import jsonschema
from tqdm import tqdm
import traceback
from pathlib import Path
from typing import Optional


from .RangersAndRuffians import RangersAndRuffians

CODE_DIRECTORY = Path(__file__).resolve().parent
BASE_DIRECTORY = Path(CODE_DIRECTORY.parent.parent)
INSTALL_DIRECTORY = BASE_DIRECTORY.joinpath('INSTALLED_DATA')
DATA_DIRECTORY = BASE_DIRECTORY.joinpath('data', 'data')
SCHEMA_DIRECTORY = BASE_DIRECTORY.joinpath('data', 'schemas')

GLOBAL_ART_PATH = Path('site', 'images')

#called by load_rangers_and_ruffians_data to install rangers to this directory.
def INSTALL_RANGERS_AND_RUFFIANS(skip_validation : bool) -> None:
  global INSTALL_DIRECTORY
  global DATA_DIRECTORY
  global SCHEMA_DIRECTORY

  INSTALL_DIRECTORY.mkdir(exist_ok=True)
  timestamp_json_path = INSTALL_DIRECTORY.joinpath('timestamps.json')

  try:
    with open(timestamp_json_path, 'r') as infile:
      timestamps = json.load(infile)
  except:
    print('Timestamp json did not exist. Creating one.')
    timestamps = dict()

  if not DATA_DIRECTORY.exists():
    print(f"ERROR! COULD NOT FIND THE DATA DIRECTORY {str(DATA_DIRECTORY)}")
    sys.exit(1)

  # Gather up the list of files we need to install
  reinstall = list()
  print(DATA_DIRECTORY)

  for data_file in DATA_DIRECTORY.glob('*.yml'):
    file_status = data_file.stat()
    modification_time = file_status.st_mtime

    if not data_file.name in timestamps:
      print(f'{data_file.name} not found in timestamps')
      reinstall.append((data_file, f'installing {data_file.name}', modification_time))
    elif modification_time != timestamps[data_file.name]:
      print(f'{data_file.name} is out of date')
      reinstall.append((data_file, f'updating {data_file.name}', modification_time))
    else:
      reinstall.append((data_file, f'always updating {data_file.name}', modification_time))
  

  validator_configuration = None
  with open(SCHEMA_DIRECTORY.joinpath('validator_configuration.json'), 'r') as infile:
    validator_configuration = json.load(infile)
  
  for data_file, schema_file in validator_configuration.items():
    full_data_file_path = DATA_DIRECTORY.joinpath(data_file)
    full_schema_path = SCHEMA_DIRECTORY.joinpath(schema_file)
    
    data_obj = None
    schema_obj = None
    with open(full_data_file_path, 'r') as infile:
      data_obj = yaml.safe_load(infile)
    with open(full_schema_path, 'r') as infile:
      schema_obj = json.load(infile)
    
    try:
      jsonschema.validate(data_obj, schema=schema_obj)
      print(f'{data_file} passed validation.')
    except jsonschema.exceptions.ValidationError as e:
      print(f"ERROR IN {data_file}")
      print(e.relative_path)
      print(e.cause)
      print(f"{e.schema_path}, {e.message}")
      sys.exit(1)
    except Exception:
      traceback.print_exc()
      sys.exit(1)

  # Run validation over all abilities
  ability_schema = None 
  with open(SCHEMA_DIRECTORY.joinpath('ability_schema.json'), 'r') as infile:
    ability_schema = json.load(infile)

  rnr_classes = None
  with open(DATA_DIRECTORY.joinpath('classes.yml'), 'r') as infile:
    rnr_classes = yaml.safe_load(infile)
  
  rnr_races = None 
  with open(DATA_DIRECTORY.joinpath('races.yml'), 'r') as infile:
    rnr_races = yaml.safe_load(infile)
  
  rnr_weapons = None 
  with open(DATA_DIRECTORY.joinpath('weapons.yml'), 'r') as infile:
    rnr_weapons = yaml.safe_load(infile)
  
  monsters = None 
  with open(DATA_DIRECTORY.joinpath('monsters.yml'), 'r') as infile:
    monsters = yaml.safe_load(infile)
  
  status_effects = None 
  with open(DATA_DIRECTORY.joinpath('status_effects.yml'), 'r') as infile:
    status_effects = yaml.safe_load(infile)

  rnr_items = None 
  with open(DATA_DIRECTORY.joinpath('items.yml'), 'r') as infile:
    rnr_items = yaml.safe_load(infile)
  
  if not skip_validation:
    for rnr_race in rnr_races:
      abilities = rnr_race.get('abilities')
      for ability in abilities:
        ability['ability_type'] = 'ability'
        validateAbility(ability, ability_schema, status_effects, rnr_race['name'])
    
    for weapon in rnr_weapons:
      for ability in weapon['abilities']:
        ability['ability_type'] = 'ability'
        validateAbility(ability, ability_schema, status_effects, weapon['name'])
    
    for rnr_item in rnr_items:
      ability = rnr_item['ability']
      ability['ability_type'] = 'ability'
      validateAbility(ability, ability_schema, status_effects, rnr_item['name'])
    
    all_monster_names = set()
    for monster in monsters:
      all_monster_names.add(monster['name'])
      for action_type in ['passive_abilities', 'combat_actions', 'villain_actions', 'lair_actions', 'dynamic_actions']:
        for ability in monster['moveset'].get(action_type, []):
          ability['ability_type'] = 'monster'
          validateAbility(ability, ability_schema, status_effects, monster['name'])

    for rnr_class in rnr_classes:
      expected_spells = 52
      expected_abilities = 25
      count_of_spells = 0
      count_of_abilities = 0
      if 'skill_tree' not in rnr_class:
        print(f"Validating Mage Class: {rnr_class['name']}")
        spellbook = rnr_class.get('spells')
        for tier, tier_spells in spellbook.items():
          for spell_def in tier_spells:
            count_of_spells += 1
            # Tell the schema to evaluate this as a spell.
            spell_def['ability_type'] = 'spell'
            validateAbility(spell_def, ability_schema, status_effects, rnr_class['name'])
        if count_of_spells < expected_spells:
          print(f"{rnr_class['name']} has {count_of_spells} / {expected_spells} spells")
      else:
        print(f"Validating Martial Class: {rnr_class['name']}")
        skill_tree = rnr_class.get('skill_tree')
        for ability_def in skill_tree['abilities']:
          count_of_abilities += 1
          # Tell the schema to evaluate this as an ability.
          ability_def['ability_type'] = 'ability'
          validateAbility(ability_def, ability_schema, status_effects, rnr_class['name'])
        if count_of_abilities < expected_abilities:
          print(f"{rnr_class['name']} has {count_of_abilities} / {expected_abilities} abilities")
    # Check for Summonable Creatures
    summoning_errors = list()
    for rnr_class in rnr_classes:
      if 'skill_tree' not in rnr_class:
        for _, tier_spells in rnr_class['spells'].items():
          for spell_def in tier_spells:
            if 'summoned_creature' not in spell_def:
              continue
            for key in ['tier_1', 'tier_2', 'tier_3', 'all_tiers']:
              if key not in spell_def['summoned_creature']:
                continue 
              creature = spell_def['summoned_creature'][key]
              if creature not in all_monster_names:
                summoning_errors.append(creature)
      else:
        skill_tree = rnr_class.get('skill_tree')
        for ability_def in skill_tree['abilities']:
          if 'summoned_creature' not in spell_def:
            continue
          for key in ['tier_1', 'tier_2', 'tier_3', 'all_tiers']:
            if key not in ability_def['summoned_creature']:
              continue 
            creature = ability_def['summoned_creature'][key]
            if creature not in all_monster_names:
              summoning_errors.append(creature)
      
    if len(summoning_errors) > 0:
      print("The following summoned creatures don't appear in monsters.yml:")
      for monster in summoning_errors:
        print(f"  {monster}")
      #raise KeyError(f"Missing {len(summoning_errors)} summoned monsters.")
                          
  # Iterate over the validated files and install them.
  if len(reinstall) > 0:
    # progress bar.
    pbar = tqdm(reinstall)
    for source, description, mod_time in pbar:
      pbar.set_description(description)
      destination_file = source.with_suffix('.json').name
      destination = INSTALL_DIRECTORY.joinpath(destination_file)
      try:
        convert_yml_file_to_json_file(source, destination)
      except Exception as e:
        print(f"ERROR: Could not install {str(source)} to {str(destination)}")
        traceback.print_exc()
        raise
      timestamps[source.name] = mod_time

      with open(timestamp_json_path, 'w') as outfile:
        json.dump(timestamps, outfile)
    pbar.close()

def convert_json_file_to_yml_file(input_file : Path, output_file : Path) -> None:
  try:
    with open(input_file, 'r') as data_file:
      d = json.load(data_file)
    with open(output_file, 'w') as outfile:
      yaml.safe_dump(d, outfile, default_flow_style=False)
  except Exception as e:
    raise Exception(f"ERROR: could not save {str(input_file)} to {str(output_file)} as a yml file\n{traceback.format_exc()}")

def convert_yml_file_to_json_file(input_file : Path, output_file : Path) -> None:
  try:
    with open(input_file, 'r') as data_file:
      d = yaml.safe_load(data_file)
    with open(output_file, 'w') as outfile:
      json.dump(d, outfile)
  except Exception as e:
    raise Exception(f"ERROR: could not save {str(input_file)} to {str(output_file)} as a yml file\n{traceback.format_exc()}")

def update_version(version_string : str, new_suffix : str) -> str:

  version_number_path = BASE_DIRECTORY.joinpath('meta.json')

  with open(version_number_path) as infile:
    data = json.load(infile)
    current_version = data['version']
    current_suffix = data.get('suffix', '')

  # Split and convert to int
  major, greater, minor = list(map(int, version_string.split('.')))
  current_major, current_greater, current_minor = list(map(int, current_version.split('.')))

  if major == current_major and greater == current_greater and minor == current_minor and current_suffix == new_suffix:
    raise Exception('Called update version with the current version and suffix')

  # If the version number changed (not just a suffix change)
  found_version_increase = False
  if major != current_major or greater != current_greater or minor != current_minor:
    for variable_name, new_version, current_version in [
      ('major', major, current_major),
      ('greater', greater, current_greater),
      ('minor', minor, current_minor)
    ]:
      if found_version_increase:
        if new_version != 0:
          raise Exception(f'Raised a higher tier but did not set {variable_name} to zero.')
        continue

      # Value is too low
      if new_version < current_version:
        raise Exception(f'Attempting to roll back {variable_name} from {current_version} to {new_version}')

      # Value is too big
      if new_version > current_version + 1:
        raise Exception(f'Attempting to increment {variable_name} by more than one step from {current_version} to {new_version}')

      # Version increased by one
      if new_version == current_version +1:
        found_version_increase = True

  #We can safely use the version.
  new_version = f'{major}.{greater}.{minor}'

  with open(BASE_DIRECTORY.joinpath('meta.json'), 'r') as infile:
    data = json.load(infile)

  data['version'] = new_version
  data['suffix'] = new_suffix

  with open(BASE_DIRECTORY.joinpath('meta.json'), 'w') as outfile:
    json.dump(data, outfile, indent=4)
  
  return f"{data['version']} {data['suffix']}"

def load_Rangers_And_Ruffians(skip_validation : bool) -> RangersAndRuffians:
  start = time.time()

  try:
    INSTALL_RANGERS_AND_RUFFIANS(skip_validation)
  except Exception as e:
    print("Critical Error while loading Rangers and Ruffians Data. Aborting")
    traceback.print_exc()
    sys.exit(1)

  class_path = INSTALL_DIRECTORY.joinpath('classes.json')
  race_path = INSTALL_DIRECTORY.joinpath('races.json')
  pantheon_path = INSTALL_DIRECTORY.joinpath('pantheon.json')
  background_path = INSTALL_DIRECTORY.joinpath('backgrounds.json')
  weapon_path = INSTALL_DIRECTORY.joinpath('weapons.json')
  item_path = INSTALL_DIRECTORY.joinpath('items.json')
  monster_path = INSTALL_DIRECTORY.joinpath('monsters.json')
  attribution_path = INSTALL_DIRECTORY.joinpath('art.json')
  version_number_path = BASE_DIRECTORY.joinpath('meta.json')

  with open(version_number_path, 'r') as infile:
    data = json.load(infile)
    version = data['version']
    version_suffix = data['suffix']

  with open(race_path, 'r') as data_file:
    race_data = json.load(data_file)

  with open(class_path, 'r') as data_file:
    class_data = json.load(data_file)

  with open(attribution_path, 'r') as data_file:
    attribution_data = json.load(data_file)

  with open(pantheon_path, 'r') as data_file:
    pantheon_data = json.load(data_file)
  
  with open(background_path, 'r') as data_file:
    background_data = json.load(data_file)
  
  with open(weapon_path, 'r') as data_file:
    weapon_data = json.load(data_file)
  
  with open(item_path, 'r') as data_file:
    item_data = json.load(data_file)    
  
  with open(monster_path, 'r') as data_file:
    monster_data = json.load(data_file)

  finish = time.time()
  print(f'LOAD TIME: {finish - start}(s)')

  return RangersAndRuffians(version, version_suffix, race_data, class_data, attribution_data, monster_data, pantheon_data, background_data, weapon_data, item_data)

####################################################################################
#
# MARKDOWN AND FILE OUTPUT
#
####################################################################################

def printLogo() -> None:
  print()
  print("__________ ")
  print("\\______   \\_____    ____    ____   ___________  ______ ")
  print(" |       _/\\__  \\  /    \\  / ___\\_/ __ \\_  __ \\/  ___/  ")
  print(" |    |   \\ / __ \\|   |  \\/ /_/  >  ___/|  | \\/\\___ \\   ")
  print(" |____|_  /(____  /___|  /\\___  / \\___  >__|  /____  >  ")
  print("        \\/      \\/     \\//_____/      \\/           \\/    ")
  print("                   .___                                ")
  print("_____    ____    __| _/                                ")
  print("\\__  \\  /    \\  / __ |                                 ")
  print(" / __ \\|   |  \\/ /_/ |                                 ")
  print("(____  /___|  /\\____ |                                 ")
  print("     \\/     \\/      \\/                                 ")
  print("__________        _____  _____.__                      ")
  print("\\______   \\__ ___/ ____\\/ ____\\__|____    ____   ______")
  print(" |       _/  |  \\   __\\\\   __\\|  \\__  \\  /    \\ /  ___/")
  print(" |    |   \\  |  /|  |   |  |  |  |/ __ \\|   |  \\___ \\ ")
  print(" |____|_  /____/ |__|   |__|  |__(____  /___|  /____  >")
  print("        \\/                            \\/     \\/     \\/ ")
  print()

def get_gendered_art(relative_art_folder : Path, absolute_art_folder : Path, art_name : str, male : bool) -> tuple[Path, str]:
  global BASE_DIRECTORY
  gender_string = 'male' if male else 'female'

  gender_image =  os.path.join(gender_string, f'{art_name}.jpg')
  neutral_image = f'{art_name}.jpg'

  if os.path.exists(os.path.join(absolute_art_folder, gender_image)):
    path = Path(relative_art_folder, gender_image)
    art_request = f'{art_name}_{gender_string}'
  else:
    path = Path(relative_art_folder, neutral_image)
    art_request = art_name

  markdown_rights = generate_markdown_art_attribution(art_request)

  if markdown_rights is None:
    print(f'could not find rights info for {art_request}.')
    return None, None
  else:
    return path, markdown_rights

def generate_markdown_art_attribution(rnr_game : RangersAndRuffians, art : Path) -> str:

  rights = rnr_game.attributions.get(art,None)

  if rights == None:
    return None

  try:
    title           = rnr_game.attributions[art]['title']
    url             = rnr_game.attributions[art]['url']
    artist          = rnr_game.attributions[art]['artist']
    license_acronym = rnr_game.attributions[art]['license_acronym']
    license_url     = rnr_game.attributions[art]['license_url']
  except Exception as e:
    traceback.print_exc()
    return None

  return f'"[{title}"]({url}) by {artist} is licensed under [{license_acronym}]({license_url})  \n'


def seekCondition(conditionName: str, conditions) -> bool:
  if conditionName.lower() == "custom":
      return True

  found = False
  for condition in conditions:
    if condition['name'].lower() == conditionName:
      found = True
      break 
  return found

def validateAbility(ability: dict, ability_schema: dict, status_effects: list, context: Optional[str]) -> None:

  try:
    jsonschema.validate(ability, schema=ability_schema)
  except jsonschema.exceptions.ValidationError as e:
    print(f"ERROR: {context} {ability.get('name', '')} {e.schema_path}, {e.message}")
    sys.exit(1)
  except Exception:
    traceback.print_exc()
    sys.exit(1)
  if 'effect' in ability:
    for condition in ability['effect']['conditions']:
      if seekCondition(condition, status_effects) == False:
        print(f'WARNING: {context} missing condition {condition}')
  if 'damage_scaling' in ability:
    
    t1 = ability['damage_scaling'].get('tier_1')
    t2 = ability['damage_scaling'].get('tier_2')
    t3 = ability['damage_scaling'].get('tier_3')
    if t1 is not None and t2 is not None and t3 is not None:
      if t1 == t2 and t2 == t3:
        print(f"WARNING: {context} {ability['name']}: All tiers have the same damage")
