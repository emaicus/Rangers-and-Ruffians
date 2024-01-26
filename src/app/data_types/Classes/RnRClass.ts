import { ClassData, RecommendedStats, SkillTree, Spells, HandbookEntry } from "../Interfaces/RnRClassInterface";
import { RnRAbility } from "./RnRAbility";
import { AbilityData } from "../Interfaces/AbilityInterface";
import { AttributedArt } from "./AttributedArt";

interface InstantiatedSkillTree {
    tree_path: string,
    abilities: RnRAbility[];
}

interface InstantiatedSpells {
    Tier_1: RnRAbility[];
    Tier_2: RnRAbility[];
    Tier_3: RnRAbility[];
}

export class RnRClass implements ClassData {
    name: string;
    expertise: string;
    recommended_stats: RecommendedStats;
    health_dice: "1d6" | "1d8" | "1d10";
    skill_tree: SkillTree;
    spells: Spells;
    handbook: HandbookEntry[];
    starting_items: string[];
    instantiated_skill_tree : InstantiatedSkillTree;
    instantiated_spells: InstantiatedSpells;
    

    constructor(data: ClassData) {
        this.name = data.name;
        this.expertise = data.expertise;
        this.recommended_stats = data.recommended_stats;
        this.health_dice = data.health_dice;

        this.handbook = data.handbook ?? [];
        this.starting_items = data.starting_items ?? [];
        this.skill_tree = data.skill_tree;
        this.instantiated_skill_tree = {
            tree_path: data?.skill_tree?.tree_path ?? "",
            abilities: (data?.skill_tree?.abilities as AbilityData[] || []).map(abilityData => new RnRAbility(abilityData, false))
        };
        
        this.spells = data.spells;
        this.instantiated_spells = {
          Tier_1: (data?.spells?.Tier_1 as AbilityData[] || []).map(abilityData => new RnRAbility(abilityData, false)),
          Tier_2: (data?.spells?.Tier_2 as AbilityData[] || []).map(abilityData => new RnRAbility(abilityData, false)),
          Tier_3: (data?.spells?.Tier_3 as AbilityData[] || []).map(abilityData => new RnRAbility(abilityData, false))
        }
    }
}