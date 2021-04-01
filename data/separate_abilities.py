import yaml
import os

abilities_file = 'abilities.yml'
out_abilities_file = os.path.join('separated', 'abilities.yml')
out_rules_file = os.path.join('separated', 'rules.yml')
out_adv_disadv = os.path.join('separated', 'adv_disadv.yml')

if __name__ == '__main__':
    with open(abilities_file) as data_file:
        all_abilities = yaml.load(data_file)

    rules = dict()
    abilities = dict()
    adv_disadv = dict()
    other = dict()

    for ability, info in all_abilities.items():
        if info['type'] in ['combat', 'general']:
            abilities[ability] = info
        elif info['type'] == 'rule':
            rules[ability] = info
        elif info['type'] in ['advantage', 'disadvantage']:
            adv_disadv[ability] = info
        else:
            other[ability] = info

    for file, dictionary in [
        (out_abilities_file, abilities),
        (out_rules_file, rules),
        (out_adv_disadv, adv_disadv)
    ]:
        with open(file, 'w') as outfile:
            yaml.dump(dictionary, outfile, default_flow_style=False)
