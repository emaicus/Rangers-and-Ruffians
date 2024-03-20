import { AbilityData } from "./AbilityInterface";

export interface RecommendedStats {
    Charisma: number;
    Dexterity: number;
    Inner_Fire: number;
    Intelligence: number;
    Perception: number;
    Strength: number;
}

export interface SkillTree {
    tree_path: string;
    abilities: AbilityData[];
}

export interface Spells {
    Tier_1: AbilityData[];
    Tier_2: AbilityData[];
    Tier_3: AbilityData[];
}

export interface HandbookEntry {
    title: string;
    display_title: boolean;
    text: string;
}

export interface ClassData {
    name: string;
    expertise: string;
    recommended_stats: RecommendedStats;
    health_dice: "1d6" | "1d8" | "1d10";
    skill_tree: SkillTree;
    spells: Spells;
    handbook: HandbookEntry[];
    starting_items: string[];
    rule_sections: string[];
}
  
  