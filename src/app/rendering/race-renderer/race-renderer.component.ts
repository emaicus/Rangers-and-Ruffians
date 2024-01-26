import { Component, Input } from '@angular/core';
import { RnRRace } from '../../data_types/Classes/RnRRace';
import { NgIf, NgFor, CommonModule } from '@angular/common';
import { AbilityRendererComponent } from '../ability-renderer/ability-renderer.component';

@Component({
  selector: 'app-race-renderer',
  standalone: true,
  imports: [CommonModule, NgIf, NgFor, AbilityRendererComponent],
  templateUrl: './race-renderer.component.html',
  styleUrl: './race-renderer.component.scss'
})
export class RaceRendererComponent {
  @Input() race?: RnRRace;
}
