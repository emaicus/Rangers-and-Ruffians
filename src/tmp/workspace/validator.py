import sys
import os
import json
import yaml
import traceback
import argparse
from pathlib import Path
import jsonschema

from rnr_race import rnr_race
from rnr_class import rnr_class

BASE_DIRECTORY = Path(__file__).resolve().parent
RNR_PATH = os.path.join(BASE_DIRECTORY.parent.parent, "Rangers-and-Ruffians", "data")

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def load_schema_file(file_name):
  schema_path = os.path.join(BASE_DIRECTORY, file_name)
  schema = None

  try:
    with open(schema_path, 'r') as schema_file:
      schema = json.load(schema_file)
  except FileNotFoundError:
    print(f"ERROR, could not find {schema_path}")
    sys.exit(1)
  except json.JSONDecodeError:
    print(f"ERROR: Trouble loading {schema_path}")
    traceback.print_exc()
    sys.exit(1)
  except Exception as e:
    traceback.traceback.print_exc()
    sys.exit(1)
  
  print("Schema loaded...")
  return schema

def load_data_file(file_name):
  data_file_path = os.path.join(RNR_PATH, file_name)
  data = None

  try:
    with open(data_file_path, 'r') as races_file:
      data = yaml.load(races_file, Loader=Loader)
  except yaml.YAMLError as exc:
    if hasattr(exc, 'problem_mark'):
      print(f"ERROR: Could not load {file_name}. Line: {exc.problem_mark.line} Column: {exc.problem_mark.column}")
      sys.exit(1)
  except Exception:
    traceback.print_exc()
    sys.exit(1)
  
  return data

def check(schema, objects, output_file, constructor, loud=False):
  with open(output_file, 'w') as outfile:
    for name, obj in objects.items():
      print(name)
      try:
        jsonschema.validate(obj, schema=schema)
        instantiated_race_obj = constructor(name, obj)

        text = instantiated_race_obj.get_markdown()
        outfile.write(f"{text}  \n")
        if args.loud:
          print(f"{text}  \n")
      except jsonschema.exceptions.ValidationError as e:
        print(f"ERROR:")
        print(f'Schema Path: {e.schema_path}')
        print(f'Path: {e.path}')
        print(f'Message: {e.message}')
        print(f'Validator: {e.validator}')
        print(f'Validator Value: {e.validator_value}')
        print(f'Context: {e.context}')
        #traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
  print('Parser booting...')
  
  parser=argparse.ArgumentParser(description="Utility to check spell balance and optionally publish races.")
  parser.add_argument('--loud', action='store_true',help="Write to command line.")
  parser.add_argument('--race', action='store_true',help="Write to command line.")
  parser.add_argument('--class', action='store_true',help="Write to command line.")

  args = parser.parse_args()

  schema = load_schema_file('class_schema.json')
  races = load_data_file('classes.yml')

  check(schema, races, 'classes.md', rnr_class, args.loud)

