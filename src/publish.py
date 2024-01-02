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

GENERATED_SITE_DIRECTORY = core.BASE_DIRECTORY.joinpath('site', 'pages', 'GENERATED')


# MALE = True
# FEMALE = False
# UNDEFINED = True

def copyImages(rnr_game : RangersAndRuffians) -> None:
  races = ('race', rnr_game.races)
  classes = ('class', rnr_game.classes)

  print('Installing Images')
  for img_type, races_or_classes in (races, classes):
    for rnr_obj in races_or_classes:
      name = rnr_obj.name.lower().replace(' ', '_')

      source = core.BASE_DIRECTORY.joinpath('docs', 'images', img_type, f'{name}.jpg')
      dest   = core.BASE_DIRECTORY.joinpath('site', 'images', img_type, f'{name}.jpg')

      if source.exists():
        source = os.path.join(core.BASE_DIRECTORY, 'docs', 'images', img_type, f'{name}.jpg')
        dest   = os.path.join(core.BASE_DIRECTORY, 'site', 'images', img_type, f'{name}.jpg')
      else:
        print(f"couldn't find {str(source)}")

      shutil.copy(str(source), str(dest))

      skill_tree_path = core.BASE_DIRECTORY.joinpath('docs', 'images', 'skill_trees', f'{name}.jpg')
      skill_tree_dest = core.BASE_DIRECTORY.joinpath('site', 'images', 'skill_trees', f'{name}.jpg')

      if skill_tree_path.exists():
        print(f"Found a skill tree for {rnr_obj.name}")
        shutil.copy(str(skill_tree_path), str(skill_tree_dest))


  source = core.BASE_DIRECTORY.joinpath('docs', 'images', 'under_construction', 'under_construction.jpg')
  dest   = core.BASE_DIRECTORY.joinpath('site', 'images', 'under_construction', 'under_construction.jpg')
  shutil.copy(str(source), str(dest))

def publish_character_creation(rnr_game, force_overwrite):
  docs_directory = core.BASE_DIRECTORY.joinpath('docs')
  docs_parts_directory = docs_directory.joinpath('parts')
  file_path = GENERATED_SITE_DIRECTORY.joinpath('Compendium_of_Character_Creation.md')

  md = markdown_handler.markdown_handler(f'Character Creation', force_overwrite=force_overwrite, heading_level=1, file=file_path)
  md.paragraph(f'_Version {rnr_game.get_full_version()}_')

  background_lines = []
  background_lines.append('{::options parse_block_html="true" /}  \n')
  background_lines.append('<details><summary markdown="span">View the Backgrounds</summary>  \n')
  for rnr_background in sorted(rnr_game.backgrounds, key=lambda x: x.name):
    list_of_lines = rnr_background.get_markdown(level=3).split('\n')
    list_of_lines = [line + '\n' for line in list_of_lines]
    list_of_lines += '---  \n  \n'
    background_lines += list_of_lines
  background_lines.append('</details><br/>')
  background_lines.append('{::options parse_block_html="false" /}')
  

  race_lines = []
  race_lines.append('{::options parse_block_html="true" /}  \n')
  race_lines.append('<details><summary markdown="span">View the Races</summary>  \n')
  for rnr_race in sorted(rnr_game.races, key=lambda x: (x.parent_class, x.name)):
    art_data = dict()
    escaped_name = rnr_race.name.replace(' ', '_').lower()
    art_data['attribution'] = rnr_game.generate_markdown_art_attribution(escaped_name)
    art_data['path'] = f"/{core.GLOBAL_ART_PATH.joinpath('race', f'{escaped_name}.jpg')}"

    list_of_lines = rnr_race.get_markdown(level=3, art_data=art_data, printable=True).split('\n')
    list_of_lines = [line + '\n' for line in list_of_lines]
    list_of_lines += '---  \n  \n'
    race_lines += list_of_lines
  race_lines.append('</details><br/>')
  race_lines.append('{::options parse_block_html="false" /}')

  class_lines = []
  class_lines.append('{::options parse_block_html="true" /}  \n')
  class_lines.append('<details><summary markdown="span">View the Classes</summary>  \n')
  for rnr_class in sorted(rnr_game.classes, key=lambda x: x.name):
    art_data = dict()
    escaped_name = rnr_class.name.replace(' ', '_').lower()
    art_data['attribution'] = rnr_game.generate_markdown_art_attribution(escaped_name)
    art_data['path'] = f"/{core.GLOBAL_ART_PATH.joinpath('class', f'{escaped_name}.jpg')}"
    art_data['skill_tree_path'] = f"/{core.GLOBAL_ART_PATH.joinpath('skill_trees', f'{escaped_name}.jpg')}"

    list_of_lines = rnr_class.get_markdown(level=3, art_data=art_data, printable=True).split('\n')
    list_of_lines = [line + '\n' for line in list_of_lines]
    list_of_lines += '---  \n  \n'
    class_lines += list_of_lines
  class_lines.append('</details><br/>')
  class_lines.append('{::options parse_block_html="false" /}')


  md.slurp_topmatter_file(os.path.join(docs_parts_directory, 'topmatter', 'character_creation_topmatter.md'))
  #md.slurp_markdown_file(os.path.join(docs_parts_directory, 'character_compendium_start.md'))
  md.start_heading("Backgrounds", 2)
  md.slurp_markdown_lines(background_lines)
  # #md.slurp_markdown_file(os.path.join(docs_parts_directory, 'race_part.md'))
  md.start_heading("Races", 2)
  md.slurp_markdown_lines(race_lines)
  # #md.slurp_markdown_file(os.path.join(docs_parts_directory, 'class_part.md'))
  md.start_heading("Classes", 2)
  md.slurp_markdown_lines(class_lines)

  md._write_topmatter()
  md._write_section(f'Character Creation')
  md.write_toc(max_to_include=3)
  md.write_buffer()

# def publish_ancients(force_overwrite):
#   docs_directory = os.path.join(core.BASE_DIRECTORY, 'docs')
#   docs_parts_directory = os.path.join(docs_directory, 'parts')

#   md = markdown_handler.markdown_handler(f'The Tome of the Ancients', force_overwrite=force_overwrite, heading_level=1, file=os.path.join(GENERATED_SITE_DIRECTORY, 'Tome_of_the_Ancients.md'))
#   md.paragraph(f'_Version {core.VERSION_NUMBER}_')

#   spells = io_handler.markdown_spellbooks()

#   md.slurp_topmatter_file(os.path.join(docs_parts_directory, 'topmatter', 'ancients_topmatter.md'))
#   md.slurp_markdown_file(os.path.join(docs_parts_directory, 'spells_part.md'))
#   md.slurp_markdown_lines(spells)

#   md._write_topmatter()
#   md._write_section(f'The Tome of the Ancients')
#   md.write_toc(max_to_include=2)
#   md.write_buffer()

# def publish_examples(force_overwrite):
#   docs_directory = os.path.join(core.BASE_DIRECTORY, 'docs')
#   docs_parts_directory = os.path.join(docs_directory, 'parts')

#   md = markdown_handler.markdown_handler(f'The Book of Examples', force_overwrite=force_overwrite, heading_level=1, file=os.path.join(GENERATED_SITE_DIRECTORY, 'Examples.md'))
#   md.paragraph(f'_Version {core.VERSION_NUMBER}_')


#   md.slurp_markdown_file(os.path.join(docs_parts_directory, 'explanations_part.md'))

#   md._write_section(f'The Book of Examples')
#   md.write_toc()
#   md.write_buffer()

#def publish_rulebook(rnr_game, force_overwrite):


#   docs_directory = os.path.join(core.BASE_DIRECTORY, 'docs')
#   docs_parts_directory = os.path.join(docs_directory, 'parts')

#   if not os.path.exists(docs_directory):
#     print(f"ERROR: cannot find docs directory: {docs_directory}")
#     sys.exit(1)

#   md = markdown_handler.markdown_handler(f'Rangers and Ruffians Rulebook', force_overwrite=force_overwrite, heading_level=1, file=os.path.join(GENERATED_SITE_DIRECTORY, 'Rulebook.md'))
#   md.paragraph(f'_Version {core.VERSION_NUMBER}_')

#   md.slurp_topmatter_file(os.path.join(docs_parts_directory, 'topmatter', 'rulebook_topmatter.md'))
#   md.slurp_markdown_file(os.path.join(docs_parts_directory, 'player_handbook_start.md'))
#   md.slurp_markdown_file(os.path.join(docs_parts_directory, 'stat_computation.md'))
#   md.slurp_markdown_file(os.path.join(docs_parts_directory, 'character_redirect.md'))

#   md._write_topmatter()
#   md._write_section(f'Rangers and Ruffians Rulebook')
#   md.write_toc(max_to_include=3)
#   md.write_buffer()
  
def publish_monsters(rnr_game : RangersAndRuffians, force_overwrite):
  docs_directory = core.BASE_DIRECTORY.joinpath('docs')
  file_path = GENERATED_SITE_DIRECTORY.joinpath('Book_of_Known_Beasts.md')

  md = markdown_handler.markdown_handler(f'The Book of Known Beasts', force_overwrite=force_overwrite, heading_level=1, file=file_path)
  md.paragraph(f'_Version {rnr_game.get_full_version()}_')

  monster_lines = []
  current_monster_class = None
  for rnr_monster in sorted(rnr_game.monsters, key=lambda x: (x.monster_class, x.monster_family, x.tier, x.name)):
    list_of_lines = list()
    if rnr_monster.monster_class != current_monster_class:
      current_monster_class = rnr_monster.monster_class
      list_of_lines.append(f'## {current_monster_class}  \n')
    list_of_lines += rnr_monster.get_markdown(level=3).split('\n')
    list_of_lines = [line + '\n' for line in list_of_lines]
    list_of_lines += '---  \n  \n'    
    monster_lines += list_of_lines


  md.slurp_topmatter_file(os.path.join(docs_directory, 'parts', 'topmatter', 'known_beasts_topmatter.md'))
  md.start_heading("Monsters", 2)
  md.slurp_markdown_lines(monster_lines)

  md._write_topmatter()
  md._write_section(f'Monsters')
  md.write_toc(max_to_include=3)
  md.write_buffer()

def publish_weapons(rnr_game : RangersAndRuffians, force_overwrite : bool):
  docs_directory = core.BASE_DIRECTORY.joinpath('docs')
  file_path = GENERATED_SITE_DIRECTORY.joinpath('Items.md')

  md = markdown_handler.markdown_handler(f'Items', force_overwrite=force_overwrite, heading_level=1, file=file_path)
  md.paragraph(f'_Version {rnr_game.get_full_version()}_')

  weapon_lines = []
  weapon_lines.append('{::options parse_block_html="true" /}  \n')
  weapon_lines.append(f'  \n<div class="printable-content" id="printable-weapons">  \n')
  weapon_lines.append(f'  \n<button onclick="printContent(\'printable-weapons\')">Print Weapons</button>  \n')
  for rnr_weapon in sorted(rnr_game.weapons, key=lambda x: x.name):
    weapon_lines += f'<div class="rnr-ability" id="weapon-{rnr_weapon.name.lower()}">  \n'
    list_of_lines = rnr_weapon.get_markdown(level=3).split('\n')
    list_of_lines = [line + '\n' for line in list_of_lines]
    weapon_lines += list_of_lines
    weapon_lines += '</div>  \n'
    weapon_lines += '---  \n  \n'    
  weapon_lines.append('</div>  \n')
  weapon_lines.append('{::options parse_block_html="false" /}')


  md.slurp_topmatter_file(os.path.join(docs_directory, 'parts', 'topmatter', 'skip_topmatter.md'))
  md.start_heading("Weapons", 2)
  md.slurp_markdown_lines(weapon_lines)

  md._write_topmatter()
  md._write_section(f'Items')
  md.write_toc(max_to_include=3)
  md.write_buffer()
# def publish_pantheon(force_overwrite):
#   core.load_Rangers_And_Ruffians_Data()
#   docs_directory = os.path.join(core.BASE_DIRECTORY, 'docs')

#   md = markdown_handler.markdown_handler(f'Book of Lore', force_overwrite=force_overwrite, heading_level=1, file=os.path.join(GENERATED_SITE_DIRECTORY, 'Book_of_Lore.md'))
#   md.paragraph(f'_Version {core.VERSION_NUMBER}_')

#   md.slurp_topmatter_file(os.path.join(docs_directory, 'parts', 'topmatter', 'lore_topmatter.md'))
#   pantheon = io_handler.markdown_pantheon()
#   md.slurp_markdown_file(os.path.join(docs_directory, 'parts', 'pantheon_part.md'))
#   md.slurp_markdown_lines(pantheon)

#   md._write_topmatter()
#   md._write_section(f'Book of Lore')
#   md.write_toc()
#   md.write_buffer()

# def publish_poohbah_printables(force_overwrite):
#   core.load_Rangers_And_Ruffians_Data()
#   docs_directory = os.path.join(core.BASE_DIRECTORY, 'docs')

#   md = markdown_handler.markdown_handler(f'Print Material for Poohbahs', force_overwrite=force_overwrite, heading_level=1, file=os.path.join(GENERATED_SITE_DIRECTORY, 'Poohbah_Printables.md'))
#   md.paragraph(f'_Version {core.VERSION_NUMBER}_')

#   md.slurp_topmatter_file(os.path.join(docs_directory, 'parts', 'topmatter', 'skip_topmatter.md'))
#   md.slurp_markdown_file(os.path.join(docs_directory, 'parts', 'poohbah_printables_part.md'))

#   md._write_topmatter()
#   md._write_section(f'Print Material for Poohbahs')
#   md.write_buffer()

# def publish_printabled_materials(force_overwrite):
#   core.load_Rangers_And_Ruffians_Data()
#   docs_directory = os.path.join(core.BASE_DIRECTORY, 'docs')

#   md = markdown_handler.markdown_handler(f'Printed Materials', force_overwrite=force_overwrite, heading_level=1, file=os.path.join(GENERATED_SITE_DIRECTORY, 'Printed_Materials.md'))
#   md.paragraph(f'_Version {core.VERSION_NUMBER}_')

#   md.slurp_topmatter_file(os.path.join(docs_directory, 'parts', 'topmatter', 'skip_topmatter.md'))
#   md.slurp_markdown_file(os.path.join(docs_directory, 'parts', 'printed_materials.md'))

#   md._write_topmatter()
#   md._write_section(f'Printed Materials')
#   md.write_buffer()

# def publish_changelog(force_overwrite):
#   docs_directory = os.path.join(core.BASE_DIRECTORY, 'docs')
#   parts_directory = os.path.join(docs_directory, 'parts')
#   changelog_directory = os.path.join(parts_directory, 'changelog_parts')

#   md = markdown_handler.markdown_handler(f'Changelog', force_overwrite=force_overwrite, heading_level=1, file=os.path.join(GENERATED_SITE_DIRECTORY, 'Changelog.md'))
#   md.slurp_topmatter_file(os.path.join(parts_directory, 'topmatter', 'changelog_topmatter.md'))

#   changelogs = list()
#   for file in Path(changelog_directory).glob('*.md'):
#     name = str(file).split('/')[-1].replace('.md', '')
#     major, greater, minor = name.split('_')
#     changelogs.append( ( int(major), int(greater), int(minor) ) )

#   changelogs = sorted(changelogs, reverse=True)

#   i = 0
#   for changelog in changelogs:
#     major, greater, minor = changelog
#     filename = f'{major}_{greater}_{minor}.md'
#     header_append = f'-{i}' if i > 0 else ''
#     i += 1
#     md.slurp_markdown_file(os.path.join(changelog_directory, filename))#, header_append=header_append, prepend=False)

#   md._write_topmatter()
#   md._write_section(f'Changelog')
#   md.write_toc(max_to_include=2)
#   md.write_buffer()

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

# def create_alt_all_race_class_json():
#   all_race_data = copy.deepcopy(core.GLOBAL_RACE_DATA)
#   all_class_data = copy.deepcopy(core.GLOBAL_CLASS_DATA)
#   ability_data = core.GLOBAL_ABILITY_DICT
#   items_data = copy.deepcopy(core.GLOBAL_STANDARD_ITEMS)

#   for race in all_race_data.keys():
#     for subrace in all_race_data[race]['subraces'].keys():
#       all_race_data[race]['subraces'][subrace]['abilities'] = core.filterAbilities(all_race_data[race]['subraces'][subrace]['abilities'])

#   for rnr_class in all_class_data.keys():
#     for subclass in all_class_data[rnr_class]["subclasses"].keys():
#       all_class_data[rnr_class]["subclasses"][subclass]["icons"] = core.which_icons('', rnr_class)

#       if 'base_abilities' in all_class_data[rnr_class]["subclasses"][subclass]:
#         all_class_data[rnr_class]["subclasses"][subclass]['base_abilities'] = core.filterAbilities(all_class_data[rnr_class]["subclasses"][subclass]['base_abilities'])
#       else:
#         all_class_data[rnr_class]["subclasses"][subclass]['base_abilities']   = {}
#       for level in all_class_data[rnr_class]["subclasses"][subclass]['levels']:
#         all_class_data[rnr_class]["subclasses"][subclass]['levels'][level]['abilities'] = core.filterAbilities(all_class_data[rnr_class]["subclasses"][subclass]['levels'][level]['abilities'])


#   # # Scrub the item data
#   # for weapon_type in items_data['weapons'].keys():
#   #   for weapon, weapon_info in items_data[weapon_type].items():
#   #     r = weapon_info['range']
#   #     if r == ''

#   data = {
#     'race_names' : core.get_all_subrace_names(),
#     'class_names' : core.get_all_subclass_names(),
#     'races' : all_race_data,
#     'classes' : all_class_data,
#     'items' : items_data,
#     'role_info' : {
#       'unique_roles' : [],
#       'class_roles' : {},
#       'tooltips' : {}
#     }
#   }
#   data["roles"] = dict()
#   data["roles"]["class_roles"] = dict()
#   unique_roles = set()
#   class_objs = core.load_all_class_objects()
#   for obj in class_objs:
#     data["roles"]["class_roles"][obj.name] = {
#       "roles" : obj.roles
#     }
#     unique_roles.update(set(obj.roles))

#   data["roles"]["unique_roles"] = list(unique_roles)

#   tooltips = {
#     "tank": "Too big to fall!",
#     "low-health": "Squishy, better hide!",
#     "self-sufficient": "Self-healing!",
#     "nature-based": "Hug the Trees!",
#     "undead": "No Longer 6ft. Under!",
#     "high-damage": "Vexing Poohbahs Since 2016!",
#     "mage": "Simple Magic or Otherwise!",
#     "non-magic": "Good Old Fashioned Steel!",
#     "spellbooks": "Choose New Spells!",
#     "support": "Helpful!",
#     "healer": "Every party needs one!",
#     "mobile": "Like a chicken with it's head cut off!",
#     "ranged": "Stays out of the fray!",
#     "area-control": "This is MY ground!",
#     "companion-creature": "Because everybody needs a friend!",
#     "charismatic": "Because somebody has to be!",
#     "sneaky": "A Sneaky Hider!",
#     "good-first-class": "Simple to pick up!",
#     "complex": "Easy to play, difficult to master!"
#   }

#   tooltip_present = set(tooltips.keys())
#   if len(unique_roles - tooltip_present) > 0:
#     print("ERROR! Missing tooltips for the following!")
#     for item in list(unique_roles - tooltip_present):
#       print(item)
#     sys.exit(1)

#   data["roles"]["tooltips"] = tooltips

#   with open( os.path.join(GENERATED_SITE_DIRECTORY, 'ALT.json' ), 'w' ) as outfile:
#     json.dump(data, outfile)

def setup_service_worker():
  intended_service_worker_path = os.path.join(core.BASE_DIRECTORY, 'service_worker.js')

  site_path = core.BASE_DIRECTORY.joinpath('_site')
  site_service_worker_path = site_path.joinpath('service_worker.js')

  os.chdir(core.BASE_DIRECTORY)
  os.system("bundle exec jekyll build")
  os.chdir(site_path)
  os.system("node build.js")
  shutil.copy(site_service_worker_path, intended_service_worker_path)
  os.chdir(core.CODE_DIRECTORY)


if __name__ == "__main__":
  core.printLogo()

  # with open('races.md', 'w') as outfile:
  #   for race_name, race_obj in rnr_game.races.items():
  #     outfile.write(race_obj.get_markdown(level=2))

  # with open('classes.md', 'w') as outfile:
  #   for class_name, class_obj in rnr_game.classes.items():
  #     outfile.write(class_obj.get_markdown(level=2))
  
  # with open('backgrounds.md', 'w') as outfile:
  #   for background_name, background_obj in rnr_game.backgrounds.items():
  #     outfile.write(background_obj.get_markdown(level=2))
  
  # with open('weapons.md', 'w') as outfile:
  #   for weapon_name, weapon_obj in rnr_game.weapons.items():
  #     outfile.write(weapon_obj.get_markdown(level=2))
  
  # with open('monsters.md', 'w') as outfile:
  #   for monster_name, monster_obj in rnr_game.monsters.items():
  #     outfile.write(monster_obj.get_markdown(level=2))


  # for class_name, class_obj in rnr_game.classes.items():
  #   for ability in class_obj.get_all_abilities():
  #     if ability.summoned_creature is not None:
  #       print(f"{class_name} {ability.summoned_creature}")


  if not os.path.exists(GENERATED_SITE_DIRECTORY):
    os.mkdir(GENERATED_SITE_DIRECTORY)

  parser=argparse.ArgumentParser(description="Utility to re-write new versions of the core rulebooks.")
  parser.add_argument('--ask', action='store_true')
  parser.add_argument('--skip_validation', action='store_true')
  args = parser.parse_args()
  force_overwrite = not args.ask
  skip_validation = args.skip_validation

  print(f"Force overwrite is {force_overwrite}")


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
  print(f"Loaded RnR version {rnr_game.get_full_version()}")

  copyImages(rnr_game)
  #publish_rulebook(force_overwrite)
  publish_monsters(rnr_game, force_overwrite)
  # publish_pantheon(force_overwrite)
  publish_character_creation(rnr_game, force_overwrite)
  publish_weapons(rnr_game, force_overwrite)
  # publish_ancients(force_overwrite)
  # publish_examples(force_overwrite)
  # publish_changelog(force_overwrite)
  # publish_printabled_materials(force_overwrite)
  # publish_poohbah_printables(force_overwrite)
  # create_alt_all_race_class_json()
  setup_service_worker()
  print("Done!")
