import { Component, Input } from '@angular/core';
import { RnRAbility } from '../../data_types/Classes/RnRAbility';
import { CommonModule } from '@angular/common';
import { NgIf, NgFor } from '@angular/common';
import { ConditionRendererComponent } from '../condition-renderer/condition-renderer.component';

@Component({
  selector: 'app-ability-renderer',
  standalone: true,
  imports: [CommonModule, NgIf, NgFor, ConditionRendererComponent],
  templateUrl: './ability-renderer.component.html',
  styleUrl: './ability-renderer.component.scss'
})
export class AbilityRendererComponent {
  @Input() ability?: RnRAbility;
}

  