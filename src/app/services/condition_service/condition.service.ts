import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { RnRCondition } from '../../data_types/Classes/RnRCondition';
import { ConditionData } from '../../data_types/Interfaces/ConditionInterface';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ConditionService {
  private jsonUrl = 'assets/data/conditions.json'; // Local JSON file
  private conditions: RnRCondition[] = [];

  private artDataChangedSubject = new BehaviorSubject<void | null>(null);
  artDataChanged: Observable<void | null> = this.artDataChangedSubject.asObservable();

  constructor(private http: HttpClient) {
    this.loadConditionData();
  }

  loadConditionData(): void {
    this.http.get<ConditionData[]>(this.jsonUrl).pipe(
      map((data: ConditionData[]) => {
        this.conditions = data.map(cdata => new RnRCondition(cdata));
        this.artDataChangedSubject.next(null); // Notify subscribers about changes
      })
    ).subscribe();
  }

  getConditionByTitle(name: string): any | undefined {
    return this.conditions.find((condition) => condition.name === name);
  }
}
  
