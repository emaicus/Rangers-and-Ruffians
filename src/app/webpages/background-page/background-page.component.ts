import { Component, OnInit,  ViewChild, AfterViewInit} from '@angular/core';
import { TopmatterComponent } from '../../rendering/topmatter/topmatter.component';
import { NgFor, NgIf, CommonModule } from '@angular/common';
import { TableOfContentsComponent } from '../../rendering/table-of-contents/table-of-contents.component';

import { BackgroundRendererComponent } from '../../rendering/background-renderer/background-renderer.component';
import { Background } from '../../data_types/Classes/RnRBackground';
import { BackgroundService } from '../../services/background_service/background.service';

@Component({
    selector: 'app-background-page',
    imports: [TopmatterComponent, BackgroundRendererComponent, NgFor, NgIf, CommonModule, TableOfContentsComponent],
    templateUrl: './background-page.component.html',
    styleUrl: './background-page.component.scss'
})
export class BackgroundPageComponent  implements OnInit, AfterViewInit{
  backgrounds: Background[] = [];
  @ViewChild(TableOfContentsComponent) tocComponent!: TableOfContentsComponent;
  constructor(private background_service: BackgroundService) {}

  ngOnInit(): void {
    this.getBackgrounds();
  }

  ngAfterViewInit(): void {
    setTimeout(() => {
      this.childRendered(true); // Check if all child components are rendered
    });
  }

  childRendered(isRendered: boolean) {
    this.tocComponent.generateTableOfContents("backgrounds");
  }

  getBackgrounds(): void {
    this.background_service.getBackgrounds()
    .subscribe(backgrounds => {
      this.backgrounds = backgrounds;
      // Sort the weapons array by some criteria, e.g., by name
      this.backgrounds.sort((a, b) => a.name.localeCompare(b.name));
    });
  }
}