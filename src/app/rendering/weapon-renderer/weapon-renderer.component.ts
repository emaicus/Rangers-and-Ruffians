import { Component, Input } from '@angular/core';
import { Weapon } from '../../data_types/Classes/Weapon';
import { CommonModule } from '@angular/common';
import { NgIf, NgFor } from '@angular/common';
import { AbilityRendererComponent } from '../ability-renderer/ability-renderer.component';

@Component({
  selector: 'app-weapon-renderer',
  standalone: true,
  imports: [CommonModule, NgIf, NgFor, AbilityRendererComponent],
  templateUrl: './weapon-renderer.component.html',
  styleUrl: './weapon-renderer.component.scss'
})
export class WeaponRendererComponent {
  @Input() weapon?: Weapon;
}