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
import { SwUpdate } from '@angular/service-worker';

@Component({
    selector: 'app-root',
    imports: [CommonModule, RouterOutlet, MatSidenavModule, MatToolbarModule, MatButtonModule, MatIconModule, RouterLink],
    templateUrl: './app.component.html',
    styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'Rangers-and-Ruffians';

  constructor(private _location: Location, private router: Router, private activatedRoute: ActivatedRoute, private navService: NavigationService, private swUpdate: SwUpdate) {}

  navigateToPageAndFragment(page: string, fragment: string) {
    this.navService.navigateToPageAndFragment(page, fragment);
  }

  backClicked() {
    this._location.back();
  }

  homeClicked() {
    this.router.navigateByUrl('/homepage');
  }

  ngOnInit() {
    if (this.swUpdate.isEnabled) {
      this.swUpdate.versionUpdates.subscribe(evt => {
        switch (evt.type) {
          case 'VERSION_DETECTED':
            console.log(`Downloading new app version: ${evt.version.hash}`);
            if (confirm('A new version is available. Load New Version?')) {
              window.location.reload();
            }
            break;
          case 'VERSION_READY':
            console.log(`Current app version: ${evt.currentVersion.hash}`);
            console.log(`New app version ready for use: ${evt.latestVersion.hash}`);
            break;
          case 'VERSION_INSTALLATION_FAILED':
            console.log(`Failed to install app version '${evt.version.hash}': ${evt.error}`);
            break;
        }
      });
    }
  }
}
