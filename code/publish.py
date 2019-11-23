import json
import sys
import os
import rnr_utils
import markdown_handler
from pathlib import Path

VERSION_NUMBER = '2.1.0'

def publish_character_creation():
  global VERSION_NUMBER
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')
  docs_parts_directory = os.path.join(docs_directory, 'parts')
  
  md = markdown_handler.markdown_handler(f'Compendium of Character Creation', heading_level=1, file=os.path.join(docs_directory, 'Compendium_of_Character_Creation.md'))
  md.paragraph(f'_Version {VERSION_NUMBER}_')

  races = rnr_utils.load_all_race_objects()
  rnr_classes = rnr_utils.load_all_class_objects()

  race_lines = []
  for race in sorted(races, key=lambda x: x.name):
    race_lines += race.markdownify()

  class_lines = []
  for rnr_class in sorted(rnr_classes, key=lambda x: x.name):
    class_lines += rnr_class.markdownify()

  skills = rnr_utils.markdown_skills()
  
  md.slurp_topmatter_file(os.path.join(docs_parts_directory, 'topmatter', 'character_creation_topmatter.md'))
  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'character_compendium_start.md'))
  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'race_part.md'))
  md.slurp_markdown_lines(race_lines)
  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'class_part.md'))
  md.slurp_markdown_lines(class_lines)
  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'skills_part.md'))
  md.slurp_markdown_lines(skills)
  
  md._write_topmatter()
  md._write_section(f'Compendium of Character Creation')
  md.write_toc()
  md.write_buffer()

def publish_spells():
  global VERSION_NUMBER
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')
  docs_parts_directory = os.path.join(docs_directory, 'parts')
  
  md = markdown_handler.markdown_handler(f'The Tome of the Ancients', heading_level=1, file=os.path.join(docs_directory, 'Tome_of_the_Ancients.md'))
  md.paragraph(f'_Version {VERSION_NUMBER}_')

  spells = rnr_utils.markdown_spellbooks()

  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'spells_part.md'))
  md.slurp_markdown_lines(spells)

  md._write_section(f'The Tome of the Ancients')
  md.write_toc()
  md.write_buffer()

def publish_examples():
  global VERSION_NUMBER
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')
  docs_parts_directory = os.path.join(docs_directory, 'parts')
  
  md = markdown_handler.markdown_handler(f'The Book of Examples', heading_level=1, file=os.path.join(docs_directory, 'Examples.md'))
  md.paragraph(f'_Version {VERSION_NUMBER}_')


  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'explanations_part.md'))

  md._write_section(f'The Book of Examples')
  md.write_toc()
  md.write_buffer()

def publish_rulebook():
  global VERSION_NUMBER
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')
  docs_parts_directory = os.path.join(docs_directory, 'parts')

  if not os.path.exists(docs_directory):
    print(f"ERROR: cannot find docs directory: {docs_directory}")
    sys.exit(1)

  md = markdown_handler.markdown_handler(f'Rangers and Ruffians Rulebook', heading_level=1, file=os.path.join(docs_directory, 'Rulebook.md'))
  md.paragraph(f'_Version {VERSION_NUMBER}_')

  md.slurp_topmatter_file(os.path.join(docs_parts_directory, 'topmatter', 'rulebook_topmatter.md'))
  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'player_handbook_start.md'))
  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'stat_computation.md'))
  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'character_redirect.md'))
  
  md._write_topmatter()
  md._write_section(f'Rangers and Ruffians Rulebook')
  md.write_toc(max_to_include=3)
  md.write_buffer()

def publish_book_of_known_beasts():
  global VERSION_NUMBER
  rnr_utils.load_Rangers_And_Ruffians_Data()
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')

  md = markdown_handler.markdown_handler(f'Book of Known Beasts', heading_level=1, file=os.path.join(docs_directory, 'Book_of_Known_Beasts.md'))
  md.paragraph(f'_Version {VERSION_NUMBER}_')

  md.slurp_topmatter_file(os.path.join(docs_directory, 'parts', 'topmatter', 'known_beasts_topmatter.md'))

  stats = rnr_utils.standard_stat_order()
  abbreviations = [rnr_utils.abbreviate_stat(stat).upper() for stat in stats]

  lines = []
  for category in sorted(rnr_utils.GLOBAL_BOOK_OF_KNOWN_BEATS.keys()):
    md.start_heading(f"{category.replace('_',' ').title()}:", 2)
    c_info = rnr_utils.GLOBAL_BOOK_OF_KNOWN_BEATS[category]
    
    if 'description' in c_info:
      md.paragraph(f">{c_info['description']}")
      md.add_whitespace()

    if 'tactics' in c_info:
      md.paragraph(f"___{c_info['tactics']}___")
    
    for beast_class in sorted(c_info['types'].keys()):
      md.start_heading(f"{beast_class.replace('_',' ').title()}:", 3)
      b_info = c_info['types'][beast_class]
      
      if 'description' in b_info:
        md.paragraph(f">{b_info['description']}")
        md.add_whitespace()

      if 'tactics' in b_info:
        md.paragraph(f"___{b_info['tactics']}___")

      for beast, info in rnr_utils.GLOBAL_BOOK_OF_KNOWN_BEATS[category]['types'][beast_class]['types'].items():
        md.start_heading(f"{beast.replace('_',' ').title()}:", 4)

        if 'description' in info:
          md.paragraph(f">{info['description']}")
          md.add_whitespace()

        if 'tactics' in info:
          md.paragraph(f"___{info['tactics']}___")


        md.paragraph(f"* ___{info['type']} Enemy___")
        md.paragraph(f"* __Health:__ {info['health']}")

        # This looks gross, but we're looping through stat names and then putting a nice little +/- effective stat.
        my_stats = [ f"{info['stats'][x]} ({'+' if int(info['stats'][x]) >= 0 else ''}{rnr_utils.convert_stat_to_effective_stat(int(info['stats'][x]))})" for x in stats ]

        md.paragraph(f"* __Spell Power:__ { 12 + rnr_utils.convert_stat_to_effective_stat( info['stats']['Inner_Fire'] ) } ")
        md.paragraph(f"* __Movement:__")
        for key, val in info['movement'].items():
          md.paragraph(f"  * __{key.title()}:__ {val} feet")
                #movement_str = '  '.join([f"{key.title()}: _{val}_" for key, val in info['movement'].items() ])

        
        if 'armor' in info:
          md.paragraph(f"* __Armor:__ {info['armor']}")
        if 'magic_armor' in info:
          md.paragraph(f"* __Magic Armor:__ {info['magic_armor']}")

        md.chart_title(abbreviations)
        md.chart_row(my_stats)
        md.add_whitespace()

        if 'abilities' in info:
          md.paragraph("__Abilities:__")
          for ability, description in info['abilities'].items():
            ability_str = f"* __{ability.replace('_', ' ').title()}:__ {description}"
            md.paragraph(ability_str)
          # Reset after abilities
          md.add_whitespace()

        if 'action_spec' in info:
          md.paragraph("__Special Action Rules:__")
          for key, val in info['action_spec'].items():
            md.paragraph(f"* __{key.replace('_', ' ').title()}:__ {val}")
          # Reset after action spec
          md.add_whitespace()


        md.paragraph("__Actions:__")
        for action, a_info in info['actions'].items():
          action_str = f"* __{action.replace('_', ' ').title()}:__"
          if 'damage' in a_info:
            damage_addition = rnr_utils.convert_stat_to_effective_stat(info['stats'][a_info['modifier']])
            action_str = f"{action_str} _{a_info['damage']} + {damage_addition} {a_info['modifier'].replace('_', ' ').title()}._"
          action_str = f"{action_str} {a_info['description']}"
          md.paragraph(action_str)

        # Reset after action
        md.add_whitespace()


        for action_type in ['offhand_actions', 'villain_actions', 'conditional_actions', 'sanctuary_actions']:
          if action_type in info:
            md.paragraph(f"__{action_type.replace('_', ' ').title()}:__")
            for action, description in info[action_type].items():
              md.paragraph(f"* __{action.replace('_', ' ').title()}:__ {description}")
            # Reset after new action type.
            md.add_whitespace()

        # One last reset just in case.
        md.add_whitespace()
        md.paragraph('___')

  md._write_topmatter()
  md._write_section(f'Book of Known Beasts')
  md.write_toc(max_to_include=4)
  md.write_buffer()

def publish_pantheon():
  global VERSION_NUMBER
  rnr_utils.load_Rangers_And_Ruffians_Data()
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')

  md = markdown_handler.markdown_handler(f'Book of Lore', heading_level=1, file=os.path.join(docs_directory, 'Book_of_Lore.md'))
  md.paragraph(f'_Version {VERSION_NUMBER}_')

  md.slurp_topmatter_file(os.path.join(docs_directory, 'parts', 'topmatter', 'lore_topmatter.md'))
  pantheon = rnr_utils.markdown_pantheon()
  md.slurp_markdown_file(os.path.join(docs_directory, 'parts', 'pantheon_part.md'))
  md.slurp_markdown_lines(pantheon)

  md._write_topmatter()
  md._write_section(f'Book of Lore')
  md.write_toc()
  md.write_buffer()
  
def publish_changelog():
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')
  parts_directory = os.path.join(docs_directory, 'parts')
  changelog_directory = os.path.join(parts_directory, 'changelog_parts')

  md = markdown_handler.markdown_handler(f'Changelog', heading_level=1, file=os.path.join(docs_directory, 'Changelog.md'))
  md.slurp_topmatter_file(os.path.join(parts_directory, 'topmatter', 'changelog_topmatter.md'))

  changelogs = list()
  for file in Path(changelog_directory).glob('*.md'):
    name = str(file).split('/')[-1].replace('.md', '')
    major, greater, minor = name.split('_')
    changelogs.append( ( int(major), int(greater), int(minor) ) )

  changelogs = sorted(changelogs, reverse=True)

  for changelog in changelogs:
    major, greater, minor = changelog
    filename = f'{major}_{greater}_{minor}.md'
    md.slurp_markdown_file(os.path.join(changelog_directory, filename))
  
  md._write_topmatter()
  md._write_section(f'Changelog')
  md.write_toc()
  md.write_buffer()

if __name__ == "__main__":
  rnr_utils.printLogo()
  rnr_utils.load_Rangers_And_Ruffians_Data()
  
  publish_rulebook()
  publish_book_of_known_beasts()
  publish_pantheon()
  publish_character_creation()
  publish_spells()
  publish_examples()
  publish_changelog()
  print("Done!")
