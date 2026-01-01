import { Component, OnInit,  ViewChild, AfterViewInit} from '@angular/core';
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
import { TableOfContentsComponent } from '../../../rendering/table-of-contents/table-of-contents.component';

@Component({
    selector: 'app-character-page',
    imports: [TopmatterComponent, RaceRendererComponent, ClassRendererComponent, BackgroundRendererComponent, NgFor, NgIf, CommonModule, TableOfContentsComponent],
    templateUrl: './character-page.component.html',
    styleUrl: './character-page.component.scss'
})
export class CharacterPageComponent implements OnInit, AfterViewInit{
  backgrounds: Background[] = [];
  races: RnRRace[] = []
  rnrclasses: RnRClass[] = [];
  @ViewChild(TableOfContentsComponent) tocComponent!: TableOfContentsComponent;

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

  ngAfterViewInit(): void {
    console.log('boop');
    setTimeout(() => {
      this.childRendered(true); // Check if all child components are rendered
    });
  }

  childRendered(isRendered: boolean) {
    this.tocComponent.generateTableOfContents('character');
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