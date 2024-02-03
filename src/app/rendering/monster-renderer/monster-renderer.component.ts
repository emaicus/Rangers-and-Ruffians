import { Component, Input, EventEmitter, Output, AfterViewInit } from '@angular/core';
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
export class MonsterRendererComponent implements AfterViewInit {
  @Input() monster?: RnRMonster;
  @Output() rendered = new EventEmitter<boolean>();
  isRendered: boolean = false;

  ngAfterViewInit() {
    this.rendered.emit(true);
    this.isRendered = true;
  }
}
