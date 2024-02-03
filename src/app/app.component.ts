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
import { ActivatedRoute } from '@angular/router';
import { NavigationService } from './services/navigation_service/navigation.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, MatSidenavModule, MatToolbarModule, MatButtonModule, MatIconModule, RouterLink],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'Rangers-and-Ruffians';

  constructor(private _location: Location, private router: Router, private activatedRoute: ActivatedRoute, private navService: NavigationService) {}

  navigateToPageAndFragment(page: string, fragment: string) {
    this.navService.navigateToPageAndFragment(page, fragment);
  }

  backClicked() {
    this._location.back();
  }

  homeClicked() {
    this.router.navigateByUrl('/homepage');
  }
}
