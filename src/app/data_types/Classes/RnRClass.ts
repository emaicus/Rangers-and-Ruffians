import { ClassData, RecommendedStats, AbilitiesByLevel, Spells, HandbookEntry, HealthSchedule } from "../Interfaces/RnRClassInterface";
import { RnRAbility } from "./RnRAbility";
import { AbilityData } from "../Interfaces/AbilityInterface";
import { AttributedArt } from "./AttributedArt";

export interface InstantiatedLevels {
    [levelKey: string]: RnRAbility[];
}

interface InstantiatedSpells {
    "Tier 1": RnRAbility[];
    "Tier 2": RnRAbility[];
    "Tier 3": RnRAbility[];
}

interface InstantiatedDiscoverableAbilities {
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
    weapon_training: string[];
    discoverable_abilities: Spells;
    instantiated_discoverable_abilities: InstantiatedDiscoverableAbilities;

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
            "Charisma": data.recommended_stats.Charisma
        }

        this.handbook = data.handbook ?? [];
        this.starting_items = data.starting_items ?? [];
        
        const abilitiesByLevel = data?.abilities_by_level ?? {};
        const levelNum = (k: string) => Number(k.replace("level_", "")) || 0;
        const bucketOrder = (a: string, b: string) => {
            if (a === "standard" && b !== "standard") return -1;
            if (b === "standard" && a !== "standard") return 1;
            return a.localeCompare(b);
        };

        this.abilities_by_level = data?.abilities_by_level;
        this.instantiated_levels = Object.fromEntries(
            Object.entries(this.abilities_by_level ?? {})
              .sort(([a], [b]) => levelNum(a) - levelNum(b))
              .map(([levelKey, abilityList]) => [
                levelKey,
                (abilityList ?? [])
                  .map(ad => new RnRAbility(ad, succinct, true))
                  .sort((x, y) => x.name.localeCompare(y.name)),
              ])
          ) as InstantiatedLevels;

        
        this.spells = data.spells;
        this.instantiated_spells = {
          "Tier 1": ((data?.spells?.tier_1 as AbilityData[] || [])
            .map(abilityData => new RnRAbility(abilityData, succinct, true)))
            .sort((a, b) => a.name.localeCompare(b.name)),
          "Tier 2": ((data?.spells?.tier_2 as AbilityData[] || [])
            .map(abilityData => new RnRAbility(abilityData, succinct, true)))
            .sort((a, b) => a.name.localeCompare(b.name)),
          "Tier 3": ((data?.spells?.tier_3 as AbilityData[] || [])
            .map(abilityData => new RnRAbility(abilityData, succinct, true)))
            .sort((a, b) => a.name.localeCompare(b.name))
        }

        this.discoverable_abilities = data.discoverable_abilities;
        this.instantiated_discoverable_abilities = {
            "Tier 1": ((data?.discoverable_abilities?.tier_1 as AbilityData[] || [])
              .map(abilityData => new RnRAbility(abilityData, succinct, true)))
              .sort((a, b) => a.name.localeCompare(b.name)),
            "Tier 2": ((data?.discoverable_abilities?.tier_2 as AbilityData[] || [])
              .map(abilityData => new RnRAbility(abilityData, succinct, true)))
              .sort((a, b) => a.name.localeCompare(b.name)),
            "Tier 3": ((data?.discoverable_abilities?.tier_3 as AbilityData[] || [])
              .map(abilityData => new RnRAbility(abilityData, succinct, true)))
              .sort((a, b) => a.name.localeCompare(b.name))
          } 

        this.is_casting_class = (this.spells?.tier_1.length ?? 0) > 0;

        this.rule_sections = data.rule_sections ?? [];
        this.weapon_training = data.weapon_training ?? [];
    }
}