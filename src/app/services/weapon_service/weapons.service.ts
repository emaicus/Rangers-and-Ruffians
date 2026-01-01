// data.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Weapon } from '../../data_types/Classes/Weapon';
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
}
