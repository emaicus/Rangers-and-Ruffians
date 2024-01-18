class Ability {
	name: string;
	ability_type: string;
	shouldDisplayActionType: boolean;
	cost: number;
	shouldDisplayCost: boolean;
	costString: string;
	duration: string | number;
	shouldDisplayDuration: boolean;
	durationString: string;
	range: string | number;
	shouldDisplayRange: boolean;
	rangeString: string;
	castingTime: string | number;
	shouldDisplayCastingTime: boolean;
	castingTimeString: string;
	radius: number;
	shouldDisplayRadius: boolean;
	requirements: object;
	description: string;
	shouldDisplayDescription: boolean;
	effect: object;
	shouldDisplayEffect: boolean;
	upcast: string;
	shouldDisplayUpcast: boolean;
	options: Array<any>;
	shouldDisplayOptions: boolean;
	damage: object;
	shouldDisplayDamage: boolean;
	isAoe: boolean;
	summonedCreature: string | object;
	shouldDisplaySummons: boolean;
	
	constructor(data: {} ) {
		this.name = data.name ?? "No Ability Name Entered";
		this.ability_type = data.type ?? "";
		this.shouldDisplayActionType = data.type != null;
		
		this.cost = data.cost ?? 0;
		this.shouldDisplayCost = data.cost != null;
		this.costString = `${this.cost} Action ${this.cost === 1 ? 'Point' : 'Points'}`;

		this.duration = data.duration ?? 0;
		this.shouldDisplayDuration = data.duration != null;
		if (typeof this.duration === 'number') {
		  this.durationString = `${this.duration} ${this.duration === 1 ? 'Turn' : 'Turns'}`;
		} else {
		  this.durationString = this.duration;
		}
		
		this.range = data.range ?? "Touch";
		this.shouldDisplayRange = data.range != null;
		this.rangeString = typeof this.range === "number" ? `{this.range} Feet` : data.range;
		
		this.castingTime = data.castingTime ?? "";
		this.shouldDisplayCastingTime = data.castingTime != null;
		this.castingTimeString = this.castingTime;
		
		this.radius = data.radius ?? 0;
		this.shouldDisplayRadius = data.radius != null;
		
		this.requirements = data.requirements ?? {};
		this.shouldDisplayRequirements = data.requirements != null;
		this.requirements['movement'] = this.requirements.movement ?? false;
		this.requirements['verbal'] = this.requirements.verbal ?? false;
		this.requirements['components'] = this.requirements.components ?? [];
		
		this.description = data.description;
		this.shouldDisplayDescription = true;

		this.effect = data.effect ?? {};
		this.shouldDisplayEffect = data.effects != null;
		this.effect.description = this.effect.description ?? "";
		this.effect.save = this.effect.save ?? "";
		this.effect.options = this.effect.options ?? [];
		// I'll have to load these from a service.
		this.effect.conditions = this.effect.conditions ?? [];
		
		this.upcast = data.upcast ?? "";
		this.shouldDisplayUpcast = data.upcast != null;
		
		this.options = data.options ?? [];
		this.shouldDisplayOptions = data.options != null;
		
		this.damage = data.damage_scaling ?? {};
		this.shouldDisplayDamage = data.damage_scaling != null;
		this.damage.multi_attack = this.damage.multi_attack ?? 1;
		this.damage.scaled_by = this.damage.scaled_by ?? {};
		this.damage.scaled_by.weapon = this.damage.scaled_by.weapon ?? false;
		this.damage.scaled_by.stat = this.damage.scaled_by.stat ?? false;
		this.damage.damage_shape = this.damage.damage_shape ?? "";
		this.isAoe = this.damage.damage_shape != "";
		
		this.summonedCreature = data.summonedCreature ?? "";
		this.shouldDisplaySummons = data.summonedCreature != null;		
	}
}
