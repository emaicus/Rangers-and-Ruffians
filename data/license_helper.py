import yaml
import os
import sys

if __name__ == '__main__':
  with open('art.yml') as infile:
    data = yaml.load(infile)
  
  new_data = dict()
  known_information = dict()

  for piece, info in data.items():
    url = info.get('license_url', None)
    acronym = info.get('license_acronym', None)
    license = info.get('license', None)

    if url is not None:
      if url not in known_information:
        known_information[url] = {
          'license' : None,
          'acronym' : None
        }
      

      if known_information[url]['license'] is None and license is not None:
        known_information[url]['license'] = license
      if known_information[url]['acronym'] is None and acronym is not None:
        known_information[url]['acronym'] = acronym

  for piece, info in data.items():
    url = info.get('license_url', None)
    acronym = info.get('license_acronym', None)
    license = info.get('license', None)

    name_split = piece.split('_')
    if len(name_split) == 2:
      if name_split[0].lower() in ['male', 'female']:
        piece = f'{name_split[1]}_{name_split[0]}'

    new_data[piece] = info

    if url is None:
      url = input(f'{piece} is missing a url for its license. We need that to populate its license info. What is the url? ').strip()
      info['license_url'] = url

    if url not in known_information:
      known_information[url] = {
        'license' : None,
        'acronym' : None
      }

    if known_information[url]['license'] is None:
      known_information[url]['license'] = input(f'What is the license name for {url}? ').strip()
    if known_information[url]['acronym'] is None:
      known_information[url]['acronym'] = input(f'What is the acronym for {url}? ').strip()

    new_data[piece]['license_acronym'] = known_information[url]['acronym']
    new_data[piece]['license'] = known_information[url]['license']

  with open('better_art.yml', 'w') as outfile:
    yaml.dump(new_data, outfile, default_flow_style=False)