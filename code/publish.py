import json
import sys
import os
import rnr_utils
import markdown_handler

if __name__ == "__main__":
  rnr_utils.printLogo()
  docs_directory = os.path.join(rnr_utils.BASE_DIRECTORY, 'docs')
  docs_parts_directory = os.path.join(docs_directory, 'parts')


  if not os.path.exists(docs_directory):
    print(f"ERROR: cannot find docs directory: {docs_directory}")
    sys.exit(1)

  md = markdown_handler.markdown_handler('Rangers and Ruffians Rulebook _Version 2.1.0_', heading_level=1, file=os.path.join(docs_directory, 'Rulebook.md'))
  md.order_next('Rangers and Ruffians Rulebook _Version 2.1.0_')

  races = rnr_utils.load_all_race_objects()
  rnr_classes = rnr_utils.load_all_class_objects()


  race_lines = []
  for race in sorted(races, key=lambda x: x.name):
    race_lines += race.markdownify()

  class_lines = []
  for rnr_class in sorted(rnr_classes, key=lambda x: x.name):
    class_lines += rnr_class.markdownify()

  spells = rnr_utils.markdown_spellbooks()
  skills = rnr_utils.markdown_skills()


  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'player_handbook_start.md'))
  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'stat_computation.md'))
  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'race_part.md'))
  md.slurp_markdown_lines(race_lines)
  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'class_part.md'))
  md.slurp_markdown_lines(class_lines)
  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'skills_part.md'))
  md.slurp_markdown_lines(skills)
  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'spells_part.md'))
  md.slurp_markdown_lines(spells)

  

  md.write_toc(max_to_include=3)
  md.write_buffer()
  print("Done!")
