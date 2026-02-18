import { RnRAbility } from "./RnRAbility";
import { AbilityData } from "../Interfaces/AbilityInterface";
import { RaceData, Handbook } from "../Interfaces/RaceInterface";
  
export class RnRRace implements RaceData {
    name: string;
    handbook: Handbook;
    abilities: AbilityData[];
    instantiated_abilities: RnRAbility[];
    parent_class: string;
  
    constructor(data: RaceData, succinct: boolean = false) {
      this.name = data.name;
      this.handbook = data.handbook;
      this.abilities = data.abilities;
      this.instantiated_abilities = ((data.abilities as AbilityData[] || [])
                                      .map(abilityData => new RnRAbility(abilityData, succinct, false)))
                                      .sort((a, b) => a.name.localeCompare(b.name));
      this.parent_class = data.parent_class;
    }
  }
  
  