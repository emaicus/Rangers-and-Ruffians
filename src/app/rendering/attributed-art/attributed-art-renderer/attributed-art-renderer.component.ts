import { Component, Input } from '@angular/core';
import { AttributedArt } from '../../../data_types/Classes/AttributedArt';
import { NgIf } from '@angular/common';

@Component({
  selector: 'app-attributed-art-renderer',
  standalone: true,
  imports: [NgIf],
  templateUrl: './attributed-art-renderer.component.html',
  styleUrl: './attributed-art-renderer.component.scss'
})
export class AttributedArtRendererComponent {
  @Input() art?: AttributedArt;
}

