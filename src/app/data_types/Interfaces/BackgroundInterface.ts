// Define interface for background options
export interface BackgroundOption {
    question: string;
    answers: string[];
  }
  
  export interface Tip {
      name: string;
      text: string;
  }
  
  // Define interface for the background object
  export interface BackgroundData {
    name: string;
    description: string;
    options: BackgroundOption[];
    starting_equipment: string[];
    tips: Tip[];
  }
  