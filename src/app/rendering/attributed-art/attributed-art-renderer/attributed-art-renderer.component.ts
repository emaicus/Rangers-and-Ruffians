import { Component, Input } from '@angular/core';
import { AttributedArt } from '../../../data_types/Classes/AttributedArt';
import { NgIf } from '@angular/common';
import { AttributionService } from '../../../services/attribution_service/attribution-service.service';
import { Subscription } from 'rxjs';
import { OnInit } from '@angular/core';

@Component({
    selector: 'app-attributed-art-renderer',
    imports: [NgIf],
    templateUrl: './attributed-art-renderer.component.html',
    styleUrl: './attributed-art-renderer.component.scss'
})
export class AttributedArtRendererComponent implements OnInit{
  @Input() artName?: string;
  art?: AttributedArt;
  private attributionSubscription?: Subscription;

  constructor(private attributionService: AttributionService) {  }

  ngOnInit(): void {
    this.attributionSubscription = this.attributionService.artDataChanged.subscribe(() => {
      if (this.artName) {
        this.art = this.attributionService.getArtByTitle(this.artName.toLowerCase());
      }
    });
  }

  getAttributedArt(art: string | undefined) {
    if(art){
      let ret = this.attributionService.getArtByTitle(art.toLowerCase());
      return ret;
    }
    return undefined;
  }

  testArtName(){
    return this.artName ?? 'nullartname';
  }

  ngOnDestroy(): void {
    // Unsubscribe from the subscription to avoid memory leaks
    if (this.attributionSubscription) {
      this.attributionSubscription.unsubscribe();
    }
  }
}

