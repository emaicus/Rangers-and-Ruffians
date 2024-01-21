import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TopmatterComponent } from '../../rendering/topmatter/topmatter.component';

@Component({
  selector: 'app-home-page',
  standalone: true,
  imports: [TopmatterComponent, RouterLink],
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.scss'
})
export class HomePageComponent {

}
