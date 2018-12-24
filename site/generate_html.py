import json
import sys
import os
import yattag
from yattag import Doc

#returns an html document using yattag
def cardsHtmlOut(data, ability_dict, image_path, next_page='', forwarding_param='',prev_value=''):
  doc, tag, text, line= Doc().ttl()
  doc.asis('<!DOCTYPE html>')
  with tag('html'):
    with tag('head'):
      doc.asis('<meta charset="utf-8">')
      doc.asis('<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">')
      doc.asis('<link rel="stylesheet" href="/static/css/bootstrap.min.css">')
      doc.asis('<link rel="stylesheet" href="/static/css/materialize.min.css">')
      doc.asis('<link rel="stylesheet" href="/static/css/rangers.css">')
    with tag('body'):
      with tag('div', klass='container'):
        with tag('div', klass='row'):
          with tag('div', klass='col s12'):
            with tag('h2', klass='text-center'):
              text('Rangers and Ruffians')
            with tag('h4', klass='text-center grey-text lighten-3'):
              text("Evan Maicus")
            if not prev_value == '':
              with tag('h4', klass='text-center'):
                text("You chose: ", prev_value)
        with tag('div', klass='row'):
          for name, details in data.items():
            with tag('div', klass='col s12'):
              with tag('div', klass='card'):
                #Grab the data that we will write on the page.
                lowername = name.lower()
                lowername = lowername.replace(' ', '_')
                path_to_image = "{0}/{1}.jpg".format(image_path, lowername)
                description = details["description"]
                if 'standings' in details:
                  standings = details["standings"]
                else:
                  standings = name + "s come in so many shapes, sizes, and belief sets that there is no set standing for them."
                abilities = details["abilities"]
                stats = details["stats"]
                
                #Begin writing the card html.
                with tag('div', klass='card-image waves-effect waves-block waves-light'):
                  doc.stag('img', klass="activator", src=path_to_image)

                with tag('div', klass="card-content browser-default-uls"):
                  with tag('span', klass="card-title activator grey-text text-darken-4"):
                    text(name)
                  with tag('a', href="/{0}?{1}&{2}={3}".format(next_page, prev_value,forwarding_param,lowername)):
                    text('Play as a {0}'.format(name))
                with tag('div', klass='card-reveal grey lighten-5'):
                  with tag('span', klass="card-title grey-text text-darken-4"):
                    text(name)
                  with tag('div', klass='card-tabs'):
                    with tag('div', klass='row'):
                      with tag('div', klass='col s12'):
                        with tag('ul', klass='tabs'): #tabs-fixed-width
                          with tag('li', klass='tab'):
                            with tag('a', href='#{0}_overview'.format(lowername)):
                              text('Overview')
                          with tag('li', klass='tab'):
                            with tag('a', href='#{0}_standings'.format(lowername)):
                              text('Standings.')
                          with tag('li', klass='tab'):
                            with tag('a', href='#{0}_abilities'.format(lowername)):
                              text('Abilities.')
                          with tag('li', klass='tab'):
                            with tag('a', href='#{0}_stats'.format(lowername)):
                              text('Stats.')
                    with tag('div', id='{0}_overview'.format(lowername), klass='col s12'):
                      with tag('p'):
                        text(description)
                    with tag('div', id='{0}_standings'.format(lowername), klass='col s12'):
                      with tag('p'):
                        text(standings)  
                    with tag('div', id='{0}_abilities'.format(lowername), klass='col s12'):
                      with tag('p'):
                        abilities = filterAbilities(abilities, ability_dict)
                        for key in ('combat', 'advantage', 'starting_item', 'choice','general'):
                          if not key in abilities:
                            continue
                          text(mapAbilityType(key))
                          with tag('ol', id=mapAbilityType(key)):
                            for ability in abilities[key]:
                              ability_description = ability_dict[ability]["description"]
                              line('li', "{0}: {1}".format(ability, ability_description))
                    with tag('div', id='{0}_stats'.format(lowername), klass='col s12'):
                      with tag('p'):
                        with tag('ol', id='stats'):
                          for stat in stats:
                            line('li', '{0}: {1}'.format(stat, stats[stat]))
      #Add the footer
      doc.asis('<script src="/static/js/jquery-3.3.1.js"></script>')
      doc.asis('<script src="/static/js/bootstrap.min.js"></script>')
      # doc.asis('<script src="/static/js/jquery.backstretch.min.js"></script>')
      doc.asis('<script src="/static/js/materialize.min.js"></script>')
      doc.asis('<script src="/static/js/rangers.js"></script>')

  return doc.getvalue()


#returns an html document using yattag
def standardHtmlOut(data, ability_dict, image_path):
  doc, tag, text, line= Doc().ttl()
  doc.asis('<!DOCTYPE html>')
  with tag('html'):
    with tag('head'):
      doc.asis('<meta charset="utf-8">')
      doc.asis('<link rel="stylesheet" href="/static/css/bootstrap.min.css">')
      doc.asis('<link rel="stylesheet" href="/static/css/rangers.css">')
    with tag('body'):
      with tag('div', klass='container-narrow'):
        with tag('div', klass='px-3'):
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
              doc.stag('img', src=path_to_image, klass="rounded mx-auto d-block", height=700)
              # outfile.write('![{0}]({1}?raw=true "{2}") \n\n'.format(name, path_to_image, name))
              doc.stag('br')
              text(description)
              doc.stag('br')
              doc.stag('br')
              #Standings section
              text("Standings: {0}".format(standings))
              doc.stag('br')
              with tag('h4', id='Abilities'):
                text("Abilities")
              
              abilities = filterAbilities(abilities, ability_dict)
              for key in ('combat', 'advantage', 'starting_item', 'choice','general'):
                if not key in abilities:
                  continue
                with tag('h5'):
                  text(mapAbilityType(key))
                with tag('ul', id=mapAbilityType(key)):
                  for ability in abilities[key]:
                    ability_description = ability_dict[ability]["description"]
                    line('li', "{0}: {1}".format(ability, ability_description))
              with tag('h4'):
                text("Stats:")
              with tag('ul', id='stats'):
                for stat in stats:
                  line('li', '{0}: {1}'.format(stat, stats[stat]))
            doc.stag('hr')
      #Add the footer
      doc.asis('<script src="/static/js/jquery-3.3.1.js"></script>')
      doc.asis('<script src="/static/js/bootstrap.min.js"></script>')
      doc.asis('<script src="/static/js/jquery.backstretch.min.js"></script>')
      doc.asis('<script src="/static/js/rangers.js"></script>')

  print(doc.getvalue)
  return doc.getvalue()


def mergeAbilities(dictionary, abilities):
  merged_abilities = dictionary['abilities']
  for i in range(len(dictionary["abilities"])):
    ability = dictionary["abilities"][i]
    merged_abilities[i] += ": {0}".format(abilities[ability]["description"])
  dictionary['abilities'] = merged_abilities
  return dictionary

def mergeRaceAndClass(race, rangers_class,ability_dict):
  race = mergeAbilities(race,ability_dict)
  rangers_class = mergeAbilities(rangers_class, ability_dict)
  
  character = dict()
  character['stats'] = dict()
  for stat, value in race["stats"].items():
    character['stats'][stat] = value + rangers_class["stats"][stat]
  character_abilities = race["abilities"] + rangers_class["abilities"]

  character['abilities'] = character_abilities
  return character

def construct_name(name):
  name = name.replace('_', ' ')
  name = name.title()
  return name
  
def comboHtml(race_data, class_data, ability_dict, image_path, race_name, rangers_class_name):
  race_name = construct_name(race_name)
  rangers_class_name = construct_name(rangers_class_name)
  race = race_data[race_name]
  rangers_class = class_data[rangers_class_name]
  character = mergeRaceAndClass(race, rangers_class,ability_dict)
  
  abilities = character["abilities"]
  abilities = filterAbilities(abilities, ability_dict)

  doc, tag, text, line= Doc().ttl()
  doc.asis('<!DOCTYPE html>')
  with tag('html'):
    with tag('head'):
      doc.asis('<meta charset="utf-8">')
      doc.asis('<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">')
      doc.asis('<link rel="stylesheet" href="/static/css/bootstrap.min.css">')
      doc.asis('<link rel="stylesheet" href="/static/css/materialize.min.css">')
      doc.asis('<link rel="stylesheet" href="/static/css/character_sheet.css">')
    with tag('body'):
      with tag('div', klass='container-narrow'):
        with tag('div', klass='character_name'):
          text("{0}, the {1} {2}".format('Archibold', race_name, rangers_class_name))
        for key in ('combat', 'advantage', 'starting_item', 'choice','general'):
          if not key in abilities:
            continue
          with tag('h5'):
            text(mapAbilityType(key))
          with tag('ul', id=mapAbilityType(key)):
            for ability in abilities[key]:
              ability_description = ability_dict[ability]["description"]
              line('li', "{0}: {1}".format(ability, ability_description))
        with tag('h4'):
          text("Stats:")
        with tag('ul', id='stats'):
          for stat in character['stats']:
            line('li', '{0}: {1}'.format(stat, character['stats'][stat]))
      doc.stag('hr')
      #Add the footer
      doc.asis('<script src="/static/js/jquery-3.3.1.js"></script>')
      doc.asis('<script src="/static/js/bootstrap.min.js"></script>')
      # doc.asis('<script src="/static/js/jquery.backstretch.min.js"></script>')
      doc.asis('<script src="/static/js/materialize.min.js"></script>')
  return doc.getvalue()

if __name__ == '__main__':
  race = 'goblin'
  rangers_class = 'hedge_knight'
  ability_dict, class_data, race_data = loadData()
  image_path = "/static/images/classes"
  template = comboHtml(race_data, class_data, ability_dict, image_path, race, rangers_class)
  print(template)
