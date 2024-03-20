import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { RnRRace } from '../../data_types/Classes/RnRRace';

@Injectable({
  providedIn: 'root'
})
export class RaceService {
  private jsonUrl = 'assets/data/races.json'; // Local JSON file
  constructor(private http: HttpClient) {}

  getRaces(succinct: boolean): Observable<RnRRace[]> {
    return this.http.get<any[]>(this.jsonUrl).pipe(
      map(data => data.map(rdata => new RnRRace(rdata, succinct)))
    );
  }
}

