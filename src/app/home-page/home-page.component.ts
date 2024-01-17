import { Component } from '@angular/core';
import { TopmatterComponent } from '../../topmatter/topmatter.component';

@Component({
  selector: 'app-home-page',
  standalone: true,
  imports: [TopmatterComponent],
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.scss'
})
export class HomePageComponent {

}
