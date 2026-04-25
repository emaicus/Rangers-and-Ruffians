import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SpellcardRendererComponent } from './spellcard-renderer.component';

describe('SpellcardRendererComponent', () => {
  let component: SpellcardRendererComponent;
  let fixture: ComponentFixture<SpellcardRendererComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SpellcardRendererComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SpellcardRendererComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
