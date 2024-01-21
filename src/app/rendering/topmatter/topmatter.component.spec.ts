import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TopmatterComponent } from './topmatter.component';

describe('TopmatterComponent', () => {
  let component: TopmatterComponent;
  let fixture: ComponentFixture<TopmatterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TopmatterComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(TopmatterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
