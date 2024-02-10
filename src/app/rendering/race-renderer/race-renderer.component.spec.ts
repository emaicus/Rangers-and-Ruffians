import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RaceRendererComponent } from './race-renderer.component';

describe('RaceRendererComponent', () => {
  let component: RaceRendererComponent;
  let fixture: ComponentFixture<RaceRendererComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RaceRendererComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(RaceRendererComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
