import { Component } from '@angular/core';

@Component({
    selector: 'app-topmatter',
    imports: [],
    templateUrl: './topmatter.component.html',
    styleUrl: './topmatter.component.scss'
})
export class TopmatterComponent {
  portrait_banner_img = "assets/images/backdrops/portrait_banner.jpg";
  portrait_art_url = "https://www.deviantart.com/ncorva/art/Call-to-adventure-664775437";
  portrait_art_name = "Call to Adventure";
  portrait_artist_url = "https://www.deviantart.com/ncorva";
  portrait_artist_name = "ncorva";
  portrait_cc_url = "https://creativecommons.org/licenses/by-nc-nd/3.0/";
  portrait_cc_name = "CC BY-NC-ND 3.0";
  landscape_banner_img = "assets/images/backdrops/landscape_banner.jpg";
  landscape_art_url = "https://www.deviantart.com/themefinland/art/The-winding-path-commission-800945478";
  landscape_art_name = "The winding path"
  landscape_artist_url = "https://www.deviantart.com/themefinland";
  landscape_artist_name = "ThemeFinland";
  landscape_cc_url = "https://creativecommons.org/licenses/by-nc-sa/3.0/";
  landscape_cc_name = "CC BY-NC-SA 3.0"
}
