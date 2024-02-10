import { RnRAbility } from "../Classes/RnRAbility";
import { AbilityData } from "../Interfaces/AbilityInterface";

// Define interface for metadata
export interface MonsterMetadata {
	type: 'Minion' | 'Heavy' | 'Villain';
	tier: 'Tier 1' | 'Tier 2' | 'Tier 3';
	monster_class: string;
	monster_family?: string;
}

// Define interface for summons
export interface MonsterSummons {
	wildshape: boolean;
}

// Define interface for speed
export interface MonsterSpeed {
	'Base Speed': number;
	'Flying Speed': number;
	'Swimming Speed': number;
}

// Define interface for stats
export interface MonsterStats {
	health: number;
	evasion: number;
	speed: MonsterSpeed;
	stat_bonus: number;
	spell_power: Number;
	size: number;
}

// Define interface for moveset
export interface MonsterMoveset {
	passive_abilities?: AbilityData[];
	combat_actions_per_turn: number;
	combat_actions?: AbilityData[];
	villain_actions_per_turn: number;
	villain_actions?: AbilityData[];
	lair_actions?: AbilityData[];
	dynamic_actions?: AbilityData[];
}

// Define interface for moveset
export interface InstantiatedMonsterMoveset {
	passive_abilities?: RnRAbility[];
	combat_actions_per_turn: number;
	combat_actions?: RnRAbility[];
	villain_actions_per_turn: number;
	villain_actions?: RnRAbility[];
	lair_actions?: RnRAbility[];
	dynamic_actions?: RnRAbility[];
}

// Define interface for monster
export interface MonsterData {
	name: string;
	metadata: MonsterMetadata;
	summons: MonsterSummons;
	stats: MonsterStats;
	moveset: MonsterMoveset;
}
