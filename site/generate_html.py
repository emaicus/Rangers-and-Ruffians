import json
import sys
import os
import yattag
from yattag import Doc

def filterAbilities(abilities, ability_dict):
  filtered_abilities = dict()
  for ability in abilities:
    ability_type = ability_dict[ability]["type"]
    if not ability_type in filtered_abilities:
      filtered_abilities[ability_type] = list()
    filtered_abilities[ability_type].append(ability)
  return filtered_abilities

def loadData():
  ability_path = "../json_files/abilities.json"
  class_path = "../json_files/classes.json"
  race_path = "../json_files/races.json"
  
  with open(ability_path) as data_file:
    ability_dict = json.load(data_file)

  with open(class_path) as data_file:
    class_data = json.load(data_file)

  with open(race_path) as data_file:
    race_data = json.load(data_file)
  
  return ability_dict, class_data, race_data

def mapAbilityType(ability):
  if ability == 'combat':
    return "Combat Abilities"
  elif ability == 'advantage':
    return "Advantages/Disadvantages"
  elif ability == 'starting_item':
    return "Starting Items"
  elif ability == 'choice':
    return "Starting Choices"
  elif ability == 'general':
    return "General Abilities"
  else:
    return ability

#returns an html document using yattag
def standardHtmlOut(data, ability_dict, image_path):
  doc, tag, text, line= Doc().ttl()

  doc.asis('<!DOCTYPE html>')
  with tag('html'):
    with tag('body'):
      for name, details in data.items():
        lowername = name.lower()
        #relative path for now
        lowername = lowername.replace(' ', '_')
        path_to_image = "{0}/{1}.jpg".format(image_path, lowername)
        description = details["description"]
        if 'standings' in details:
          standings = details["standings"]
        else:
          standings = name + "s come in so many shapes, sizes, and belief sets that there is no set standing for them."
        abilities = details["abilities"]
        stats = details["stats"]
        with tag('div', id=name):
          with tag('h1', id='name_header'):
            text(name)
          #adds an image (klass is the yattag 'class' variable)
          doc.stag('img', src=path_to_image, klass="photo", height=700)
          # outfile.write('![{0}]({1}?raw=true "{2}") \n\n'.format(name, path_to_image, name))
          doc.stag('br')
          text(description)

          #Standings section
          text("Standings: {0}".format(standings))
          with tag('h1', id='Standings'):
            text("Abilities")
          
          abilities = filterAbilities(abilities, ability_dict)
          for key in ('combat', 'advantage', 'starting_item', 'choice','general'):
            if not key in abilities:
              continue
            with tag('h2'):
              text(mapAbilityType(key))
            with tag('ul', id=mapAbilityType(key)):
              for ability in abilities[key]:
                ability_description = ability_dict[ability]["description"]
                line('li', "{0}: {1}".format(ability, ability_description))
          with tag('h1'):
            text("Stats:")
          with tag('ul', id='stats'):
            for stat in stats:
              line('li', '{0}: {1}'.format(stat, stats[stat]))
  print(doc.getvalue)
  return doc.getvalue()