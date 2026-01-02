import { ClassData, RecommendedStats, SkillTree, Spells, HandbookEntry, HealthSchedule } from "../Interfaces/RnRClassInterface";
import { RnRAbility } from "./RnRAbility";
import { AbilityData } from "../Interfaces/AbilityInterface";
import { AttributedArt } from "./AttributedArt";

interface InstantiatedSkillTree {
    tree_path: string,
    abilities: RnRAbility[];
}

interface InstantiatedSpells {
    "Tier 1": RnRAbility[];
    "Tier 2": RnRAbility[];
    "Tier 3": RnRAbility[];
}

export class RnRClass implements ClassData {
    name: string;
    recommended_stats: RecommendedStats;
    health_schedule: HealthSchedule;
    skill_tree: SkillTree;
    spells: Spells;
    handbook: HandbookEntry[];
    starting_items: string[];
    instantiated_skill_tree : InstantiatedSkillTree;
    instantiated_spells: InstantiatedSpells;
    displayReccomendedStats;
    rule_sections: string[];
    is_casting_class: boolean;
    

    constructor(data: ClassData, succinct: boolean) {
        this.name = data.name;
        this.health_schedule = data.health_schedule; 
        this.recommended_stats = data.recommended_stats;
        this.displayReccomendedStats = {
            "Strength": data.recommended_stats.Strength,
            "Dexterity": data.recommended_stats.Dexterity,
            "Intelligence": data.recommended_stats.Intelligence,
            "Inner Fire": data.recommended_stats.Inner_Fire,
            "Perception": data.recommended_stats.Perception,
            "Charisma": data.recommended_stats.Charisma
        }

        this.handbook = data.handbook ?? [];
        this.starting_items = data.starting_items ?? [];
        this.skill_tree = data.skill_tree;
        this.instantiated_skill_tree = {
            tree_path: data?.skill_tree?.tree_path ?? "",
            abilities: ((data?.skill_tree?.abilities as AbilityData[] || [])
                .map(abilityData => new RnRAbility(abilityData, succinct, true)))
                .sort((a, b) => a.name.localeCompare(b.name))
        };
        
        this.spells = data.spells;
        this.instantiated_spells = {
          "Tier 1": ((data?.spells?.Tier_1 as AbilityData[] || [])
            .map(abilityData => new RnRAbility(abilityData, succinct, true)))
            .sort((a, b) => a.name.localeCompare(b.name)),
          "Tier 2": ((data?.spells?.Tier_2 as AbilityData[] || [])
            .map(abilityData => new RnRAbility(abilityData, succinct, true)))
            .sort((a, b) => a.name.localeCompare(b.name)),
          "Tier 3": ((data?.spells?.Tier_3 as AbilityData[] || [])
            .map(abilityData => new RnRAbility(abilityData, succinct, true)))
            .sort((a, b) => a.name.localeCompare(b.name))
        }

        this.is_casting_class = this.instantiated_skill_tree.abilities.length === 0;;

        this.rule_sections = data.rule_sections ?? [];
    }
}