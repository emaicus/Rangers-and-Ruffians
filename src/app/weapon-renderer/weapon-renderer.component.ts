import { Component, Input } from '@angular/core';
import { Weapon } from '../data_types/Weapon'
import { CommonModule } from '@angular/common';
import { NgIf } from '@angular/common';

@Component({
  selector: 'app-weapon-renderer',
  standalone: true,
  imports: [CommonModule, NgIf],
  templateUrl: './weapon-renderer.component.html',
  styleUrl: './weapon-renderer.component.scss'
})
export class WeaponRendererComponent {
  @Input() weapon?: Weapon;
}