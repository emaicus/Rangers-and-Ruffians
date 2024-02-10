import { BackgroundData, BackgroundOption, Tip } from "../Interfaces/BackgroundInterface";

export class Background {
    name: string;
    description: string;
    options: BackgroundOption[];
    startingEquipment: string[];
    tips: Tip[];
    
    constructor(data: BackgroundData){
        this.name = data.name;
        this.description = data.description;
        this.options = data.options;
        this.startingEquipment = data.starting_equipment;
        this.tips = data.tips || [];
    }
    
    addArticle(item: string): string {
        // Function to determine whether to add "A " or "An "
        const vowels = ["a", "e", "i", "o", "u"];
        const firstLetter = item.toLowerCase().charAt(0);
        return vowels.includes(firstLetter) ? "an" : "a";
    }

}