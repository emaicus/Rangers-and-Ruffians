import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RangerCompanionCreatureComponent } from './ranger-companion-creature.component';

describe('RangerCompanionCreatureComponent', () => {
  let component: RangerCompanionCreatureComponent;
  let fixture: ComponentFixture<RangerCompanionCreatureComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RangerCompanionCreatureComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(RangerCompanionCreatureComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
