export class Weapon {
    public name : String;
    public base_stat: String;
    public value : String;
    public damage_scaling : Object;
    public range: String;
    public harried: boolean;
    public handedness: String;
    public abilities: Object;

    constructor(name: string, base_stat : string, value : string, damage_scaling: Object, 
                    range : string, harried: boolean, handedness: string, abilities: Object) {
        this.name = name;
        this.base_stat = base_stat;
        this.value = value;
        this.damage_scaling = damage_scaling;
        this.range = range;
        this.harried = harried;
        this.handedness = handedness;
        this.abilities  = abilities;
    }
}