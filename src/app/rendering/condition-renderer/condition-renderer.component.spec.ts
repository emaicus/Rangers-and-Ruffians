import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConditionRendererComponent } from './condition-renderer.component';

describe('ConditionRendererComponent', () => {
  let component: ConditionRendererComponent;
  let fixture: ComponentFixture<ConditionRendererComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ConditionRendererComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ConditionRendererComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
