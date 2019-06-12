import yaml

with open('merged_spells.yml') as data_file:
  spell_books = yaml.load(data_file)

empty_spellbooks = dict()

for spell_book, chapters in spell_books.items():
  empty_spellbooks[spell_book] = dict()
  for chapter, spells in chapters.items():
    empty_spellbooks[spell_book][chapter] = dict()

with open('empty_spellbook.yml', 'w') as outfile:
    yaml.dump(empty_spellbooks, outfile)