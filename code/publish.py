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
  md.slurp_markdown_file(os.path.join(docs_parts_directory, 'player_handbook_start.md'))


  races = rnr_utils.load_all_race_objects()
  rnr_classes = rnr_utils.load_all_class_objects()


  race_str = "## Races  \n"
  for race in sorted(races, key=lambda x: x.name):
    race_str += race.markdownify()

  class_str = '## Classes  \n'
  for rnr_class in sorted(rnr_classes, key=lambda x: x.name):
    class_str += rnr_class.markdownify()

  md.slurp_markdown_lines(race_str.split('\n'))
  md.slurp_markdown_lines(class_str.split('\n'))
  


  #outfile.write(rnr_utils.markdown_spellbooks())
  #print()


  md.write_toc()
  md.write_buffer()
  print("Done!")
