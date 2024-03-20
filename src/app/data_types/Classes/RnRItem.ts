import { AbilityData } from "../Interfaces/AbilityInterface"
import { ItemData } from "../Interfaces/ItemInterface"
import { RnRAbility } from "./RnRAbility"

export class RnRItem implements ItemData {
    name: string;
    goldValue: number;
    type: string;
    subtype: string;
    ability: AbilityData;
    instantiatedAbility: RnRAbility;

    constructor(data: ItemData) {
        this.name = data.name ?? "Unknown Item";
        this.goldValue = data.goldValue ?? 5;
        this.type = data.type ?? "Item"
        this.subtype = data.type ?? ""
        this.ability = data.ability;
        this.instantiatedAbility = new RnRAbility(data.ability, true, false);
    }
}