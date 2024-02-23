import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GameDesignPageComponent } from './game-design-page.component';

describe('GameDesignPageComponent', () => {
  let component: GameDesignPageComponent;
  let fixture: ComponentFixture<GameDesignPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GameDesignPageComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(GameDesignPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
