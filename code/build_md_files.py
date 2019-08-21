import json
import sys
import os
import rnr_utils

if __name__ == "__main__":
  rnr_utils.printLogo()


#   <style>
#   .phb#p1{ text-align:center; }
#   .phb#p1:after{ display:none; }
# </style>

# <div style='margin-top:450px;'></div>

# # The Legion Ingredient

# <div style='margin-top:25px'></div>
# <div class='wide'>
# ##### In a wicked universe, five seers fight lawlessness.
# </div>

# \page

  races = rnr_utils.load_all_race_objects()
  rnr_classes = rnr_utils.load_all_class_objects()

  with open('../rulebook.md', 'w') as outfile:
    for race in sorted(races, key=lambda x: x.name):
      outfile.write(race.markdownify())
    for rnr_class in sorted(rnr_classes, key=lambda x: x.name):
      outfile.write(rnr_class.markdownify())
    outfile.write(rnr_utils.markdown_spellbooks())
  print()
  print("Done!")
