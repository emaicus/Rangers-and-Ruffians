import yaml
import os
import argparse
import traceback

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Merge two yml files')
  parser.add_argument('path_1',  help="The first yml")
  parser.add_argument('path_2',  help="The second yml")
  parser.add_argument('output_path',  help="The resultant yml")
  args = parser.parse_args()

  with open(args.path_1) as infile:
    book_1 = yaml.load(infile)

  with open(args.path_2) as infile:
    book_2 = yaml.load(infile)


  for spell_book, contents in book_2.items():
    if not spell_book in book_1:
      book_1[spell_book] = dict()
    for chapter, spells in contents.items():
      if not chapter in book_1[spell_book]:
        book_1[spell_book][chapter] = dict()
      for spell, stats in spells.items():
        if not 'cost' in stats:
          num = chapter.split('_')
          try:
            cost = int(num[1])
            stats['cost'] = cost
          except Exception as e:
            print('exception', chapter)
        if spell in book_1[spell_book][chapter]:
          print('duplicate spell {0}'.format(spell))
        else:
          book_1[spell_book][chapter][spell] = stats

  for spell_book, contents in book_1.items():
    for chapter, spells in contents.items():
      for spell, stats in spells.items():
        if not 'cost' in stats:
          num = chapter.split('_')
          try:
            cost = int(num[1])
            book_1[spell_book][chapter][spell]['cost'] = cost
          except Exception as e:
            print('exception', chapter)

  with open(args.output_path, 'w') as outfile:
    yaml.dump(book_1, outfile, default_flow_style=False)