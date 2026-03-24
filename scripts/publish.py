import json
import sys
import os
import traceback
import shutil
import argparse
import copy
import pathlib
import shutil


from pathlib import Path

# CODE_DIRECTORY = pathlib.Path(__file__).resolve()
# BASE_DIRECTORY = CODE_DIRECTORY.parent.parent.parent.parent
# CODE_DIRECTORY = os.path.join(BASE_DIRECTORY, 'src')
# sys.path.append(CODE_DIRECTORY)

from rangers_and_ruffians import core
from rangers_and_ruffians import markdown_handler
#from src.rangers_and_ruffians import io_handler
from rangers_and_ruffians import RangersAndRuffians
from rangers_and_ruffians import RnRClass
from rangers_and_ruffians import RnRClass
from rangers_and_ruffians import RnRAbility

#GENERATED_SITE_DIRECTORY = core.BASE_DIRECTORY.joinpath('site', 'pages', 'GENERATED')
GENERATED_DATA_DIRECTORY = core.BASE_DIRECTORY.joinpath('src', 'assets', 'data')


def archive_past_versions():
  version_number_path = core.BASE_DIRECTORY.joinpath('meta.json')

  with open(version_number_path) as infile:
    data = json.load(infile)
    archive_version = data['version']

  docs_directory = os.path.join(core.BASE_DIRECTORY, 'docs')
  archve_directory = os.path.join(docs_directory, 'archive')

  old_version = archive_version.replace('.', '_')

  print(f'searching {docs_directory} for markdown files')
  for file in Path(docs_directory).glob('*.md'):
    name = str(file).split('/')[-1].replace('.md', '')
    name = f'{name}_{old_version}.md'
    print(f'moving {file} to {os.path.join(archve_directory, name)}')
    shutil.move(file, os.path.join(archve_directory, name))


def serialize_conditions():
  input =  core.DATA_DIRECTORY.joinpath('status_effects.yml')
  output = GENERATED_DATA_DIRECTORY.joinpath('conditions.json')
  core.convert_yml_file_to_json_file(input, output)


if __name__ == "__main__":
 
  core.printLogo()

  parser=argparse.ArgumentParser(description="Utility to re-write new versions of the core rulebooks.")
  parser.add_argument('--skip_validation', action='store_true')
  args = parser.parse_args()
  skip_validation = args.skip_validation

  update_version = False
  # Never allow a new version to be built without validation
  if not args.skip_validation:
    try:
      new_version = input('Is this a new edition? If so, what is the new number? ')
      major, greater, minor = new_version.split('.')
      _,_,_ = int(major), int(greater), int(minor)
      update_version = True
      new_suffix = input('What is the version suffix? ')
    except Exception as e:
      print("Not naming a new version.")

    if update_version:
      print('Archiving past versions...')
      archive_past_versions()
      update = core.update_version(new_version, new_suffix)
  
  rnr_game = core.load_Rangers_And_Ruffians(skip_validation=skip_validation)
  
  rnr_game.print_statistics()

  with open(GENERATED_DATA_DIRECTORY.joinpath('monsters.json'), 'w') as outfile:
    json.dump(rnr_game.serialize_monsters(), outfile)
  
  with open(GENERATED_DATA_DIRECTORY.joinpath('items.json'), 'w') as outfile:
    json.dump(rnr_game.serialize_items(), outfile)
  
  with open(GENERATED_DATA_DIRECTORY.joinpath('backgrounds.json'), 'w') as outfile:
    json.dump(rnr_game.serialize_backgrounds(), outfile)
  
  with open(GENERATED_DATA_DIRECTORY.joinpath('races.json'), 'w') as outfile:
    json.dump(rnr_game.serialize_races(), outfile)
  
  with open(GENERATED_DATA_DIRECTORY.joinpath('classes.json'), 'w') as outfile:
    json.dump(rnr_game.serialize_classes(), outfile)
  
  with open(GENERATED_DATA_DIRECTORY.joinpath('attributions.json'), 'w') as outfile:
    json.dump(rnr_game.serialize_attributions(), outfile)
  
  serialize_conditions()
