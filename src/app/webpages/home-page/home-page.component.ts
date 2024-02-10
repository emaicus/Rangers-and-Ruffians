import { Component, OnInit } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TopmatterComponent } from '../../rendering/topmatter/topmatter.component';
import { NgIf } from '@angular/common';


@Component({
  selector: 'app-home-page',
  standalone: true,
  imports: [TopmatterComponent, RouterLink, NgIf],
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.scss'
})
export class HomePageComponent implements OnInit {
  deferredPrompt: any;

  constructor() { }

  ngOnInit(): void {
    window.addEventListener('beforeinstallprompt', (event) => {
      // Prevent Chrome 67 and earlier from automatically showing the prompt
      event.preventDefault();
      // Stash the event so it can be triggered later.
      this.deferredPrompt = event;
    });
  }

  installPWA(): void {
    if (this.deferredPrompt) {
      // Show the prompt
      this.deferredPrompt.prompt();
      // Wait for the user to respond to the prompt
      this.deferredPrompt.userChoice.then((choiceResult :  { outcome: string }) => {
        if (choiceResult.outcome === 'accepted') {
          console.log('User accepted the install prompt');
        } else {
          console.log('User dismissed the install prompt');
        }
        this.deferredPrompt = null;
      });
    }
  }
}
