import { Component, Input, EventEmitter, Output, AfterViewInit } from '@angular/core';
import { Weapon } from '../../data_types/Classes/Weapon';
import { NgIf, NgFor, CommonModule } from '@angular/common';
import { AbilityRendererComponent } from '../ability-renderer/ability-renderer.component';

@Component({
  selector: 'app-weapon-renderer',
  standalone: true,
  imports: [CommonModule, NgIf, NgFor, AbilityRendererComponent],
  templateUrl: './weapon-renderer.component.html',
  styleUrl: './weapon-renderer.component.scss'
})
export class WeaponRendererComponent implements AfterViewInit {
  @Input() weapon?: Weapon;
  @Output() rendered = new EventEmitter<boolean>();
  isRendered: boolean = false;

  ngAfterViewInit() {
    this.rendered.emit(true);
    this.isRendered = true;
  }
}