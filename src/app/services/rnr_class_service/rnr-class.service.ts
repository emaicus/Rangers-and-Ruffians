import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { RnRClass } from '../../data_types/Classes/RnRClass';

@Injectable({
  providedIn: 'root'
})
export class RnRClassService {
  private jsonUrl = 'assets/data/classes.json'; // Local JSON file
  constructor(private http: HttpClient) {}

  getClasses(succinct: boolean): Observable<RnRClass[]> {
    return this.http.get<any[]>(this.jsonUrl).pipe(
      map(data => data.map(cdata => new RnRClass(cdata, succinct)))
    );
  }
}



