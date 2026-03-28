import { Component } from '@angular/core';
import { MarkdownModule } from 'ngx-markdown';

@Component({
  selector: 'app-quick-reference-page',
  imports: [MarkdownModule],
  templateUrl: './quick-reference-page.component.html',
  styleUrl: './quick-reference-page.component.scss'
})
export class QuickReferencePageComponent {

}
