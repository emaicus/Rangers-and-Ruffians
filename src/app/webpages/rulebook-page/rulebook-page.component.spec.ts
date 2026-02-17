import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RulebookPageComponent } from './rulebook-page.component';

describe('RulebookPageComponent', () => {
  let component: RulebookPageComponent;
  let fixture: ComponentFixture<RulebookPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RulebookPageComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RulebookPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
