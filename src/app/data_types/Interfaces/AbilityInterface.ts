export interface AbilityData {
    name: string,
    ability_type: string,
	action_type: string;
    cost: number,
    duration: string | number,
    range: string | number,
    casting_time: string | number,
    radius: number,
    requirements: Requirements,
    description: string,
    effect: Effect,
    upcast: string,
    options: Array<any>,
    damage_scaling: Damage,
    summoned_creature: Summons,
	source_info: Source
}


export interface Source {
	source?: string;
	source_name?: string;
	type?: string;
	when?: string;
}

export interface Requirements {
	movement?: boolean;
	verbal?: boolean;
	components?: string[];
}

export interface Effect {
	description?: string;
	save?: string;
	options?: any[]; // Adjust the type based on the actual structure of options
	conditions?: string[];
}

export interface Damage {
	multi_attack?: number;
	scaled_by?: {
	  weapon?: boolean;
	  stat?: boolean;
	};
	damage_shape?: string;
	tier_1: string;
	tier_2: string;
	tier_3: string;
	all_tiers: string;
	damage_type: string;
}

export interface Summons {
	all_tiers: string;
	tier_1: string;
	tier_2: string;
	tier_3: string;
}