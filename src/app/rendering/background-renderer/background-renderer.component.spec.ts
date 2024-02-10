import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BackgroundRendererComponent } from './background-renderer.component';

describe('BackgroundRendererComponent', () => {
  let component: BackgroundRendererComponent;
  let fixture: ComponentFixture<BackgroundRendererComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BackgroundRendererComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(BackgroundRendererComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
