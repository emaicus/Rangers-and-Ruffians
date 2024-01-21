import { AbilityData } from "../Interfaces/AbilityInterface"
import { WeaponData, DamageScaling, Range } from "../Interfaces/WeaponInterface"
import { RnRAbility } from "./RnRAbility"

export class Weapon {
    public name : string;
    public baseStat: string;
    public tierOneDamage: string;
    public tierTwoDamage: string;
    public tierThreeDamage: string;
    public damageType: string;
    public range: Range;
    public harried: boolean;
    public handedness: string;
    public abilities: RnRAbility[];
    public tierOneValue: number;
    public tierTwoValue: number;
    public tierThreeValue: number;
    public handednessLine: string;

    constructor(data: WeaponData) {
        this.name = data.name ?? "Unknown Weapon";
        this.tierOneValue = data.goldValue ?? 5;
        this.tierTwoValue = this.tierOneValue * 10;
        this.tierThreeValue = this.tierOneValue * 100;
        this.tierOneDamage = data.damage_scaling.Common ?? "1d6";
        this.tierTwoDamage = data.damage_scaling["Mastercraft 1"] ?? "1d8";
        this.tierThreeDamage = data.damage_scaling["Mastercraft 2"] ?? "1d10";
        this.damageType = data.damage_scaling.damage_type ?? "blunt";
        this.range = data.range;

        this.baseStat = data.base_stat ?? "Strength";
        this.harried = data.harried ?? false;
        let harriedString = this.harried ? "Harried" : null;
        this.handedness = data.handedness ?? "One Handed";
        
        this.handednessLine = [this.baseStat, this.handedness,  harriedString].filter(value => value !== null && value !== undefined).join(', ');

        this.abilities = (data.abilities as AbilityData[] || []).map(abilityData => new RnRAbility(abilityData));
    }
}