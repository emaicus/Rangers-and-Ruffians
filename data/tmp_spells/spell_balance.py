import os
import json
import yaml
import statistics

required_fields = ["cost", "target", "num_targets", "duration", "description", "range", "purpose", "school"]
all_fields = required_fields + ["dice", "effect_type", "effects", "casting_time", "components", "upcast", "action_type", "effect_radius", "charisma_cost", "hit"]
conditional_requirements = {
    "dice" : ["effect_type"],
    "effect_type" : ["dice"]
}

expected_damage = {
    'single' : {
        'Tier_0' : 7,
        'Tier_1' : 14,
        'Tier_2' : 27,
        'Tier_3' : 36,
        'Tier_4' : 50,
        'Tier_5' : 70
    },
    'multi' : {
        'Tier_0' : 4.5,
        'Tier_1' : 10,
        'Tier_2' : 20,
        'Tier_3' : 30,
        'Tier_4' : 38,
        'Tier_5' : 58
    }
}

MACRO_LIST = [
    "INTEGER_MACRO",
    "HOURS_MACRO",
    "DAYS_MACRO",
    "WEEKS_MACRO",
    "STRING_MACRO",
    "DICE_MACRO",
    "MILES_MACRO"
]

valid_values = {
    "cost" : ["INTEGER_MACRO"],
    "target": ["friendly", "enemy", "everyone", "self", "space", "other"],
    "num_targets": [1, "many"],
    "duration": ["INTEGER_MACRO", "save", "battle", "HOURS_MACRO", "DAYS_MACRO", "WEEKS_MACRO", "concentration", "infinite"],
    "description": ["STRING_MACRO"],
    "range": ["self", "hand", "close", "near", "mid", "archer", "far", "infinite", "MILES_MACRO"],
    "purpose": ["damage", "healing", "buff", "debuff", "summon", "utility"],
    "dice": ["DICE_MACRO"],
    "effect_type": ['blunt', 'slashing', 'piercing', 'healing', 'elemental', 'poison', 'force', 'psychic', 'ice', 'fire', 'dark', 'radiant', 'necrotic'],
    "casting_time": ["INTEGER_MACRO", "HOURS_MACRO"],
    "action_type": ["Action", "Offhand Action", "Reaction", "Free Action"],
    "effect_radius": ["INTEGER_MACRO", "MILES_MACRO"],
    "charisma_cost": ["INTEGER_MACRO"],
    "hit" : ["always", "roll", "other"]
}

def is_macro(value, macro):
    if macro == 'INTEGER_MACRO':
        return isinstance(value, int)
    elif not isinstance(value, str):
        return False
    elif macro == 'HOURS_MACRO':
        return 'hour' in value
    elif macro == 'DAYS_MACRO':
        return 'day' in value
    elif macro == 'WEEKS_MACRO':
        return 'week' in value
    elif macro == 'MILES_MACRO':
        return 'mile' in value
    elif macro == "STRING_MACRO":
        return isinstance(value, str)
    elif macro == "DICE_MACRO":
        try:
            parts = value.split('d')
            int(parts[0])
            return len(parts) == 2 and int(parts[1]) in [2,4,6,8,10,12,20]
        except Exception:
            return False

def check_conditional_requirements(spell_name, spell_info):
    error = False
    for field, val in spell_info.items():
        if field in conditional_requirements:
            for req in conditional_requirements[field]:
                if not req in spell_info:
                    error = True
                    print(f'{spell_name} has {field}, but not {req}')

    if 'purpose' in spell_info and spell_info['purpose'] in ['damage', 'debuff']:
        if not 'hit' in spell_info:
            error = True
            print(f'{spell_name} has purpose {spell_info["purpose"]} but does not have a "hit" value')
    return error

def check_spell_syntax(spell_name, spell_info):
    ''' Checks that a spell has required fields, and that all fields are typed correctly'''
    encountered_errors = False
    # Look for required fields
    for field in required_fields:
        if not field in spell_info:
            print(f"{spell_name} is missing {field}")
            encountered_errors = True

    # Check that conditional requirements are met (e.g., if you have a, you also need b)
    if check_conditional_requirements(spell_name, spell_info):
        encountered_errors =  True

    for field, val in spell_info.items():
        # Look for bad fields
        if field not in all_fields:
            print(f'{spell_name} has unexpected field {field}')
            encountered_errors = True
            continue

        # Check to see if there is a requirement on what the value of 'field' can be
        if field in valid_values:
            valid = False
            for valid_value in valid_values[field]:
                if valid_value in MACRO_LIST:
                    valid = is_macro(val, valid_value)
                    if valid:
                        break
                else:
                    if val == valid_value:
                        valid = True
                        break
            if not valid:
                print(f'{spell_name} invalid value for {field}: {val}')
                encountered_errors = True
    return encountered_errors

def get_balance_value(tier_name, spell_info):
    multi = spell_info['num_targets'] == 'many'

    # Multi-target spells do 75% single target damage
    if multi:
        dmg = expected_damage['multi'][tier_name]
    else:
        dmg = expected_damage['single'][tier_name]

    # Concentration spells do 85% damage, >1 duration does 75% damage,
    # single turn does 100% duration
    if spell_info['duration'] == 'concentration' and spell_info['cost'] > 0:
        duration_mod = .85
    elif spell_info['duration'] == 1 or spell_info['duration'] == 'concentration':
        duration_mod = 1
    else:
        duration_mod = .75

    return dmg * duration_mod



def get_expected_value(dice_str, num_targets, duration, cost):
    avg_roll = _get_avg_roll_from_dice_string(dice_str)
    # Now compenstated for in balance value
    num_targets = 1 #2 if num_targets == 'many' else 1
    duration = 1

    # now compensated for in balance value
    # if duration == 'concentration':
    #     duration = 1 if cost == 0 else 1.5
    # elif isinstance(duration, str):
    #     duration = 2
    # else:
    #     duration = duration

    return avg_roll * duration * num_targets


def _get_avg_roll_from_dice_string(dice_str):
    parts = dice_str.split('d')
    num = int(parts[0])
    dice = int(parts[1])
    return num * ((dice // 2) + .5)

def get_tier_dict(default_val):
    ret = {}
    for value in range(0,6):
        if default_val == 'dictionary':
          ret[f'Tier_{value}'] = {}
        elif default_val == 'list':
          ret[f'Tier_{value}'] = []
        else:
          ret[f'Tier_{value}'] = default_val
    return ret

def spell_type_analysis(spellbook_name, spell_tiers):
    spells_by_type = get_tier_dict('dictionary')
    spell_damage = get_tier_dict('list')
    spell_healing = get_tier_dict('list')
    spell_counts = get_tier_dict(0)

    for tier_name, tier_spells in spell_tiers.items():
        for spell_name, spell_info in tier_spells.items():
            spell_counts[tier_name] += 1
            purpose = spell_info['purpose']
            if not purpose in spells_by_type[tier_name]:
                spells_by_type[tier_name][purpose] = 0
            spells_by_type[tier_name][purpose] += 1

            if purpose == 'damage':
                spell_damage[tier_name].append(
                    (
                        spell_name,
                        get_expected_value(spell_info['dice'], spell_info['num_targets'], spell_info['duration'], spell_info['cost']),
                        get_balance_value(tier_name, spell_info)
                    )
                )
            elif purpose == 'healing':
                spell_healing[tier_name].append(
                    (
                        spell_name,
                        get_expected_value(spell_info['dice'], spell_info['num_targets'], spell_info['duration'], spell_info['cost']),
                        get_balance_value(tier_name, spell_info)
                    )
                )

    # Get the averages
    avg_damage_per_tier = get_tier_dict(0)
    avg_healing_per_tier = get_tier_dict(0)
    for tier_name in spells_by_type.keys():
        for spell, avg_damage, _ in spell_damage[tier_name]:
            avg_damage_per_tier[tier_name] += avg_damage
        avg_damage_per_tier[tier_name] = avg_damage_per_tier[tier_name] / len(spell_damage[tier_name]) if len(spell_damage[tier_name]) > 0 else 0
        for spell, avg_healing, _ in spell_healing[tier_name]:
            avg_healing_per_tier[tier_name] += avg_healing
        avg_healing_per_tier[tier_name] = avg_healing_per_tier[tier_name] / len(spell_healing[tier_name]) if len(spell_healing[tier_name]) > 0 else 0



    # Print the statistics
    print(f'{spellbook_name}')
    for tier_name in spells_by_type.keys():
        print(f'  {tier_name}:')
        print(f'    consists of {spell_counts[tier_name]} spells:')
        for purpose, val in spells_by_type[tier_name].items():
            print(f'      {val} {purpose} spells')
    print(f'    Damage Spell Breakdown:')
    for tier_name in spells_by_type.keys():
        print(f"      {tier_name}, average damage {avg_damage_per_tier[tier_name]} (single {expected_damage['single'][tier_name]}, multi {expected_damage['multi'][tier_name]})")
        for spell, avg_damage, balance_damage in spell_damage[tier_name]:
          print(f'        {spell}: {avg_damage} / {balance_damage}')
    print(f'    Healing Spell Breakdown:')
    for tier_name in spells_by_type.keys():
        print(f'      {tier_name}, average healing {avg_healing_per_tier[tier_name]}')
        for spell, avg_healing, _ in spell_healing[tier_name]:
          print(f'        {spell}: {avg_healing}')


def main():
    with open('formatted_spells.yml') as infile:
        rnr_spell_data = yaml.load(infile)

    encountered_errors = False
    for spellbook, spell_tiers in rnr_spell_data.items():
        print(f'processing {spellbook}')
        for tier_name, tier_spells in spell_tiers.items():
            for spell_name, spell_info in tier_spells.items():
                encountered_errors = check_spell_syntax(spell_name, spell_info) and encountered_errors
    # print(json.dumps(rnr_spell_data, indent=4))

    if encountered_errors:
        sys.exit(1)
    for spellbook, spell_tiers in rnr_spell_data.items():
        spell_type_analysis(spellbook, spell_tiers)


if __name__ == '__main__':
    main()