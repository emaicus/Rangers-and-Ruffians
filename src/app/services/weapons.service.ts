// data.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import * as weapons from '../weapons.json';


@Injectable({
  providedIn: 'root',
})
export class WeaponsService {
  private jsonUrl = 'assets/data.json'; // Local JSON file

  constructor(private http: HttpClient) {}

  getLocalData(): Observable<any> {
    return this.http.get(this.jsonUrl);
  }

  getFirestoreData(): Observable<any> {
    // Implement logic to fetch data from Firestore (to be added in the future)
    // Example: return this.http.get('Firestore API endpoint');
  }
}
