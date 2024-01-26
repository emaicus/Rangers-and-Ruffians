import { Component, OnInit } from '@angular/core';
import { NgFor, NgIf } from '@angular/common';
import { TopmatterComponent } from '../../../rendering/topmatter/topmatter.component';

import { Background } from '../../../data_types/Classes/RnRBackground';
import { BackgroundService } from '../../../services/background_service/background.service';
import { BackgroundRendererComponent } from '../../../rendering/background-renderer/background-renderer.component';

import { RnRRace } from '../../../data_types/Classes/RnRRace';
import { RaceService } from '../../../services/race_service/race.service';
import { RaceRendererComponent } from '../../../rendering/race-renderer/race-renderer.component';

import { RnRClass } from '../../../data_types/Classes/RnRClass';
import { RnRClassService } from '../../../services/rnr_class_service/rnr-class.service';
import { ClassRendererComponent } from '../../../rendering/class-renderer/class-renderer.component';

import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-character-page',
  standalone: true,
  imports: [TopmatterComponent, RaceRendererComponent, ClassRendererComponent, BackgroundRendererComponent, NgFor, NgIf, CommonModule],
  templateUrl: './character-page.component.html',
  styleUrl: './character-page.component.scss'
})
export class CharacterPageComponent implements OnInit {
  backgrounds: Background[] = [];
  races: RnRRace[] = []
  rnrclasses: RnRClass[] = [];

  constructor(
      private background_service: BackgroundService, 
      private race_service: RaceService, 
      private rnr_class_service : RnRClassService, 
  ) {}

  ngOnInit(): void {
    this.getBackgrounds();
    this.getRaces();
    this.getRnRClasses();
  }

  getBackgrounds(): void {
    this.background_service.getBackgrounds()
    .subscribe(backgrounds => {
      this.backgrounds = backgrounds;
      // Sort the weapons array by some criteria, e.g., by name
      this.backgrounds.sort((a, b) => a.name.localeCompare(b.name));
    });
  }

  getRaces(): void {
    this.race_service.getRaces()
    .subscribe(races => {
      this.races = races;
      // Sort the weapons array by some criteria, e.g., by name
      this.races.sort((a, b) => a.name.localeCompare(b.name));
    });
  }

  getRnRClasses(): void {
    this.rnr_class_service.getClasses()
    .subscribe(rnr_classes => {
      this.rnrclasses = rnr_classes;
      // Sort the weapons array by some criteria, e.g., by name
      this.rnrclasses.sort((a, b) => a.name.localeCompare(b.name));
    });
  }
}