import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QuickReferencePageComponent } from './quick-reference-page.component';

describe('QuickReferencePageComponent', () => {
  let component: QuickReferencePageComponent;
  let fixture: ComponentFixture<QuickReferencePageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [QuickReferencePageComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(QuickReferencePageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
