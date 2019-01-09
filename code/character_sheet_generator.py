import json
import sys
import os
from collections import OrderedDict
from collections import Counter
import yaml
import rnr_utils

rnr_utils.printLogo()
rnr_utils.load_Rangers_And_Ruffians_Data()

#races
catterwol = rnr_utils.load_race("Catterwol")
human = rnr_utils.load_race("Human")
halfling = rnr_utils.load_race("Halfling")
orc = rnr_utils.load_race("Orc")
elf = rnr_utils.load_race("Elf")

#classes
rogue = rnr_utils.load_class("Rogue")
knight = rnr_utils.load_class("Knight")
wizard = rnr_utils.load_class("Wizard")
sorcerer = rnr_utils.load_class("Sorcerer")
archer = rnr_utils.load_class("Archer")

emily = (rnr_utils.rnr_character("Vasha", "", "", catterwol, rogue),"vasha")
jeremy = (rnr_utils.rnr_character("Gillthunder", "", "", human, knight),"gillthunder")
nick = (rnr_utils.rnr_character("Bilgolf the Purple", "", "", halfling, wizard),"bilgolf_wizard")
nick2 = (rnr_utils.rnr_character("Bilgolf the Purple", "", "", halfling, sorcerer),"bilgolf_sorcerer")
seantelle = (rnr_utils.rnr_character("Harley", "", "", elf, wizard),"harley_wizard")
seantelle2 = (rnr_utils.rnr_character("Harley", "", "", elf, sorcerer),"harley_sorcerer")
zack = (rnr_utils.rnr_character("Orcenshield", "", "", orc, archer),"orcenshield")

hetzer_company = (emily, jeremy, nick, nick2, seantelle, seantelle2, zack)

dirname = "hetzer_company"
if not os.path.exists(dirname):
  os.makedirs(dirname)

for player in hetzer_company:
  with open(os.path.join(dirname, "{0}.md".format(player[1])), 'w') as outfile:
    outfile.write(player[0].markdownify())


#rnr_character