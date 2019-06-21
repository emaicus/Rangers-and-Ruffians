import yaml
import os
import inquirer
import json
import copy

def ask(question, options):
  q = inquirer.List('answer',
                  message=question,
                  choices=options,
              )
  return inquirer.prompt([q,])['answer']

def printDetails(details):
  for key, val in details.items():
    print("{0}: {1}".format(key, val))
  print()

if __name__ == '__main__':
  with open('classes_2.yml', 'r') as infile:
    data = yaml.load(infile)

  for rnr_class_type, rnr_classes in data.items():
    for rnr_class, rnr_class_info in rnr_classes.items():
      print("We're working on {0}".format(rnr_class))
      details = copy.deepcopy(rnr_class_info['base_stats'])
      printDetails(details)
      for i in range(1,11):
        print("Level {0}".format(i))
        printDetails(details)
        recommended_stats = {}
        answer = ask("Which Stat should be increased?", list(details.keys()))
        recommended_stats[answer] = 1
        details[answer] += 1
        printDetails(details)
        answer = ask("Which Stat should be increased?", list(details.keys()))
        if not answer in recommended_stats:
          recommended_stats[answer] = 1
        else:
          recommended_stats[answer] += 1
        details[answer]+=1
        rnr_class_info['levels']['level_{0}'.format(i)]['stats'] = recommended_stats
      print("saving...")
      with open('classes_2.yml', 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
      print("saved!")