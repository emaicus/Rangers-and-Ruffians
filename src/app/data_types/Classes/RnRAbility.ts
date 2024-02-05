import { AbilityData , Requirements, Effect, Damage, Summons} from "../Interfaces/AbilityInterface";

export class RnRAbility {
	name: string;
	abilityType: string;
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
	requirements: Requirements;
	requirementsArr: string = "";
	description: string;
	shouldDisplayDescription: boolean;
	effect: Effect;
	shouldDisplayEffect: boolean;
	upcast: string;
	shouldDisplayUpcast: boolean;
	options: Array<any>;
	shouldDisplayOptions: boolean;
	damageScaling: Damage;
	shouldDisplayDamage: boolean;
	isAoe: boolean;
	summonedCreature: Summons;
	shouldDisplaySummons: boolean;
	damageType: string;
	displayableDamageType : string;
	
	constructor(
		data: AbilityData,
		succinct: boolean
	) {
		this.name = data.name ?? "No Ability Name Entered";
		this.abilityType = data.ability_type ?? "";
		this.shouldDisplayActionType = data.ability_type != null;
		
		this.cost = data.cost ?? 0;
		this.shouldDisplayCost = data.cost != null && (!succinct || (succinct && data.cost != 0));
		this.costString = `${this.cost} Action ${this.cost === 1 ? 'Point' : 'Points'}`;

		this.duration = data.duration ?? 0;
		this.shouldDisplayDuration = data.duration != null &&  data.duration != "Inherited" && (!succinct || (succinct && data.duration != "Instantaneous"));
		if (typeof this.duration === 'number') {
		  this.durationString = `${this.duration} ${this.duration === 1 ? 'Turn' : 'Turns'}`;
		} else {
		  this.durationString = this.duration;
		}
		
		this.range = data.range ?? "Touch";
		this.shouldDisplayRange = data.range != null  &&  data.range != "Inherited"  && (!succinct || (succinct && !(data.range == "Touch" || data.range == "Self")));
		this.rangeString = typeof this.range === "number" ? `${this.range} Feet` : data.range.toString();
		
		this.castingTime = data.castingTime ?? "";
		this.shouldDisplayCastingTime = data.castingTime != null;
		this.castingTimeString = this.castingTime.toString();
		
		this.radius = data.radius ?? 0;
		this.shouldDisplayRadius = data.radius != null;
		
		this.requirements = data.requirements ?? {};
		this.requirements.movement = this.requirements.movement ?? false;
		this.requirements.verbal = this.requirements.verbal ?? false;
		this.requirements.components = this.requirements.components ?? [];

		if (this.requirements.movement) {
			this.requirementsArr += 'm, ';
		}
		if (this.requirements.verbal) {
			this.requirementsArr += 'v, ';
		}
		this.requirementsArr  += this.requirements.components.join(', ');
		  
		  // Remove the trailing comma if exists
		this.requirementsArr = this.requirementsArr.replace(/, $/, '');
		
		this.description = data.description;
		this.shouldDisplayDescription = true;

		this.effect = data.effect ?? {};
		this.shouldDisplayEffect = data.effect != null;
		this.effect.description = this.effect.description ?? "";
		this.effect.save = this.effect.save ?? "";
		this.effect.options = this.effect.options ?? [];
		// I'll have to load these from a service.
		this.effect.conditions = this.effect.conditions ?? [];
		
		this.upcast = data.upcast ?? "";
		this.shouldDisplayUpcast = data.upcast != null;
		
		this.options = data.options ?? [];
		this.shouldDisplayOptions = data.options != null;
		
		this.damageScaling = data.damage_scaling ?? {};
		this.shouldDisplayDamage = data.damage_scaling != null;
		this.damageScaling.multi_attack = this.damageScaling.multi_attack ?? 1;
		this.damageScaling.scaled_by = this.damageScaling.scaled_by ?? {};
		this.damageScaling.scaled_by.weapon = this.damageScaling.scaled_by.weapon ?? false;
		this.damageScaling.scaled_by.stat = this.damageScaling.scaled_by.stat ?? false;
		this.damageScaling.damage_shape = this.damageScaling.damage_shape ?? "";
		this.isAoe = this.damageScaling.damage_shape != "";
		this.damageScaling.all_tiers = this.damageScaling.all_tiers;
		this.damageScaling.tier_1 = this.damageScaling.tier_1;
		this.damageScaling.tier_2 = this.damageScaling.tier_2;
		this.damageScaling.tier_3 = this.damageScaling.tier_3;
		this.damageType = this.damageScaling?.damage_type ?? "";
		this.displayableDamageType = this.damageType != "Inherited" ? "" : this.damageType; 

		this.summonedCreature = data.summonedCreature ?? "";
		this.shouldDisplaySummons = data.summonedCreature != null;		
	}
}
