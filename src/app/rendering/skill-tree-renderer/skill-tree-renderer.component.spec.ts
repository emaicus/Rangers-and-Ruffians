import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SkillTreeRendererComponent } from './skill-tree-renderer.component';

describe('SkillTreeRendererComponent', () => {
  let component: SkillTreeRendererComponent;
  let fixture: ComponentFixture<SkillTreeRendererComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SkillTreeRendererComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SkillTreeRendererComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
