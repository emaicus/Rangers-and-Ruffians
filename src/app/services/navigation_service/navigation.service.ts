import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class NavigationService {

  constructor(private router: Router) {}

  navigateToPageAndFragment(page: string, fragment: string) {
    this.router.navigate([page], { fragment: fragment }).then(() => {
      setTimeout(() => {
        const element = document.getElementById(fragment);
        if (element) {
          element.scrollIntoView({ behavior: 'auto', block: 'start' });
        }
      }, 150); // Adjust the delay as needed
    });
  }
}
