import { Component, Input } from '@angular/core';
import { RnRAbility } from '../../data_types/Classes/RnRAbility';
import { CommonModule } from '@angular/common';
import { NgIf, NgFor } from '@angular/common';
import { ConditionRendererComponent } from '../condition-renderer/condition-renderer.component';
import { NavigationService } from '../../services/navigation_service/navigation.service';

@Component({
  selector: 'app-ability-renderer',
  standalone: true,
  imports: [CommonModule, NgIf, NgFor, ConditionRendererComponent],
  templateUrl: './ability-renderer.component.html',
  styleUrl: './ability-renderer.component.scss'
})
export class AbilityRendererComponent {
  @Input() ability?: RnRAbility;
  constructor(private navService: NavigationService){}

  navigateToPageAndFragment(page: string, fragment: string) {
    this.navService.navigateToPageAndFragment(page, fragment);
  }
}

  