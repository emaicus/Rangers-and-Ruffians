import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AbilityRendererComponent } from './ability-renderer.component';

describe('AbilityRendererComponent', () => {
  let component: AbilityRendererComponent;
  let fixture: ComponentFixture<AbilityRendererComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AbilityRendererComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AbilityRendererComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
