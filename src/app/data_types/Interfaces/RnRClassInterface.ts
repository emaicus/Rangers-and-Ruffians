import { AbilityData } from "./AbilityInterface";

export interface RecommendedStats {
    Charisma: number;
    Dexterity: number;
    Inner_Fire: number;
    Intelligence: number;
    Perception: number;
    Strength: number;
}

export interface AbilitiesByLevel {
    [levelKey: string]: AbilitiesAtLevel;
}

export interface ClassPaths {
    [pathKey: string]: string;
}
  
export interface AbilitiesAtLevel {
    // "standard" is optional
    standard?: AbilityData[];
  
    // any number of path names
    [pathName: string]: AbilityData[] | undefined;
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

export interface HealthSchedule {
    starting_health: number;
    standard_level_health_bonus: number;
    tier_increase_health_bonus: number;
}

export interface ClassData {
    name: string;
    class_type: string;
    recommended_stats: RecommendedStats;
    abilities_by_level: AbilitiesByLevel;
    spells: Spells;
    health_schedule: HealthSchedule;
    handbook: HandbookEntry[];
    starting_items: string[];
    rule_sections: string[];
    is_casting_class: boolean;
    paths: ClassPaths;
}
  
  