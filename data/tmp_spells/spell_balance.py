import os
import json
import yaml
import statistics
import sys

required_fields = ["cost", "target", "num_targets", "duration", "description", "range", "purpose"]#, "school"]
all_fields = required_fields + ["dice", "effect_type", "effects", "casting_time", "components", "upcast", "action_type", "effect_radius",  "hit", "school"]
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
    "STRING_LIST_MACRO",
    "DICE_MACRO",
    "MILES_MACRO"
]

valid_values = {
    "cost" : ["INTEGER_MACRO"],
    "target": ["friendly", "enemy", "entity", "self", "space", "other"],
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

required_effect_fields = ['description', 'save']
all_effect_fields = required_effect_fields + ['condition', 'repeat'] 
valid_effect_values = {
    "condition" : ["STRING_MACRO"],
    "description" : ["STRING_MACRO"],
    "save" : ["STRING_MACRO"],
    "repeat" : ["STRING_LIST_MACRO"]
}

# Log levels are WARN, DANGER, and 
LOG_LEVELS = {
  'INFO' : 0,
  'WARN' : 1,
  'DANGER': 2
}
GLOBAL_LOG_LEVEL = LOG_LEVELS['INFO']

def log(message, log_level='INFO'):
    global LOG_LEVELS, GLOBAL_LOG_LEVEL

    level = LOG_LEVELS.get(log_level, None)
    if level is None:
        print(f'ERROR: Bad log level {log_level}')
    elif level >= GLOBAL_LOG_LEVEL:
        print(message)



def is_macro(value, macro):
    if macro == 'INTEGER_MACRO':
        return isinstance(value, int)
    elif macro == "STRING_LIST_MACRO":
        if not isinstance(value, list):
            return False
        else:
            for item in value:
                if not isinstance(item, str):
                    return False
            return True
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
                    log(f'{spell_name} has {field}, but not {req}', 'DANGER')

    if 'purpose' in spell_info and spell_info['purpose'] in ['damage', 'debuff']:
        if not 'hit' in spell_info:
            error = True
            log(f'{spell_name} has purpose {spell_info["purpose"]} but does not have a "hit" value', 'DANGER')
    return error

# Cheks to see if val is a valid value for key per the valid_dict.
def check_equality(key, val, valid_dict, descriptive_name):
    if key not in valid_dict:
        log(f'ERROR: no valid values listed for {key}', 'DANGER')
        return False
    else:
        for valid_value in valid_dict[key]:
            if valid_value in MACRO_LIST:
                if is_macro(val, valid_value):
                    return True
            else:
                if val == valid_value:
                    return True
        return False

def check_spell_syntax(spell_name, spell_info):
    ''' Checks that a spell has required fields, and that all fields are typed correctly'''
    encountered_errors = False
    # Look for required fields
    for field in required_fields:
        if not field in spell_info:
            if field == 'purpose':
                log(f"{spell_name} lacks {field}", 'DANGER')
            else:
                log(f"{spell_name} is missing {field}", 'DANGER')
            encountered_errors = True

    # Check that conditional requirements are met (e.g., if you have a, you also need b)
    if check_conditional_requirements(spell_name, spell_info):
        encountered_errors =  True

    for field, val in spell_info.items():
        # Look for bad fields
        if field not in all_fields:
            log(f'{spell_name} has unexpected field {field}', 'WARN')
            encountered_errors = True
            continue

        # Check to see if there is a requirement on what the value of 'field' can be
        if field in valid_values:
            valid = check_equality(field, val, valid_values, spell_name)
            if not valid:
                log(f'{spell_name} invalid value for {field}: {val}', 'DANGER')
                encountered_errors = True

    if 'effects' in spell_info:
        if not isinstance(spell_info['effects'], list):
            log(f'{spell_name} Spell effects must be a list.', 'DANGER')
            encountered_errors = True
        else:
            for effect in spell_info['effects']:
                for field in required_effect_fields:
                    if not field in effect:
                        log(f'{spell_name}: Effect is missing {field}', 'DANGER')
                        encountered_errors = True
                for key, val in effect.items():
                    if key not in all_effect_fields:
                        log(f'{spell_name} bad effect field {key}', 'DANGER')
                        encountered_errors = True
                    else:
                        valid = check_equality(key, val, valid_effect_values, spell_name)
                        if not valid:
                            log(f'{spell_name} invalid value for {key}: {val}', 'DANGER')
                            encountered_errors = True

    if 'upcast' in spell_info:
        if 'cost' in spell_info['upcast']:
            if not is_macro(spell_info['upcast']['cost'], 'INTEGER_MACRO') and spell_info['upcast']['cost'] != 'scaling':
                log(f"{spell_name} invalid upcast cost, {spell_info['upcast']}", 'DANGER')
        else:
            log(f"{spell_name} upcast does not have a cost", 'DANGER')

        if 'effect' in spell_info['upcast']:
            if not is_macro(spell_info['upcast']['effect'], 'STRING_MACRO'):
                log(f"{spell_name} invalid upcast effect, {spell_info['upcast']['effect']}", 'DANGER')
        else:
            log(f"{spell_name} upcast does not have an effect", 'DANGER')

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
    elif spell_info['duration'] in [0,1] or spell_info['duration'] == 'concentration':
        duration_mod = 1
    else:
        duration_mod = .75

    return dmg * duration_mod



def get_expected_value(dice_str, num_targets, duration):
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
            try:
                spell_counts[tier_name] += 1
                purpose = spell_info['purpose']
                if not purpose in spells_by_type[tier_name]:
                    spells_by_type[tier_name][purpose] = 0
                spells_by_type[tier_name][purpose] += 1

                if purpose == 'damage':
                    spell_damage[tier_name].append(
                        (
                            spell_name,
                            get_expected_value(spell_info['dice'], spell_info['num_targets'], spell_info['duration']),
                            get_balance_value(tier_name, spell_info)
                        )
                    )
                elif purpose == 'healing':
                    spell_healing[tier_name].append(
                        (
                            spell_name,
                            get_expected_value(spell_info['dice'], spell_info['num_targets'], spell_info['duration']),
                            get_balance_value(tier_name, spell_info)
                        )
                    )
            except Exception:
                print(f'failed processing {spellbook_name} {tier_name} {spell_name}')
                raise

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
    log(f'{spellbook_name}', 'WARN')
    for tier_name in spells_by_type.keys():
        log(f'  {tier_name}:')
        log(f'    consists of {spell_counts[tier_name]} spells:')
        for purpose, val in spells_by_type[tier_name].items():
            log(f'      {val} {purpose} spells')
    log(f'    Damage Spell Breakdown:', 'WARN')
    for tier_name in spells_by_type.keys():
        log(f"      {tier_name}, average damage {avg_damage_per_tier[tier_name]} (expect single {expected_damage['single'][tier_name]}, multi {expected_damage['multi'][tier_name]})")
        for spell, avg_damage, balance_damage in spell_damage[tier_name]:
            log_level = 'INFO'
            warn = '' 
            if avg_damage < balance_damage - (balance_damage * .1) or avg_damage > balance_damage + (balance_damage * .1):
                warn = '(WARNING)'
                log_level = 'WARN'
            log(f'{warn}        {spell}: {avg_damage} / {balance_damage}', log_level)
    log(f'    Healing Spell Breakdown:')
    for tier_name in spells_by_type.keys():
        log(f'      {tier_name}, average healing {avg_healing_per_tier[tier_name]}')
        for spell, avg_healing, _ in spell_healing[tier_name]:
            log(f'        {spell}: {avg_healing}')


def yield_all_damage_spells(spellbooks):
    ret = get_tier_dict('dictionary')
    num = 0

    for spellbook, tiers in spellbooks.items():
        print(spellbook)
        for tier, spells in tiers.items():
            if 'aoe' not in ret[tier]:
                ret[tier]['aoe'] = dict()
            if 'single' not in ret[tier]:
                ret[tier]['single'] = dict()
            for spell, spell_info in spells.items():
                if spell_info['purpose'] != 'damage':
                    continue
                num += 1
                if spell_info['num_targets'] != 1:
                    ret[tier]['aoe'][spell] = spell_info
                else:
                    ret[tier]['single'][spell] = spell_info
    return ret, num

def analyze_global_damage(spellbooks):
    tiers, num = yield_all_damage_spells(spellbooks)
    print(f'There are {num} damage spells')
    aoe_values = get_tier_dict('list')
    single_values = get_tier_dict('list')
    aoe_stats = get_tier_dict('dictionary')
    single_stats = get_tier_dict('dictionary')

    for damage_type, stat_list in [('aoe', aoe_values), ('single', single_values)]:
        for tier, tier_breakdown in tiers.items():
            for spell, spell_info in tier_breakdown[damage_type].items():
                stat_list[tier].append(
                    (
                        spell, 
                        get_expected_value(
                            spell_info['dice'],
                            spell_info['num_targets'],
                            spell_info['duration']
                        )
                    )
                )
        

    for damage_values, stat_dict in [(aoe_values, aoe_stats), (single_values, single_stats)]:
        for tier, damage_list in damage_values.items():
            if len(damage_list) == 0:
                stat_dict[tier]['avg'] = stat_dict[tier]['stdev'] = 0
            else:
                stat_dict[tier]['avg'] = sum(n for _, n in damage_list) / len(damage_list)
                stat_dict[tier]['stdev'] = statistics.stdev(n for _, n in damage_list)

    for damage_type, stats, values in [('aoe', aoe_stats, aoe_values), ('single', single_stats, single_values)]:
        print(f'{damage_type.upper()}:')
        for tier in stats.keys():
            print(f'  {tier} avg: {stats[tier]["avg"]} stdev {stats[tier]["stdev"]}')
        print()
        for tier, tier_breakdown in tiers.items():
            for spell, spell_info in tier_breakdown[damage_type].items():
                stdev = stats[tier]['stdev']
                avg = stats[tier]['avg']
                expected_damage = get_expected_value(
                        spell_info['dice'],
                        spell_info['num_targets'],
                        spell_info['duration']
                    )
                if expected_damage > avg + stdev:
                    print(f'  WARNING!  {spell} is powerful! actual: {expected_damage} vs {avg}-{avg+stdev}')
                elif expected_damage < avg - stdev:
                    print(f'  WARNING!  {spell} is weak! actual: {expected_damage} vs {avg-stdev}-{avg}')
        print()


        for tier, damage_list in values.items():
            print(f'  Tier {tier}')
            damage_list.sort(key=lambda x:x[1])
            for spell, damage in damage_list:
                print(f'    {spell} ({damage})')
        print()








def main():
    deck_vals = {
        'Tier_0': 14,
        'Tier_1': 13,
        'Tier_2': 9,
        'Tier_3': 8,
        'Tier_4': 6,
        'Tier_5': 4
    }
    decks = {}
    with open('../spells.yml') as infile:
        rnr_spell_data = yaml.load(infile)

    encountered_errors = False
    for spellbook, spell_tiers in rnr_spell_data.items():
        decks[spellbook] = {}
        log(f'processing {spellbook}')
        for tier_name, tier_spells in spell_tiers.items():
            decks[spellbook][tier_name] = 0
            for spell_name, spell_info in tier_spells.items():
                decks[spellbook][tier_name] += 1
                encountered_errors = check_spell_syntax(spell_name, spell_info) or encountered_errors
    log('')
    for deck, deck_info in decks.items():
        log(f'Deck stats for {deck}:', 'WARN')
        for tier, tier_num in deck_info.items():
            if tier_num > deck_vals[tier]:
                log(f'    -{tier_num - deck_vals[tier]} {tier}', 'WARN')
            elif tier_num < deck_vals[tier]:
                log(f'    +{deck_vals[tier]-tier_num} {tier}', 'WARN')
            else:
                log(f'    +{deck_vals[tier]-tier_num} {tier}')
    if encountered_errors:
        sys.exit(1)
    for spellbook, spell_tiers in rnr_spell_data.items():
        spell_type_analysis(spellbook, spell_tiers)

    analyze_global_damage(rnr_spell_data)


if __name__ == '__main__':
    GLOBAL_LOG_LEVEL = LOG_LEVELS['WARN']
    main()