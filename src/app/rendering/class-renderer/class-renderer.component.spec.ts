import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClassRendererComponent } from './class-renderer.component';

describe('ClassRendererComponent', () => {
  let component: ClassRendererComponent;
  let fixture: ComponentFixture<ClassRendererComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ClassRendererComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ClassRendererComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
