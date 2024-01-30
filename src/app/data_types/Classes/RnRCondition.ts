import { ConditionData } from "../Interfaces/ConditionInterface";

export class RnRCondition {
    name: string;
    balance: string;
    about: string;
    
    constructor(data: ConditionData){
        this.name = data.name ?? "";
        this.name = this.name.toLowerCase();
        this.balance = data.balance ?? "";
        this.about = data.about ?? "";
    }
}