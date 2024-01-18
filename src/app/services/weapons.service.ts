// data.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Weapon } from '../weapon';
import { map } from 'rxjs/operators';


@Injectable({
  providedIn: 'root',
})
export class WeaponsService {
  private jsonUrl = 'assets/data/weapons.json'; // Local JSON file

  constructor(private http: HttpClient) {}

  getWeapons(): Observable<Weapon[]> {
    return this.http.get<any[]>(this.jsonUrl).pipe(
      map(data => data.map(wdata => new Weapon(wdata.name, wdata.base_stat,
           wdata.value, wdata.damage_scaling, wdata.range, wdata.harried,
           wdata.handedness, wdata.abilities)))
    );
  }

  // getFirestoreData(): Observable<any> {
  //   // Implement logic to fetch data from Firestore (to be added in the future)
  //   // Example: return this.http.get('Firestore API endpoint');
  // }
}
