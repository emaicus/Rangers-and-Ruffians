import { Component, Input, EventEmitter, Output, AfterViewInit } from '@angular/core';
import { RnRItem } from '../../data_types/Classes/RnRItem';
import { NgIf, NgFor, CommonModule } from '@angular/common';
import { AbilityRendererComponent } from '../ability-renderer/ability-renderer.component';

@Component({
    selector: 'app-item-renderer',
    imports: [CommonModule, NgIf, NgFor, AbilityRendererComponent],
    templateUrl: './item-renderer.component.html',
    styleUrl: './item-renderer.component.scss'
})
export class ItemRendererComponent implements AfterViewInit {
  @Input() item?: RnRItem;
  @Output() rendered = new EventEmitter<boolean>();
  isRendered: boolean = false;

  ngAfterViewInit() {
    this.rendered.emit(true);
    this.isRendered = true;
  }
}