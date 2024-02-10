import { Component, OnInit, AfterViewInit, ViewChild} from '@angular/core';
import { TopmatterComponent } from '../../rendering/topmatter/topmatter.component';
import { NgFor, NgIf, CommonModule } from '@angular/common';
import { TableOfContentsComponent } from '../../rendering/table-of-contents/table-of-contents.component';

import { RaceRendererComponent } from '../../rendering/race-renderer/race-renderer.component';
import { RnRRace } from '../../data_types/Classes/RnRRace';
import { RaceService } from '../../services/race_service/race.service';

@Component({
  selector: 'app-race-page',
  standalone: true,
  imports: [TopmatterComponent, RaceRendererComponent, NgFor, NgIf, CommonModule, TableOfContentsComponent],
  templateUrl: './race-page.component.html',
  styleUrl: './race-page.component.scss'
})
export class RacePageComponent implements OnInit, AfterViewInit {
  rnrRaces: RnRRace[] = [];
  @ViewChild(TableOfContentsComponent) tocComponent!: TableOfContentsComponent;
  constructor(private rnrRaceService: RaceService) {}

  ngOnInit(): void {
    this.getRaces();
  }

  ngAfterViewInit(): void {
    setTimeout(() => {
      this.childRendered(true); // Check if all child components are rendered
    });
  }

  childRendered(isRendered: boolean) {
    this.tocComponent.generateTableOfContents('races');
  }

  getRaces(): void {
    this.rnrRaceService.getRaces()
    .subscribe(races => {
      this.rnrRaces = races;
      // Sort the weapons array by some criteria, e.g., by name
      this.rnrRaces.sort((a, b) => a.name.localeCompare(b.name));
    });
  }

}