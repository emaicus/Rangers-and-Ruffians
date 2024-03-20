// data.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { RnRItem } from '../../data_types/Classes/RnRItem';
import { map } from 'rxjs/operators';


@Injectable({
  providedIn: 'root',
})
export class ItemService {
  private jsonUrl = 'assets/data/items.json'; // Local JSON file

  constructor(private http: HttpClient) {}

  getItems(): Observable<RnRItem[]> {
    return this.http.get<any[]>(this.jsonUrl).pipe(
      map(data => data.map(idata => new RnRItem(idata)))
    );
  }

}
