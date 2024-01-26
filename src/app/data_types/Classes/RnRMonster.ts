import { RnRAbility } from "./RnRAbility";
import { MonsterData, MonsterMetadata, MonsterSummons, MonsterStats, MonsterMoveset, InstantiatedMonsterMoveset } from "../Interfaces/MonsterInterface";

// Define the class implementing the interface
export class RnRMonster implements MonsterData {
	name: string = '';
	metadata: MonsterMetadata;;
	summons: MonsterSummons;
	stats: MonsterStats;
	moveset: MonsterMoveset;
	instantiatedMoveset: InstantiatedMonsterMoveset;
	
	constructor( data : MonsterData) {
		this.name = data.name ?? "Unknown Name";
		
		this.metadata = {
			type: data?.metadata?.type ?? "Unassigned",
			tier: data?.metadata?.tier ?? "Unassigned",
			monster_class: data?.metadata?.monster_class ?? "Unassigned",
			monster_family: data?.metadata?.monster_family
		}
		
		this.summons = {
		  wildshape: data?.summons?.wildshape ?? false
		};
		
		this.stats = {
			health: data?.stats?.health ?? 0,
			evasion: data?.stats?.evasion ?? 0,
			stat_bonus: data?.stats?.stat_bonus ?? 0,
			spell_power: data?.stats?.spell_power ?? 0,
			size: data?.stats?.size  ?? 0,
			speed: data?.stats?.speed,
		};
		
		this.moveset = data?.moveset;
		this.instantiatedMoveset = {
		  combat_actions_per_turn: this.moveset?.combat_actions_per_turn ?? 1,
		  villain_actions_per_turn: this.moveset?.villain_actions_per_turn ?? 1,
		  passive_abilities: (this.moveset?.passive_abilities || []).map((ability: any) => new RnRAbility(ability, true)),
		  combat_actions: (this.moveset?.combat_actions || []).map((ability: any) => new RnRAbility(ability, true)),
		  villain_actions: (this.moveset?.villain_actions || []).map((ability: any) => new RnRAbility(ability, true)),
		  lair_actions: (this.moveset?.lair_actions || []).map((ability: any) => new RnRAbility(ability, true)),
		  dynamic_actions: (this.moveset?.dynamic_actions || []).map((ability: any) => new RnRAbility(ability, true)),
		};	
	}  

}
