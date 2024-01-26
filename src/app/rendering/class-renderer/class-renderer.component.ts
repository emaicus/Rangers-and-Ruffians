import { Component, Input } from '@angular/core';
import { RnRClass } from '../../data_types/Classes/RnRClass';
import { NgIf, NgFor, CommonModule } from '@angular/common';
import { AbilityRendererComponent } from '../ability-renderer/ability-renderer.component';
import { AttributedArtRendererComponent } from '../attributed-art/attributed-art-renderer/attributed-art-renderer.component';
import { AttributionService } from '../../services/attribution_service/attribution-service.service';
import { Subscription } from 'rxjs';
import { AttributedArt } from '../../data_types/Classes/AttributedArt';

@Component({
  selector: 'app-class-renderer',
  standalone: true,
  imports: [CommonModule, NgIf, NgFor, AbilityRendererComponent, AttributedArtRendererComponent],
  templateUrl: './class-renderer.component.html',
  styleUrl: './class-renderer.component.scss'
})
export class ClassRendererComponent {
  @Input() rnrclass?: RnRClass; 
  private attributedArt?: AttributedArt;
  private attributionSubscription?: Subscription;

  constructor(private attributionService: AttributionService) {
    this.attributionSubscription = this.attributionService.artDataChanged.subscribe(() => {
      if (this.rnrclass) {
        this.attributedArt = this.attributionService.getArtByTitle(this.rnrclass.name.toLowerCase());
      }
    });
  }

  getAttributedArt(cls: RnRClass) {
    if(cls){
      let ret = this.attributionService.getArtByTitle(cls.name.toLowerCase());
      return ret;
    }
    return undefined;
  }

  ngOnDestroy(): void {
    // Unsubscribe from the subscription to avoid memory leaks
    if (this.attributionSubscription) {
      this.attributionSubscription.unsubscribe();
    }
  }

}
