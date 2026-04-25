import { Component, Input } from '@angular/core';
import { RnRAbility } from '../../data_types/Classes/RnRAbility';
import { NgIf, NgFor, TitleCasePipe} from '@angular/common';
import { ConditionRendererComponent } from '../condition-renderer/condition-renderer.component';

@Component({
  selector: 'app-spellcard-renderer',
  imports: [NgIf, NgFor, ConditionRendererComponent, TitleCasePipe],
  templateUrl: './spellcard-renderer.component.html',
  styleUrl: './spellcard-renderer.component.scss'
})
export class SpellcardRendererComponent {
  @Input() ability?: RnRAbility; 
  @Input() className?: string;
  @Input() level?: string;
  @Input() pathString?: string;

  stripAction(value?: string): string {
    if (!value) return '';
    if (value === "Action") return value;
  
    return value
      .replace(/\s*Action$/, '')
      .trim();
  }
}
