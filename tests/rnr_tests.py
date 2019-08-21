import unittest
import os
import sys
sys.path.append(os.path.abspath('../code'))
import rnr_utils
import rnr_descriptions
import balance_report

def log_output(test, errors):
  log_path = 'log.txt'

  with open(log_path, 'a') as logfile:
    logfile.write('{0}\n'.format(test))
    for error in errors:
      logfile.write("  {0}\n".format(error))

class rnrTests(unittest.TestCase):
  
  def setUpClass():
    # empty the log file before tests begin.
    with open('log.txt', 'w') as outfile:
      pass

  def test_load_files(self):
    try:
      rnr_utils.load_Rangers_And_Ruffians_Data()
    except:
      self.fail("ERROR: Could not load RNR Data")

  def test_ability_existence(self):
    rnr_utils.load_Rangers_And_Ruffians_Data()
    errors = balance_report.get_non_existent_abilities()
    if len(errors)  > 0:
      log_output("Ability Existence", errors)
    self.assertEqual(len(errors), 0 )

  def test_spell_count_number(self):
    rnr_utils.load_Rangers_And_Ruffians_Data()
    errors = balance_report.evaluate_spells_for_failures(print_errors=False)
    if len(errors) > 0:
      log_output("Spell Counts", errors)
    self.assertEqual(len(errors),0)

  def test_spell_count_doubling(self):
    rnr_utils.load_Rangers_And_Ruffians_Data()
    errors = balance_report.evaluate_spells_for_doubling(print_errors=False)
    if len(errors) > 0:
      log_output("Spell Doubling", errors)
    self.assertEqual(len(errors),0)

  def test_description_lengths(self):
    rnr_utils.load_Rangers_And_Ruffians_Data()
    errors = balance_report.check_brief_abilities(print_errors=False)
    if len(errors) > 0:
      log_output("Description Lengths", errors)
    self.assertEqual(len(errors),0)

  def test_descriptions_for_unescaped_characters(self):
    rnr_utils.load_Rangers_And_Ruffians_Data()
    errors = balance_report.check_descriptions(print_errors=False)
    if len(errors) > 0:
      log_output("Descriptions", errors)
    self.assertEqual(len(errors),0)

  def test_for_spelling_errors(self):
    rnr_utils.load_Rangers_And_Ruffians_Data()
    errors = balance_report.spell_check(fix_errors=False, print_errors=False)
    if len(errors.keys()) > 0:
      all_error_list = list()
      for file, errs in errors.items():
        for e in errs:
          all_error_list.append("{0} {1}".format(file, e))
      log_output("Spell Check", all_error_list)
    self.assertEqual(len(errors.keys()), 0)

  def test_class_balance(self):
    all_classes = rnr_utils.load_all_class_objects(level=0)
    errors = list()
    for c in all_classes:
      val = sum(list(c.stats.values()))
      if val != -3:
        errors.append("{0}'s stats sum to {1}".format(c.name, val))
    
    if len(errors) > 0:
      log_output("Class Balance", errors)
    
    self.assertEqual(len(errors), 0)

  def test_race_balance(self):
    all_races = rnr_utils.load_all_race_objects()
    errors = list()
    for r in all_races:
      val = sum(list(r.stats.values()))
      if val != 4:
        errors.append("{0}'s stats sum to {1}".format(r.name, val))

    self.assertEqual(len(errors), 0)

if __name__ == '__main__':
  unittest.main()


