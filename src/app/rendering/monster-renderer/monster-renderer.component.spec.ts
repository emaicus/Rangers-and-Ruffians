import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MonsterRendererComponent } from './monster-renderer.component';

describe('MonsterRendererComponent', () => {
  let component: MonsterRendererComponent;
  let fixture: ComponentFixture<MonsterRendererComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MonsterRendererComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(MonsterRendererComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
