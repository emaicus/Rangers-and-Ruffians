import { Component, Input } from '@angular/core';
import { RnRClass } from '../../data_types/Classes/RnRClass';
import { NgIf, NgFor, CommonModule } from '@angular/common';
import { AbilityRendererComponent } from '../ability-renderer/ability-renderer.component';
import { AttributedArtRendererComponent } from '../attributed-art/attributed-art-renderer/attributed-art-renderer.component';

@Component({
  selector: 'app-class-renderer',
  standalone: true,
  imports: [CommonModule, NgIf, NgFor, AbilityRendererComponent, AttributedArtRendererComponent],
  templateUrl: './class-renderer.component.html',
  styleUrl: './class-renderer.component.scss'
})
export class ClassRendererComponent {
  @Input() rnrclass?: RnRClass; 

}
