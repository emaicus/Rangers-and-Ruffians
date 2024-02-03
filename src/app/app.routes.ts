import { Routes } from '@angular/router';
import { HomePageComponent } from './webpages/home-page/home-page.component';
import { WeaponPageComponent } from './webpages/weapon-page/weapon-page.component';
import { CharacterPageComponent } from './webpages/character-page/character-page/character-page.component';
import { MonsterPageComponent } from './webpages/monster-page/monster-page.component';
import { RacePageComponent } from './webpages/race-page/race-page.component';
import { BackgroundPageComponent } from './webpages/background-page/background-page.component';
import { ClassPageComponent } from './webpages/class-page/class-page.component';

export const routes: Routes = [ 
    { path: '', redirectTo: '/homepage', pathMatch: 'full' },
    { path: 'homepage', component: HomePageComponent },
    { path: 'weapons', component: WeaponPageComponent },
    { path: 'backgrounds', component: BackgroundPageComponent},
    { path: 'races', component: RacePageComponent},
    { path: 'classes', component: ClassPageComponent},
    { path: 'monsters', component: MonsterPageComponent}
]