import { Component, Input } from '@angular/core';
import { RnRMonster } from '../../data_types/Classes/RnRMonster';
import { NgIf, NgFor, CommonModule } from '@angular/common';
import { AbilityRendererComponent } from '../ability-renderer/ability-renderer.component';

@Component({
  selector: 'app-monster-renderer',
  standalone: true,
  imports: [CommonModule, NgIf, NgFor, AbilityRendererComponent],
  templateUrl: './monster-renderer.component.html',
  styleUrl: './monster-renderer.component.scss'
})
export class MonsterRendererComponent {
  @Input() monster?: RnRMonster;
}
