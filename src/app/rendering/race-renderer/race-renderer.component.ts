import { Component, Input, EventEmitter, Output, AfterViewInit } from '@angular/core';
import { RnRRace } from '../../data_types/Classes/RnRRace';
import { NgIf, NgFor, CommonModule } from '@angular/common';
import { AbilityRendererComponent } from '../ability-renderer/ability-renderer.component';
import { AttributedArtRendererComponent } from '../attributed-art/attributed-art-renderer/attributed-art-renderer.component';

@Component({
    selector: 'app-race-renderer',
    imports: [CommonModule, NgIf, NgFor, AbilityRendererComponent, AttributedArtRendererComponent],
    templateUrl: './race-renderer.component.html',
    styleUrl: './race-renderer.component.scss'
})
export class RaceRendererComponent implements AfterViewInit {
  @Input() race?: RnRRace;
  @Output() rendered = new EventEmitter<boolean>();
  isRendered: boolean = false;

  ngAfterViewInit() {
    this.rendered.emit(true);
    this.isRendered = true;
  }
}
