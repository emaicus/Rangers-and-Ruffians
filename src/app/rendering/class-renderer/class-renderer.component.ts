import { Component, Input, EventEmitter, Output, AfterViewInit, ViewChild, ElementRef } from '@angular/core';
import { RnRClass } from '../../data_types/Classes/RnRClass';
import { NgIf, NgFor, CommonModule} from '@angular/common';
import { AbilityRendererComponent } from '../ability-renderer/ability-renderer.component';
import { AttributedArtRendererComponent } from '../attributed-art/attributed-art-renderer/attributed-art-renderer.component';
import { SkillTreeRendererComponent } from '../skill-tree-renderer/skill-tree-renderer.component';
import { RangerCompanionCreatureComponent } from '../../rule_fragments/ranger-companion-creature/ranger-companion-creature.component';

@Component({
  selector: 'app-class-renderer',
  standalone: true,
  imports: [CommonModule, NgIf, NgFor, AbilityRendererComponent, AttributedArtRendererComponent, SkillTreeRendererComponent, RangerCompanionCreatureComponent],
  templateUrl: './class-renderer.component.html',
  styleUrl: './class-renderer.component.scss'
})
export class ClassRendererComponent implements AfterViewInit {
  @Input() rnrclass?: RnRClass; 
  @Output() rendered = new EventEmitter<boolean>();
  isReadyToPrint = false;
  isRendered: boolean = false;

  constructor() {}

  ngAfterViewInit() {
    this.isRendered = true;
    this.rendered.emit(true);
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
