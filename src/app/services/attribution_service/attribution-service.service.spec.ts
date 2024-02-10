import { TestBed } from '@angular/core/testing';

import { AttributionServiceService } from './attribution-service.service';

describe('AttributionServiceService', () => {
  let service: AttributionServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AttributionServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
