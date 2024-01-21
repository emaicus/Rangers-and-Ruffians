import { Routes } from '@angular/router';
import { HomePageComponent } from './webpages/home-page/home-page.component';
import { WeaponPageComponent } from './webpages/weapon-page/weapon-page.component';

export const routes: Routes = [ 
    { path: '', redirectTo: '/homepage', pathMatch: 'full' },
    { path: 'homepage', component: HomePageComponent },
    { path: 'weapons', component: WeaponPageComponent }
]