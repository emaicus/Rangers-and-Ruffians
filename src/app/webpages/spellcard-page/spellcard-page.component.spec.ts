import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SpellcardPageComponent } from './spellcard-page.component';

describe('SpellcardPageComponent', () => {
  let component: SpellcardPageComponent;
  let fixture: ComponentFixture<SpellcardPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SpellcardPageComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SpellcardPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
