import unittest
import os
import sys
sys.path.append(os.path.abspath('../code'))
import rnr_utils
import rnr_descriptions
import balance_report

def log_output(test, errors, sort=False):
  log_path = 'log.txt'

  with open(log_path, 'a') as logfile:
    logfile.write('{0}\n'.format(test))
    if sort:
      errors = sorted(errors)
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

  def test_ability_types(self):
    rnr_utils.load_Rangers_And_Ruffians_Data()
    errors = balance_report.check_ability_types(print_errors=False)
    if len(errors) > 0:
      log_output("Ability Types", errors)
    self.assertEqual(len(errors),0)

  def test_description_lengths(self):
    rnr_utils.load_Rangers_And_Ruffians_Data()
    errors = balance_report.check_brief_abilities(print_errors=False)
    if len(errors) > 0:
      log_output("Description Lengths", errors, sort=True)
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
      hp = (c.health_die_pieces - 2) // 2
      if hp != 2 - c.get_stat('luck'):
        errors.append(f'{c.name} has {hp} health die pieces and {c.get_stat("luck")} luck.')

      necessary_set = set([2,1,0,-1,-2,-3])
      
      for key, val in c.stats.items():
        if key.lower() == 'luck':
          continue
        if val in necessary_set:
          necessary_set.remove(val)
        else:
          errors.append(f'{c.name} has duplicate or bad stats! Could not find {val}')
          break
    
    if len(errors) > 0:
      log_output("Class Balance", errors)
    
    self.assertEqual(len(errors), 0)

  def test_race_balance(self):
    all_races = rnr_utils.load_all_race_objects()
    errors = list()
    for r in all_races:
      hp = (r.health_die_pieces - 2) // 2
      if hp != 2 - r.get_stat('luck'):
        errors.append(f'{r.name} has {hp} health die pieces and {r.get_stat("luck")} luck.')


      stat_sum = sum(list(r.stats.values())) - r.get_stat('luck')

      if stat_sum != 0:
        errors.append("{0}'s stats sum to {1}".format(r.name, stat_sum))

    if len(errors) > 0:
      log_output("Race Balance", errors)

    self.assertEqual(len(errors), 0)

  def test_book_of_known_beasts(self):
    rnr_utils.load_Rangers_And_Ruffians_Data()
    errors = balance_report.check_known_beasts()
    if len(errors) > 0:
      log_output("Known Beasts", errors)
    self.assertEqual(len(errors),0)

  def test_pantheon(self):
    rnr_utils.load_Rangers_And_Ruffians_Data()
    errors = balance_report.check_pantheon()
    if len(errors) > 0:
      log_output("Pantheon", errors)
    self.assertEqual(len(errors),0)


if __name__ == '__main__':
  unittest.main()


