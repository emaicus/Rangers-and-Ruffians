import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WeaponRendererComponent } from './weapon-renderer.component';

describe('WeaponRendererComponent', () => {
  let component: WeaponRendererComponent;
  let fixture: ComponentFixture<WeaponRendererComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [WeaponRendererComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(WeaponRendererComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
