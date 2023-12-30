import yaml
import os
import sys
import traceback
import rnr_balance
from pathlib import Path

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

'''
RNR Spell object.
'''


condition_data = None
BASE_DIRECTORY = Path(__file__).resolve().parent
DATA_PATH = os.path.join(BASE_DIRECTORY, "status_effects.yml")

class status_effect():
  def __init__(self, name, balance, about):
    global Effect_Rankings
    self.name = name
    self.balance = balance 
    self.numeric_balance = int(rnr_balance.get_balance_value('effect_ranking')[balance])
    self.about = about

  #simple constructor
  @classmethod
  def name_constructor(cls, condition_name):
    global condition_data
    if condition_data is None:
        condition_data = dict()
        try:
            with open(DATA_PATH, 'r') as condition_file:
                tmp = yaml.load(condition_file, Loader=Loader)
                for it in tmp:
                    condition_data[it['name'].lower()] = it
        except yaml.YAMLError as exc:
            if hasattr(exc, 'problem_mark'):
                print(f"ERROR: Could not load status_effects.yml. Line: {exc.problem_mark.line} Column: {exc.problem_mark.column}")
                traceback.print_exc()
                sys.exit(1)
        except Exception:
            traceback.print_exc()
            sys.exit(1)

    if condition_name != 'custom':
        my_data = condition_data[condition_name.lower()]
    else: 
        my_data = {
           'name': 'Custom',
           'balance': 'neutral',
           'about': ''
        }

    return cls(my_data['name'], my_data['balance'], my_data['about'])

  def get_markdown(self):
    return self.about