import { AbilityData } from "./AbilityInterface"
// Define interface for damage scaling
export interface DamageScaling {
    damage_type: 'blunt' | 'piercing';
    'Common': string;
    'Mastercraft 1': string;
    'Mastercraft 2': string;
  }
  
  // Define interface for range
  export interface Range {
    reach: number;
    fired: number;
    thrown: number;
  }
  
  // Define interface for weapon
  export interface WeaponData {
    name: string;
    base_stat: 'Dexterity' | 'Strength' | 'Intelligence' | 'Inner Fire' | 'Perception' | 'Charisma';
    goldValue: number;
    damage_scaling: DamageScaling;
    range: Range;
    harried: boolean;
    handedness: 'One Handed' | 'Two Handed';
    abilities: AbilityData[];
  }
  
  