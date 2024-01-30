import { Component, Input } from '@angular/core';
import { RnRCondition } from '../../data_types/Classes/RnRCondition';
import { NgIf } from '@angular/common';
import { Subscription } from 'rxjs';
import { ConditionService } from '../../services/condition_service/condition.service';

@Component({
  selector: 'app-condition-renderer',
  standalone: true,
  imports: [NgIf],
  templateUrl: './condition-renderer.component.html',
  styleUrl: './condition-renderer.component.scss'
})
export class ConditionRendererComponent {
  @Input() conditionName?: string;
  condition?: RnRCondition;
  private conditionSubscription?: Subscription;

  constructor(private conditionService: ConditionService) {  }

  ngOnInit(): void {
    this.conditionSubscription = this.conditionService.artDataChanged.subscribe(() => {
      if (this.conditionName) {
        this.condition = this.conditionService.getConditionByTitle(this.conditionName.toLowerCase());
      }
    });
  }

  getCondition(c_name: string | undefined) {
    if(c_name){
      let ret = this.conditionService.getConditionByTitle(c_name.toLowerCase());
      return ret;
    }
    return undefined;
  }

  ngOnDestroy(): void {
    // Unsubscribe from the subscription to avoid memory leaks
    if (this.conditionSubscription) {
      this.conditionSubscription.unsubscribe();
    }
  }
}

