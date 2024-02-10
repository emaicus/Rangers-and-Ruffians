import { AbilityData } from "./AbilityInterface";
// Define interface for Handbook options
export interface HandbookOption {
    title: string;
    options: string[];
}
  
  // Define interface for Handbook
export interface Handbook {
    introduction: string[];
    you_may: HandbookOption;
    assumptions: HandbookOption;
    looks: { title: string; options: string }[];
    tips?: { name: string; text: string }[];
}
  
  // Define interface for Race
export interface RaceData {
    name: string;
    health_dice: "1d4" | "1d6" | "1d8";
    base_movement: number;
    handbook: Handbook;
    abilities: AbilityData[];
    parent_class: string;
}