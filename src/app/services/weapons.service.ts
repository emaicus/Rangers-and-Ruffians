// data.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Weapon } from '../data_types/Weapon';
import { map } from 'rxjs/operators';


@Injectable({
  providedIn: 'root',
})
export class WeaponsService {
  private jsonUrl = 'assets/data/weapons.json'; // Local JSON file

  constructor(private http: HttpClient) {}

  getWeapons(): Observable<Weapon[]> {
    return this.http.get<any[]>(this.jsonUrl).pipe(
      map(data => data.map(wdata => new Weapon(wdata)))
    );
  }

  // getFirestoreData(): Observable<any> {
  //   // Implement logic to fetch data from Firestore (to be added in the future)
  //   // Example: return this.http.get('Firestore API endpoint');
  // }
}
