import { AttributedArtData } from "../Interfaces/AttributionInterface";
// Define interface for Handbook options


export class AttributedArt implements AttributedArtData {
    name: string = "";
    path_prefix: string = "";
    artist: string ="";
    license: string="";
    license_acronym="";
    license_url="";
    title="";
    url="";
    ai_art: boolean=false;
    imageExists: boolean = false;

    constructor (data: AttributedArtData) {
        this.name = data.name;
        this.ai_art = data.ai_art ?? false;

        if(this.ai_art == false) {
            this.artist = data.artist;
            this.license = data.license;
            this.license_acronym = data.license_acronym;
            this.license_url = data.license_url;
            this.title = data.title;
            this.url = data.url;
        } else {
            this.artist ="AI";
            this.license = "Public Domain";
            this.license_acronym = "Public Domain";
            this.license_url = "";
            this.title = data.title;
            this.url = "";
        }
        
        
        this.checkIfImageExists();
    }

    checkIfImageExists(): void {
        const imagePath = this.getImagePath();
        const img = new Image();

        img.onload = () => {
            this.imageExists = true;
        };

        img.onerror = () => {
            this.imageExists = false;
        };
        
        img.src = imagePath;
    }

    getImagePath(): string {
        return `assets/images/${this.name}.jpg`;
    }
}