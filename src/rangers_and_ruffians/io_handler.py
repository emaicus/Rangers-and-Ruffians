import string
import os
from rangers_and_ruffians import core

def get_class_markdown(rnr_class_obj, male=False, sub_heading=False):
    gender = "male" if male else "female"

    absolute_art_folder = os.path.join(core.GLOBAL_ART_PATH, 'class')
    relative_art_folder = os.path.join('..', '..', 'images', 'class')
    image_path, image_attribution = core.get_gendered_art(
        relative_art_folder,
        absolute_art_folder,
        rnr_class_obj.subclass.replace(' ','_').lower(),
        male
    )

    ret = []
    description = rnr_class_obj.description
    # # The 100 should future proof us.
    # abilities = rnr_class_obj.get_abilities_to_level(100)
    # abilities = core.filterAbilities(rnr_class_obj.abilities)

    indent = '####' if sub_heading else '###'
    ret.append(f"{indent} {rnr_class_obj.subclass_name} \n")

    if image_path is not None and image_attribution is not None:
        ret.append(f"<img src='{image_path}' class=\"raceClassImage\" />\n\n")
        ret.append(image_attribution)

    if rnr_class_obj.handbook is not None:
        for section in rnr_class_obj.handbook["sections"]:
            ret.append(f'__{section["title"]}__  \n')
            for subsection in section["subsections"]:
                if 'title' in subsection and subsection["title"] != '':
                    ret.append(f'__{subsection["title"]}__  \n')
                ret.append(subsection["text"])
                ret.append('\n\n')


    ret.append(f"\n")
    ret.append(f"{description}\n")
    ret.append(f"\n")

    ret.append(f"\n")
    ret.append(f"The following starting stats are recommended for a {rnr_class_obj.subclass_name}")
    ret.append(f"\n  ")
    ret.append(f"|STR|INT|PER|DEX|INF|CHA|  \n")
    ret.append(f"|:---:|:---:|:---:|:---:|:---:|:---:|  \n")
    ret.append(f"|{rnr_class_obj.get_stat('strength')}|{rnr_class_obj.get_stat('intelligence')}|{rnr_class_obj.get_stat('perception')}|{rnr_class_obj.get_stat('dexterity')}|{rnr_class_obj.get_stat('inner_fire')}|{rnr_class_obj.get_stat('charisma')}|  \n")
    ret.append(f"\n")

    ret.append("  \n__Expertise:__  \n")
    ret.append(f"{rnr_class_obj.subclass_name}s have expertise in three of the following checks:  \n")
    for expertise_stat in rnr_class_obj.expertise_choices:
        for expertise in core.get_expertises_for_stat(expertise_stat):
            ret.append(f"  * {expertise} _({core.abbreviate_stat(expertise_stat, capitalize_first=True)})_  \n")



    # if len(abilities) > 0:
    #   ret.append(f"__{string.capwords(rnr_class_obj.class_name)} Abilities:__ \n")
    #   for key in ('rule', 'spellbook', 'choice','general', 'starting_item', 'advantage', 'disadvantage', 'combat'):
    #     if not key in abilities:
    #       continue
    #     ret.append(f"* __{mapAbilityType(key)}:__   \n")
    #     for ability, info in abilities[key].items():
    #       if 'cost' in info and info['cost'] not in [None, 0]:
    #         ret.append(f"  * __{ability}:__ _(Cost {info['cost']})_ {info['verbose']}  \n")
    #       else:
    #         ret.append(f"  * __{ability}:__ {info['verbose']}  \n")

    ret.append('  \n')

    ret.append(f'\n<a class="btn btn-primary" href="/site/pages/level_up_sheet.html?class={rnr_class_obj.class_name}" role="button">Level Up Sheet</a>\n')
    ret.append(f"  \n___\n")
    return ret

def get_level_up_sheet_markdown(rnr_class_obj):
    ret = []
    all_data = core.get_subclass_data_with_name(rnr_class_obj.subclass)
    level_data = all_data['levels']
    for i in range(0,100):
        level = f'level_{i}'
        if not level in level_data:
            continue
        ret.append( f"__{string.capwords(level.replace('_',' '))} {string.capwords(rnr_class_obj.subclass_name.replace('_', ' '))}__\n\n")

        if 'abilities' in level_data[level]:
            level_abilities = core.filterAbilities(level_data[level]['abilities'])
            for key in ('general', 'combat'):
                if not key in level_abilities:
                    continue
                ret.append(f"* __{mapAbilityType(key)}:__   \n")
                for ability, info in level_abilities[key].items():
                    if 'cost' in info and info['cost'] not in [None, 0]:
                        ret.append( f"  * __{ability}:__ _(Cost {info['cost']})_ {info['verbose']}  \n")
                    else:
                        ret.append( f"  * __{ability}:__ {info['verbose']}  \n")
                ret.append('\n\n')

    return ret

def get_rnr_race_markdown(rnr_race_obj, male=False, sub_heading=False):

    absolute_art_folder = os.path.join(core.GLOBAL_ART_PATH, 'race')
    relative_art_folder = os.path.join('..', '..', 'images', 'race')

    image_path, image_attribution = core.get_gendered_art(relative_art_folder, absolute_art_folder, rnr_race_obj.subrace_name.replace(' ','_').lower(), male)

    gender = "male" if male else "female"

    ret = []
    description = rnr_race_obj.description
    abilities = rnr_race_obj.abilities
    indent = '####' if sub_heading else '###'
    ret.append(f"{indent} {rnr_race_obj.subrace_name} \n")

    if image_path is not None and image_attribution is not None:
        ret.append(f"<img src='{image_path}' class=\"raceClassImage\" />\n\n")
        ret.append(image_attribution)

    if rnr_race_obj.quote:
        ret.append(f'>{rnr_race_obj.quote}\n>\n>—{rnr_race_obj.quote_author}\n\n')
    if not rnr_race_obj.handbook is None:
        for section in rnr_race_obj.handbook["sections"]:
            ret.append(f'__{section["title"]}__  \n')
            for subsection in section["subsections"]:
                if 'title' in subsection and subsection["title"] != '':
                    ret.append(f'__{subsection["title"]}__  \n')
                ret.append(subsection["text"])
                ret.append('\n\n')


    ret.append(f"\n")
    ret.append(f"{description}\n")
    ret.append(f"\n")
    ret.append(f"\n")

    ret.append("  \n__Expertise:__  \n")
    ret.append(f"{rnr_race_obj.subrace_name}s have expertise in one of the following checks:  \n")
    for expertise_stat in rnr_race_obj.expertise_choices:
        for expertise in core.get_expertises_for_stat(expertise_stat):
            ret.append(f"  * {expertise} _({core.abbreviate_stat(expertise_stat, capitalize_first=True)})_  \n")
    ret.append('  \n  ')


    abilities = core.filterAbilities(rnr_race_obj.abilities)

    if len(abilities) > 0:
        ret.append(f"__{string.capwords(rnr_race_obj.subrace_name)} Abilities:__ \n")
        for key in ('general', 'combat'):
            if not key in abilities:
                continue
            ret.append(f"* __{mapAbilityType(key)}:__   \n")
            for ability, info in abilities[key].items():
                if 'cost' in info and info['cost'] not in [None, 0]:
                    ret.append(f"  * __{ability}:__ _(Cost {info['cost']})_ {info['verbose']}  \n")
                else:
                    ret.append(f"  * __{ability}:__ {info['verbose']}  \n")

    ret.append('  \n')
    ret.append(f"  \n___\n")
    return ret

def get_rnr_class_wrapper_markdown(rnr_class_wrapper, gender_mappings):

    preferred_image = gender_mappings.get(rnr_class_wrapper.class_name.lower().replace(" ", "_"), None)

    male = 'male' if preferred_image else 'female'

    absolute_art_folder = os.path.join(core.GLOBAL_ART_PATH, 'class')
    relative_art_folder = os.path.join('..', '..', 'images', 'class')

    image_path, attribution = core.get_gendered_art(relative_art_folder, absolute_art_folder, rnr_class_wrapper.class_name.lower(), male)

    ret = []

    sub_heading = False
    if len(rnr_class_wrapper.subclasses) > 1:
        ret.append(f"### {rnr_class_wrapper.class_name} \n")

        if image_path is not None and attribution is not None:
            ret.append(f"<img src='{image_path}' class=\"raceClassImage\" />\n\n")
            ret.append(attribution)
        sub_heading = True

    if 'description' in rnr_class_wrapper.class_data:
        ret.append('\n')
        ret.append(rnr_class_wrapper.class_data['description'])
        ret.append('\n')

    for subclass in sorted(rnr_class_wrapper.subclasses, key=lambda x: x.name):
        preferred_image = gender_mappings.get(subclass.subclass.lower().replace(" ", "_"), None)
        male = True if preferred_image else False
        ret += get_class_markdown(subclass, male=male, sub_heading=sub_heading)
    return ret

def get_rnr_race_wrapper_markdown(rnr_race_wrapper, gender_mappings):

    preferred_image = gender_mappings.get(rnr_race_wrapper.race_name.lower().replace(" ", "_"), None)
    male = 'male' if preferred_image else 'female'

    absolute_art_folder = os.path.join(core.GLOBAL_ART_PATH, 'race')
    relative_art_folder = os.path.join('..', '..', 'images', 'race')
    image_path, attribution = core.get_gendered_art(relative_art_folder, absolute_art_folder, rnr_race_wrapper.race_name.replace(' ','_').lower(), male)


    ret = []
    sub_heading = False
    if len(rnr_race_wrapper.subraces) > 1:
        ret.append(f"### {rnr_race_wrapper.race_name} \n")

        if image_path is not None and attribution is not None:
            ret.append(f"<img src='{image_path}' class=\"raceClassImage\" />\n\n")
            ret.append(attribution)
        sub_heading = True

    if 'description' in rnr_race_wrapper.race_data:
        ret.append('\n')
        ret.append(rnr_race_wrapper.race_data['description'])
        ret.append('\n')

    for subrace in sorted(rnr_race_wrapper.subraces, key=lambda x: x.name):
        preferred_image = gender_mappings.get(subrace.subrace_name.lower().replace(" ", "_"), None)
        male = True if preferred_image else False
        ret += get_rnr_race_markdown(subrace, male=male, sub_heading=sub_heading)


    return ret

def markdown_spellbooks():
    lines = []
    spellbooks = core.get_all_spellbooks()
    for spellbook, chapters in spellbooks.items():
        lines.append(f'## {string.capwords(spellbook.replace("_"," "))}  \n')
        for chapter, spell_list in chapters.items():
            lines.append(f'  \n### {string.capwords(chapter.replace("_"," "))}  \n')
            for spell, spell_data in spell_list.items():
                lines += markdown_spell(spell, spell_data)
    return lines

def format_spell_duration(duration):
    if duration in ['infinite', 'save']:
        return ''
    elif isinstance(duration, int):
        if duration == 0:
            return f' __Duration:__ Instantaneous'
        else:
            return f' __Duration:__ {duration} minute(s)'
    elif duration == 'concentration':
        return f' __Duration:__ {duration.title()}'
    else:
        return f' __Duration:__ {duration.title()}'

def format_effect(effect):
    s = ' '
    if 'condition' in effect:
        s += effect['condition']
    else:
        s += 'Effected enemies must make a'
    if 'save' in effect:
        s += f' {effect["save"]} or'
    s += f' {effect["description"]}'

    if 'repeat' in effect:
        s += 'The save may be repeated '
        s += ', or '.join(effect['repeat'])
    s += '.'
    return s

def convert_range(spell_range):
    if spell_range == 'self':
        return 'Self'
    elif spell_range == 'hand':
        return 'Hand to Hand'
    elif spell_range == 'close':
        return '15 feet'
    elif spell_range == 'near':
        return '30 feet'
    elif spell_range == 'mid':
        return '60 feet'
    elif spell_range == 'archer':
        return '90 feet'
    elif spell_range == 'far':
        return '300 feet'
    elif spell_range == 'infinite':
        return 'infinite'
    else:
        return 'UNKNOWN RANGE'


def markdown_spell(spell_name, spell_data):
    lines = []

    lines.append(f'#### {spell_name.title()}  \n')
    first_line = f'__Cost:__ {spell_data["cost"]} '

    if 'dice' in spell_data:
        if spell_data['purpose'] == 'healing':
            first_line += f' __Healing:__ {spell_data["dice"]}'
        else:
            first_line += f' __Damage:__ {spell_data["dice"]}'

    if 'range' in spell_data:
        first_line += f' __Range:__ {convert_range(spell_data["range"])}'

    first_line += format_spell_duration(spell_data['duration'])

    second_line = ''

    if 'hit' in spell_data:
        if spell_data['hit'] == 'roll':
            second_line += '__Roll to hit__'
        else:
            second_line += '__Always hits__'

    if 'casting_time' in spell_data:
        if isinstance(spell_data['casting_time'], int):
            second_line += f' __{spell_data["casting_time"]} minute casting time__'
        else:
            second_line += f' __{spell_data["casting_time"]} casting time__'
    # second_line = f'{spell_data["school"]}'

    description_line = spell_data['description']
    if 'effects' in spell_data:
        for effect in spell_data['effects']:
            description_line += format_effect(effect)

    print(spell_name)
    if 'upcast' in spell_data:
        print(spell_data['upcast'])
        if spell_data['upcast']['cost'] == 'scaling':
            description_line += ' Each additional action point spent on this spell'
        else:
            description_line += f" You may spend {spell_data['upcast']['cost']} additional action points on this spell to"

        description_line += f" {spell_data['upcast']['effect']}."

    lines.append(f'{first_line}  \n')
    lines.append(f'{second_line}  \n')
    lines.append(f'{description_line}  \n')
    return lines


def markdown_skills():

    lines = []
    for skill, info in core.GLOBAL_SKILL_DATA.items():
        lines.append(f'* __{skill}:__ { info["description"] }  \n')
        if 'requirements' in info:
            if 'skills' in info['requirements']:
                skill_list = [item for item in info['requirements']['skills']]
                lines.append(f"  * Skill Requirements: _{ ', '.join(skill_list) }_  \n")
            if 'stats' in info['requirements']:
                stat_str = [f'{stat}: {val}' for stat, val in info['requirements']['stats'].items() ]
                lines.append(f"  * Stat Requirements: _{ ', '.join(stat_str) }_  \n")
    return lines

def markdown_pantheon():

    lines = []

    for deity_type, evil_val in [('Light', False), ('Darkness', True)]:
        lines.append(f'### Gods of {deity_type}  \n')
        for deity, info in core.GLOBAL_PANTHEON.items():
            if info['evil'] != evil_val:
                continue
            lines.append(f'#### {deity.title()}  \n  \n')
            lines.append(f'{info["description"]}  \n  \n')
            # if not 'abilities' in info:
            #   continue
            # lines.append('__Gifts:__  \n  \n')
            # for i in range(30):
            #   for level in sorted(info['abilities'].keys()):
            #     actual_level = str(level.split('_')[-1])
            #     if str(i) == actual_level:
            #       lines.append(f'* __{level.replace("_", " ").title()}__  \n')
            #       for ability, ability_info in info['abilities'][level].items():
            #         lines.append(f'  * __{ability.replace("_", " ").title()}:__ {ability_info["description"]}  \n')


    return lines

def mapAbilityType(ability_type):
    if ability_type == "combat":
        return "Combat Abilities"
    elif ability_type == "advantage":
        return "Advantages"
    elif ability_type == 'disadvantage':
        return "Disadvantages"
    elif ability_type == "starting_item":
        return "Starting Items"
    elif ability_type == "choice":
        return "Choices"
    elif ability_type == 'rule':
        return "Rules"
    elif ability_type == 'spellbook':
        return "Spellbooks"
    elif ability_type == 'action':
        return "Actions"
    else:
        return "General Abilities"
