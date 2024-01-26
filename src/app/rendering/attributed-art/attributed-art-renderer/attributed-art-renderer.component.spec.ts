import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AttributedArtRendererComponent } from './attributed-art-renderer.component';

describe('AttributedArtRendererComponent', () => {
  let component: AttributedArtRendererComponent;
  let fixture: ComponentFixture<AttributedArtRendererComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AttributedArtRendererComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AttributedArtRendererComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
