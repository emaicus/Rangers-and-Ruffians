import { Component, Input } from '@angular/core';
import { NgIf, NgFor, CommonModule } from '@angular/common';
import { Background } from '../../data_types/Classes/RnRBackground';

@Component({
  selector: 'app-background-renderer',
  standalone: true,
  imports: [NgIf, NgFor, CommonModule],
  templateUrl: './background-renderer.component.html',
  styleUrl: './background-renderer.component.scss'
})
export class BackgroundRendererComponent {
  @Input() background?: Background;
}
