import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { RnRMonster } from '../../data_types/Classes/RnRMonster';

@Injectable({
  providedIn: 'root'
})
export class MonsterService {
  private jsonUrl = 'assets/data/monsters.json'; // Local JSON file

  constructor(private http: HttpClient) {}

  getMonsters(): Observable<RnRMonster[]> {
    return this.http.get<any[]>(this.jsonUrl).pipe(
      map(data => data.map(mdata => new RnRMonster(mdata)))
    );
  }
}




