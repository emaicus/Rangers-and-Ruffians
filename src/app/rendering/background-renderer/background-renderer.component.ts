import { Component, Input, EventEmitter, Output, AfterViewInit } from '@angular/core';
import { NgIf, NgFor, CommonModule } from '@angular/common';
import { Background } from '../../data_types/Classes/RnRBackground';

@Component({
    selector: 'app-background-renderer',
    imports: [NgIf, NgFor, CommonModule],
    templateUrl: './background-renderer.component.html',
    styleUrl: './background-renderer.component.scss'
})
export class BackgroundRendererComponent implements AfterViewInit {
  @Input() background?: Background;
  @Output() rendered = new EventEmitter<boolean>();
  isRendered: boolean = false;

  ngAfterViewInit() {
    this.rendered.emit(true);
    this.isRendered = true;
  }
}
