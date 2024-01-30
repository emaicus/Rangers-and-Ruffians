import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button'; 
import { MatIconModule } from '@angular/material/icon';
import { Location } from '@angular/common';
import { RouterLink } from '@angular/router';
import { Router } from '@angular/router';
import { ActivatedRoute, NavigationEnd } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, MatSidenavModule, MatToolbarModule, MatButtonModule, MatIconModule, RouterLink],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'Rangers-and-Ruffians';

  constructor(private _location: Location, private router: Router, private activatedRoute: ActivatedRoute) {}

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

  backClicked() {
    this._location.back();
  }

  homeClicked() {
    this.router.navigateByUrl('/homepage');
  }
}
