import unittest
import os
import sys
import pathlib

TEST_DIRECTORY = pathlib.Path(__file__).resolve()
BASE_DIRECTORY = TEST_DIRECTORY.parent.parent
CODE_DIRECTORY = os.path.join(BASE_DIRECTORY, 'src')
sys.path.append(CODE_DIRECTORY)

from rangers_and_ruffians import core
from rangers_and_ruffians import balance_report
from test_utils import test_utils


class rnrTests(unittest.TestCase):

  def setUpClass():
    # empty the log file before tests begin.
    with open('log.txt', 'w') as outfile:
      pass

  def test_ability_existence(self):
        core.load_Rangers_And_Ruffians_Data()
        errors = balance_report.get_non_existent_abilities()
        if len(errors)  > 0:
            test_utils.log_output("Ability Existence", errors)
        self.assertEqual(len(errors), 0 )

  def test_spell_count_number(self):
      core.load_Rangers_And_Ruffians_Data()
      errors = balance_report.evaluate_spells_for_failures(print_errors=False)
      if len(errors) > 0:
          test_utils.log_output("Spell Counts", errors)
      self.assertEqual(len(errors),0)

  def test_ability_types(self):
      core.load_Rangers_And_Ruffians_Data()
      errors = balance_report.check_ability_types(print_errors=False)
      if len(errors) > 0:
          test_utils.log_output("Ability Types", errors)
      self.assertEqual(len(errors),0)


  # def test_description_lengths(self):
  #   core.load_Rangers_And_Ruffians_Data()
  #   errors = balance_report.check_brief_abilities(print_errors=False)
  #   if len(errors) > 0:
  #     test_utils.log_output("Description Lengths", errors, sort=True)
  #   self.assertEqual(len(errors),0)

  # def test_descriptions_for_unescaped_characters(self):
  #   core.load_Rangers_And_Ruffians_Data()
  #   errors = balance_report.check_descriptions(print_errors=False)
  #   if len(errors) > 0:
  #     test_utils.log_output("Descriptions", errors)
  #   self.assertEqual(len(errors),0)

  def test_for_spelling_errors(self):
    core.load_Rangers_And_Ruffians_Data()
    errors = balance_report.spell_check(fix_errors=False, print_errors=False)
    if len(errors.keys()) > 0:
      all_error_list = list()
      for file, errs in errors.items():
        for e in errs:
          all_error_list.append("{0} {1}".format(file, e))
      test_utils.log_output("Spell Check", all_error_list)
    self.assertEqual(len(errors.keys()), 0)

  def test_class_balance(self):
    all_classes = core.load_all_class_objects()
    errors = list()
    for c in all_classes:
      if c.health_die_pieces not in [4, 6, 8, 10]:
        errors.append(f'{c.subclass_name} has {c.health_die_pieces} health die pieces.')

      necessary_set = [2, 1, 1, 0, -1, -2]

      for key, val in c.stat_recommendation.items():
        if val in necessary_set:
          necessary_set.remove(val)
        else:
          errors.append(f'{c.subclass_name} has duplicate or bad stats! {json.dumps(c.stat_recommendation, indent=4)}')
          break

    if len(errors) > 0:
      test_utils.log_output("Class Balance", errors)

    self.assertEqual(len(errors), 0)

  def test_race_balance(self):
    all_races = core.load_all_race_objects()
    errors = list()
    for r in all_races:
      if r.health_die_pieces not in [0,2]:
        errors.append(f'{r.name} has {hp} health die pieces.')

    if len(errors) > 0:
      test_utils.log_output("Race Balance", errors)

    self.assertEqual(len(errors), 0)

  def test_book_of_known_beasts(self):
    core.load_Rangers_And_Ruffians_Data()
    errors = balance_report.check_known_beasts()
    if len(errors) > 0:
      test_utils.log_output("Known Beasts", errors)
    self.assertEqual(len(errors),0)

  def test_pantheon(self):
    core.load_Rangers_And_Ruffians_Data()
    errors = balance_report.check_pantheon()
    if len(errors) > 0:
      test_utils.log_output("Pantheon", errors)
    self.assertEqual(len(errors),0)

  # def test_weapons(self):
  #   core.load_Rangers_And_Ruffians_Data()
  #   errors = balance_report.check_weapons(print_errors=False)
  #   if len(errors) > 0:
  #     test_utils.log_output("Weapons", errors)
  #   self.assertEqual(len(errors),0)


if __name__ == '__main__':
  unittest.main()


