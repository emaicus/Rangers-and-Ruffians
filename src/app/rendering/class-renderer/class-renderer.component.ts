import { Component, Input, EventEmitter, Output, AfterViewInit } from '@angular/core';
import { RnRClass } from '../../data_types/Classes/RnRClass';
import { NgIf, NgFor, CommonModule } from '@angular/common';
import { AbilityRendererComponent } from '../ability-renderer/ability-renderer.component';
import { AttributedArtRendererComponent } from '../attributed-art/attributed-art-renderer/attributed-art-renderer.component';
import { SkillTreeRendererComponent } from '../skill-tree-renderer/skill-tree-renderer.component';

@Component({
  selector: 'app-class-renderer',
  standalone: true,
  imports: [CommonModule, NgIf, NgFor, AbilityRendererComponent, AttributedArtRendererComponent, SkillTreeRendererComponent],
  templateUrl: './class-renderer.component.html',
  styleUrl: './class-renderer.component.scss'
})
export class ClassRendererComponent implements AfterViewInit {
  @Input() rnrclass?: RnRClass; 
  @Output() rendered = new EventEmitter<boolean>();
  isRendered: boolean = false;

  ngAfterViewInit() {
    this.isRendered = true;
    this.rendered.emit(true);
  }

  printContent(divId: string): void {
    let printContents = document.getElementById(divId);

    if (!printContents) {
      console.error(`Element with id ${divId} not found.`);
      return;
    }
  
    let printWindow = window.open('', '_blank');
  
    if (!printWindow) {
      console.error('Failed to open print window.');
      return;
    }
  
    // Write the HTML content to the print window
    printWindow.document.write('<html><head><title>Print</title>');
  
    // Include the Angular stylesheets in the print window
    printWindow.document.write('<link rel="stylesheet" type="text/css" href="styles.css">');
  
    // Finish the head section and start the body section
    printWindow.document.write('</head><body>');
  
    // Write the HTML content of the element to be printed
    printWindow.document.write(printContents.innerHTML);
  
    // Finish writing to the print window
    printWindow.document.write('</body></html>');
    printWindow.document.close();
  
    // Trigger the print dialog
    printWindow.print();
  }
}
