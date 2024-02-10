import { TestBed } from '@angular/core/testing';

import { RnrClassService } from './rnr-class.service';

describe('RnrClassService', () => {
  let service: RnrClassService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RnrClassService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
