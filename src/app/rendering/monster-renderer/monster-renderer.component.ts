import { Component, Input, EventEmitter, Output, AfterViewInit } from '@angular/core';
import { RnRMonster } from '../../data_types/Classes/RnRMonster';
import { NgIf, NgFor, CommonModule } from '@angular/common';
import { AbilityRendererComponent } from '../ability-renderer/ability-renderer.component';

@Component({
    selector: 'app-monster-renderer',
    imports: [CommonModule, NgIf, NgFor, AbilityRendererComponent],
    templateUrl: './monster-renderer.component.html',
    styleUrl: './monster-renderer.component.scss'
})
export class MonsterRendererComponent implements AfterViewInit {
  @Input() monster?: RnRMonster;
  @Output() rendered = new EventEmitter<boolean>();
  isRendered: boolean = false;
  isReadyToPrint = false;

  ngAfterViewInit() {
    this.rendered.emit(true);
    this.isRendered = true;
  }

  printContent(): void {
    this.isReadyToPrint = true;
    console.log(this.isReadyToPrint);

    // Wait for a short delay (to ensure the class is applied)
    setTimeout(() => {
      // Print the document
      window.print();

      // Reset flag after a short delay (to ensure printing is complete)
      setTimeout(() => {
        this.isReadyToPrint = false;
      }, 100); // Adjust delay as needed
    }, 100); // Adjust delay as needed
  }
}
