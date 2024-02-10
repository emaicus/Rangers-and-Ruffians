import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Background } from '../../data_types/Classes/RnRBackground';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class BackgroundService {
  private jsonUrl = 'assets/data/backgrounds.json'; // Local JSON file
  constructor(private http: HttpClient) {}

  getBackgrounds(): Observable<Background[]> {
    return this.http.get<any[]>(this.jsonUrl).pipe(
      map(data => data.map(bdata => new Background(bdata)))
    );
  }
}

