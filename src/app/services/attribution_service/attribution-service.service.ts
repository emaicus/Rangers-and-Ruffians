import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { AttributedArt } from '../../data_types/Classes/AttributedArt';
import { AttributedArtData } from '../../data_types/Interfaces/AttributionInterface';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AttributionService {
  private jsonUrl = 'assets/data/attributions.json'; // Local JSON file
  private attributedArt: AttributedArt[] = [];

  private artDataChangedSubject = new Subject<void>();
  artDataChanged: Observable<void> = this.artDataChangedSubject.asObservable();

  constructor(private http: HttpClient) {
    this.loadAttributedArt();
  }

  loadAttributedArt(): void {
    this.http.get<AttributedArtData[]>(this.jsonUrl).pipe(
      map((data: AttributedArtData[]) => {
        this.attributedArt = data.map(adata => new AttributedArt(adata));
        this.artDataChangedSubject.next(); // Notify subscribers about changes
      })
    ).subscribe();
  }

  getArtByTitle(name: string): any | undefined {
    return this.attributedArt.find((art) => art.name === name);
  }
}
