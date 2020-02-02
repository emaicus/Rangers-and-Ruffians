import json
import sys
import os
import rnr_utils
import markdown_handler
import traceback
import shutil
from pathlib import Path
import argparse
import copy

GENERATED_SITE_DIRECTORY = os.path.join(rnr_utils.BASE_DIRECTORY, 'new_site', 'pages', 'GENERATED')

MALE = True
FEMALE = False
UNDEFINED = True

# True means male
PREFERRED_IMAGES = {
  'automaton' : UNDEFINED,
  'catterwol' : FEMALE,
  'daemonspawn' : MALE,
  'deep_elf' : FEMALE,
  'dwarf' : MALE,
  'fleetfoot_halfling' : FEMALE,
  'gnome' : FEMALE,
  'goblin' : MALE,
  'hardfoot_halfling' : FEMALE,
  'high_elf' : FEMALE,
  'hissling' : UNDEFINED,
  'human' : MALE,
  'kragraven' : UNDEFINED,
  'lizkin' : MALE,
  'orc' : FEMALE,
  'sprout' : FEMALE,
  'waterborn' : FEMALE,
  'wood_elf' : FEMALE,

  'archer' : FEMALE,
  'barbarian' : FEMALE,
  'bard' : FEMALE,
  'beastmaster' : FEMALE,
  'cleric' : FEMALE,
  'druid' : MALE,
  'fighter' : FEMALE,
  'gunslinger' : MALE,
  'highborn' : MALE,
  'knight' : MALE,
  'monk' : MALE,
  'necromancer' : FEMALE,
  'paladin' : MALE,
  'ranger' : MALE,
  'rogue' : MALE,
  'sorcerer' : MALE,
  'wizard' : MALE,
}

def copyImages():
  races = ('race', rnr_utils.get_all_race_names())
  classes = ('class', rnr_utils.get_all_class_names())

  visited = set()

  for img_type, items in (races, classes):
    for (item, sub_item) in items:
      usable_item = item.lower().replace(' ', '_')
      usable = sub_item.lower().replace(' ', '_')

      if not usable in PREFERRED_IMAGES:
        usable = usable_item

      if usable in visited:
        continue

      if not usable in PREFERRED_IMAGES:
        print(f"No preferred image for {usable}!")
        sys.exit(1)

      male = 'male' if PREFERRED_IMAGES[usable] else 'female'
      source = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs', 'images', img_type, male, f'{usable}.jpg')
      dest   = os.path.join(rnr_utils.BASE_DIRECTORY, 'new_site', 'images', img_type, male, f'{usable}.jpg')

      if not os.path.exists(source):
        print(f"couldn't find {source}")
        source = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs', 'images', img_type, f'{usable}.jpg')
        dest   = os.path.join(rnr_utils.BASE_DIRECTORY, 'new_site', 'images', img_type, f'{usable}.jpg')

      shutil.copy(source, dest)
      visited.add(usable)

def publish_character_creation(force_overwrite):
  global PREFERRED_IMAGES
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')
  docs_parts_directory = os.path.join(docs_directory, 'parts')
  
  md = markdown_handler.markdown_handler(f'Compendium of Character Creation', force_overwrite=force_overwrite, heading_level=1, file=os.path.join(GENERATED_SITE_DIRECTORY, 'Compendium_of_Character_Creation.md'))
  md.paragraph(f'_Version {rnr_utils.VERSION_NUMBER}_')

  rnr_race_wrappers  = rnr_utils.load_all_race_wrappers()
  rnr_class_wrappers = rnr_utils.load_all_class_wrappers()

  race_lines = []
  for race in sorted(rnr_race_wrappers, key=lambda x: x.race_name):
    race_lines += race.markdownify(PREFERRED_IMAGES)

  class_lines = []
  for rnr_class in sorted(rnr_class_wrappers, key=lambda x: x.class_name):
    class_lines += rnr_class.markdownify(PREFERRED_IMAGES)

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

def publish_ancients(force_overwrite):
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')
  docs_parts_directory = os.path.join(docs_directory, 'parts')
  
  md = markdown_handler.markdown_handler(f'The Tome of the Ancients', force_overwrite=force_overwrite, heading_level=1, file=os.path.join(GENERATED_SITE_DIRECTORY, 'Tome_of_the_Ancients.md'))
  md.paragraph(f'_Version {rnr_utils.VERSION_NUMBER}_')

  spells = rnr_utils.markdown_spellbooks()
  
  md.slurp_topmatter_file(os.path.join(docs_parts_directory, 'topmatter', 'ancients_topmatter.md'))
  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'spells_part.md'))
  md.slurp_markdown_lines(spells)
  
  md._write_topmatter()
  md._write_section(f'The Tome of the Ancients')
  md.write_toc()
  md.write_buffer()

def publish_examples(force_overwrite):
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')
  docs_parts_directory = os.path.join(docs_directory, 'parts')
  
  md = markdown_handler.markdown_handler(f'The Book of Examples', force_overwrite=force_overwrite, heading_level=1, file=os.path.join(GENERATED_SITE_DIRECTORY, 'Examples.md'))
  md.paragraph(f'_Version {rnr_utils.VERSION_NUMBER}_')


  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'explanations_part.md'))

  md._write_section(f'The Book of Examples')
  md.write_toc()
  md.write_buffer()

def publish_rulebook(force_overwrite):
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')
  docs_parts_directory = os.path.join(docs_directory, 'parts')

  if not os.path.exists(docs_directory):
    print(f"ERROR: cannot find docs directory: {docs_directory}")
    sys.exit(1)

  md = markdown_handler.markdown_handler(f'Rangers and Ruffians Rulebook', force_overwrite=force_overwrite, heading_level=1, file=os.path.join(GENERATED_SITE_DIRECTORY, 'Rulebook.md'))
  md.paragraph(f'_Version {rnr_utils.VERSION_NUMBER}_')

  md.slurp_topmatter_file(os.path.join(docs_parts_directory, 'topmatter', 'rulebook_topmatter.md'))
  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'player_handbook_start.md'))
  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'stat_computation.md'))
  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'character_redirect.md'))
  
  md._write_topmatter()
  md._write_section(f'Rangers and Ruffians Rulebook')
  md.write_toc(max_to_include=3)
  md.write_buffer()

def publish_book_of_known_beasts(force_overwrite):
  rnr_utils.load_Rangers_And_Ruffians_Data()
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')

  md = markdown_handler.markdown_handler(f'Book of Known Beasts', force_overwrite=force_overwrite, heading_level=1, file=os.path.join(GENERATED_SITE_DIRECTORY, 'Book_of_Known_Beasts.md'))
  md.paragraph(f'_Version {rnr_utils.VERSION_NUMBER}_')

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

def publish_pantheon(force_overwrite):
  rnr_utils.load_Rangers_And_Ruffians_Data()
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')

  md = markdown_handler.markdown_handler(f'Book of Lore', force_overwrite=force_overwrite, heading_level=1, file=os.path.join(GENERATED_SITE_DIRECTORY, 'Book_of_Lore.md'))
  md.paragraph(f'_Version {rnr_utils.VERSION_NUMBER}_')

  md.slurp_topmatter_file(os.path.join(docs_directory, 'parts', 'topmatter', 'lore_topmatter.md'))
  pantheon = rnr_utils.markdown_pantheon()
  md.slurp_markdown_file(os.path.join(docs_directory, 'parts', 'pantheon_part.md'))
  md.slurp_markdown_lines(pantheon)

  md._write_topmatter()
  md._write_section(f'Book of Lore')
  md.write_toc()
  md.write_buffer()

def publish_poohbah_printables(force_overwrite):
  rnr_utils.load_Rangers_And_Ruffians_Data()
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')

  md = markdown_handler.markdown_handler(f'Print Material for Poohbahs', force_overwrite=force_overwrite, heading_level=1, file=os.path.join(GENERATED_SITE_DIRECTORY, 'Poohbah_Printables.md'))
  md.paragraph(f'_Version {rnr_utils.VERSION_NUMBER}_')
  
  md.slurp_topmatter_file(os.path.join(docs_directory, 'parts', 'topmatter', 'skip_topmatter.md'))
  md.slurp_markdown_file(os.path.join(docs_directory, 'parts', 'poohbah_printables_part.md'))

  md._write_topmatter()
  md._write_section(f'Print Material for Poohbahs')
  md.write_buffer()

def publish_printabled_materials(force_overwrite):
  rnr_utils.load_Rangers_And_Ruffians_Data()
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')

  md = markdown_handler.markdown_handler(f'Printed Materials', force_overwrite=force_overwrite, heading_level=1, file=os.path.join(GENERATED_SITE_DIRECTORY, 'Printed_Materials.md'))
  md.paragraph(f'_Version {rnr_utils.VERSION_NUMBER}_')
  
  md.slurp_topmatter_file(os.path.join(docs_directory, 'parts', 'topmatter', 'skip_topmatter.md'))
  md.slurp_markdown_file(os.path.join(docs_directory, 'parts', 'printed_materials.md'))

  md._write_topmatter()
  md._write_section(f'Printed Materials')
  md.write_buffer()
  
def publish_changelog(force_overwrite):
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')
  parts_directory = os.path.join(docs_directory, 'parts')
  changelog_directory = os.path.join(parts_directory, 'changelog_parts')

  md = markdown_handler.markdown_handler(f'Changelog', force_overwrite=force_overwrite, heading_level=1, file=os.path.join(GENERATED_SITE_DIRECTORY, 'Changelog.md'))
  md.slurp_topmatter_file(os.path.join(parts_directory, 'topmatter', 'changelog_topmatter.md'))

  changelogs = list()
  for file in Path(changelog_directory).glob('*.md'):
    name = str(file).split('/')[-1].replace('.md', '')
    major, greater, minor = name.split('_')
    changelogs.append( ( int(major), int(greater), int(minor) ) )

  changelogs = sorted(changelogs, reverse=True)

  i = 0
  for changelog in changelogs:
    major, greater, minor = changelog
    filename = f'{major}_{greater}_{minor}.md'
    header_append = f'-{i}' if i > 0 else ''
    i += 1
    md.slurp_markdown_file(os.path.join(changelog_directory, filename))#, header_append=header_append, prepend=False)
  
  md._write_topmatter()
  md._write_section(f'Changelog')
  md.write_toc(max_to_include=3)
  md.write_buffer()

def archive_past_versions():
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')
  archve_directory = os.path.join(docs_directory, 'archive')

  old_version = rnr_utils.VERSION_NUMBER.replace('.', '_')

  print(f'searching {docs_directory} for markdown files')
  for file in Path(docs_directory).glob('*.md'):
    name = str(file).split('/')[-1].replace('.md', '')
    name = f'{name}_{old_version}.md'
    print(f'moving {file} to {os.path.join(archve_directory, name)}')
    shutil.move(file, os.path.join(archve_directory, name))

def create_alt_all_race_class_json():
  all_race_data = copy.deepcopy(rnr_utils.GLOBAL_RACE_DATA)
  all_class_data = copy.deepcopy(rnr_utils.GLOBAL_CLASS_DATA)
  ability_data = rnr_utils.GLOBAL_ABILITY_DICT

  for race in all_race_data.keys():
    for subrace in all_race_data[race]['subraces'].keys():
      all_race_data[race]['subraces'][subrace]['abilities'] = rnr_utils.filterAbilities(all_race_data[race]['subraces'][subrace]['abilities'])
  
  for rnr_class in all_class_data.keys():
    for subclass in all_class_data[rnr_class]["subclasses"].keys():
      all_class_data[rnr_class]["subclasses"][subclass]["icons"] = rnr_utils.which_icons('', rnr_class)

      if 'base_abilities' in all_class_data[rnr_class]["subclasses"][subclass]:
        all_class_data[rnr_class]["subclasses"][subclass]['base_abilities'] = rnr_utils.filterAbilities(all_class_data[rnr_class]["subclasses"][subclass]['base_abilities'])
      else:
        all_class_data[rnr_class]["subclasses"][subclass]['base_abilities']   = {}
      for level in all_class_data[rnr_class]["subclasses"][subclass]['levels']:
        all_class_data[rnr_class]["subclasses"][subclass]['levels'][level]['abilities'] = rnr_utils.filterAbilities(all_class_data[rnr_class]["subclasses"][subclass]['levels'][level]['abilities'])

  data = {
    'race_names' : rnr_utils.get_all_subrace_names(), 
    'class_names' : rnr_utils.get_all_subclass_names(), 
    'races' : all_race_data,
    'classes' : all_class_data,
    'role_info' : {
      'unique_roles' : [],
      'class_roles' : {},
      'tooltips' : {}
    }
  }
  data["roles"] = dict()
  data["roles"]["class_roles"] = dict()
  unique_roles = set()
  class_objs = rnr_utils.load_all_class_objects()
  for obj in class_objs:
    data["roles"]["class_roles"][obj.name] = {
      "roles" : obj.roles
    }
    unique_roles.update(set(obj.roles))
  
  data["roles"]["unique_roles"] = list(unique_roles)

  tooltips = {
    "tank": "Too big to fall!",
    "low-health": "Squishy, better hide!",
    "self-sufficient": "Self-healing!",
    "nature-based": "Hug the Trees!",
    "undead": "No Longer 6ft. Under!",
    "high-damage": "Vexing Poohbahs Since 2016!",
    "mage": "Simple Magic or Otherwise!",
    "non-magic": "Good Old Fashioned Steel!",
    "spellbooks": "Choose New Spells!",
    "support": "Helpful!",
    "healer": "Every party needs one!",
    "mobile": "Like a chicken with it's head cut off!",
    "ranged": "Stays out of the fray!",
    "area-control": "This is MY ground!",
    "companion-creature": "Because everybody needs a friend!",
    "charismatic": "Because somebody has to be!",
    "sneaky": "A Sneaky Hider!",
    "good-first-class": "Simple to pick up!",
    "complicated": "Lots to pay attention to!"
  }

  tooltip_present = set(tooltips.keys())
  if len(unique_roles - tooltip_present) > 0:
    print("ERROR! Missing tooltips for the following!")
    for item in list(unique_roles - tooltip_present):
      print(item)
    sys.exit(1)

  data["roles"]["tooltips"] = tooltips

  with open( os.path.join(GENERATED_SITE_DIRECTORY, 'ALT.json' ), 'w' ) as outfile:
    json.dump(data, outfile)

def setup_service_worker():
  intended_service_worker_path = os.path.join(rnr_utils.BASE_DIRECTORY, 'service_worker.js')
  code_path = os.path.join(rnr_utils.BASE_DIRECTORY, 'code')

  site_path = os.path.join(rnr_utils.BASE_DIRECTORY, '_site')
  site_service_worker_path = os.path.join(site_path, 'service_worker.js')

  os.chdir(rnr_utils.BASE_DIRECTORY)
  os.system("bundle exec jekyll build")
  os.chdir(site_path)
  os.system("node build.js")
  shutil.copy(site_service_worker_path, intended_service_worker_path)
  os.chdir(code_path)


if __name__ == "__main__":
  rnr_utils.printLogo()
  rnr_utils.load_Rangers_And_Ruffians_Data()

  if not os.path.exists(GENERATED_SITE_DIRECTORY):
    os.mkdir(GENERATED_SITE_DIRECTORY)

  parser=argparse.ArgumentParser(description="Utility to re-write new versions of the core rulebooks.")
  parser.add_argument('--ask', action='store_true')
  args = parser.parse_args()
  force_overwrite = not args.ask

  print(f"Yes is {force_overwrite}")


  update_version = False  
  try:
    new_version = input('Is this a new edition? If so, what is the new number? ')
    major, greater, minor = new_version.split('.')
    _,_,_ = int(major), int(greater), int(minor)
    update_version = True
  except Exception as e:
    print("Not naming a new version.")

  if update_version:
    print('Archiving past versions...')
    archive_past_versions()
    rnr_utils.update_version(new_version)
    print(f"The Version Number is now {rnr_utils.VERSION_NUMBER}")

  copyImages()
  publish_rulebook(force_overwrite)
  publish_book_of_known_beasts(force_overwrite)
  publish_pantheon(force_overwrite)
  publish_character_creation(force_overwrite)
  publish_ancients(force_overwrite)
  publish_examples(force_overwrite)
  publish_changelog(force_overwrite)
  publish_printabled_materials(force_overwrite)
  publish_poohbah_printables(force_overwrite)
  create_alt_all_race_class_json()
  setup_service_worker()
  print("Done!")
