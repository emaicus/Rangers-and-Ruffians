import { ClassData, RecommendedStats, AbilitiesByLevel, ClassPaths, Spells, HandbookEntry, HealthSchedule } from "../Interfaces/RnRClassInterface";
import { RnRAbility } from "./RnRAbility";
import { AbilityData } from "../Interfaces/AbilityInterface";
import { AttributedArt } from "./AttributedArt";

export interface InstantiatedLevels {
    [levelKey: string]: InstantiatedAbilitiesAtLevel;
}

export interface InstantiatedAbilitiesAtLevel {
    // "standard" is optional
    standard?: RnRAbility[];
  
    // any number of path names
    [pathName: string]: RnRAbility[] | undefined;
  }

interface InstantiatedSpells {
    "Tier 1": RnRAbility[];
    "Tier 2": RnRAbility[];
    "Tier 3": RnRAbility[];
}

export class RnRClass implements ClassData {
    name: string;
    class_type: string;
    recommended_stats: RecommendedStats;
    health_schedule: HealthSchedule;
    abilities_by_level: AbilitiesByLevel;
    spells: Spells;
    handbook: HandbookEntry[];
    starting_items: string[];
    instantiated_levels : InstantiatedLevels;
    instantiated_spells: InstantiatedSpells;
    displayReccomendedStats;
    rule_sections: string[];
    is_casting_class: boolean;
    paths: ClassPaths;
    path_count: number;

    constructor(data: ClassData, succinct: boolean) {
        this.name = data.name;
        this.class_type = data.class_type;
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
        this.paths = data.paths ?? {};
        this.path_count = Object.keys(data.paths).length; 
        
        const abilitiesByLevel = data?.abilities_by_level ?? {};
        const levelNum = (k: string) => Number(k.replace("level_", "")) || 0;
        const bucketOrder = (a: string, b: string) => {
            if (a === "standard" && b !== "standard") return -1;
            if (b === "standard" && a !== "standard") return 1;
            return a.localeCompare(b);
        };

        this.abilities_by_level = data?.abilities_by_level;
        this.instantiated_levels = Object.fromEntries(
        Object.entries(abilitiesByLevel)
            .sort(([a], [b]) => levelNum(a) - levelNum(b))
            .map(([levelKey, buckets]) => {
            const instantiatedBuckets = Object.fromEntries(
                Object.entries(buckets ?? {})
                .sort(([a], [b]) => bucketOrder(a, b))
                .map(([bucketName, abilityList]) => [
                    bucketName,
                    (abilityList ?? [])
                        .map(ad => new RnRAbility(ad, succinct, true))
                        .sort((x, y) => x.name.localeCompare(y.name)),
                ])
            ) as InstantiatedAbilitiesAtLevel;

            return [levelKey, instantiatedBuckets];
            })
        ) as InstantiatedLevels;

        
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

        this.is_casting_class = (this.spells?.Tier_1.length ?? 0) > 0;

        this.rule_sections = data.rule_sections ?? [];
    }
}