import { Component, Input } from '@angular/core';
import { RouterLink } from '@angular/router';
import { NgIf, NgFor, NgStyle } from '@angular/common';
import { NavigationService } from '../../services/navigation_service/navigation.service';

@Component({
    selector: 'app-table-of-contents',
    imports: [RouterLink, NgIf, NgFor, NgStyle],
    templateUrl: './table-of-contents.component.html',
    styleUrl: './table-of-contents.component.scss'
})
export class TableOfContentsComponent {
  @Input() contentSelector: string = ".toc-section"; // CSS selector for the content container
  headings: { page: string, text: string, fragment: string }[] = [];

  constructor(private navService: NavigationService){}

  public generateTableOfContents(page: string) {
    this.headings = [];

    const contentSections = Array.from(document.querySelectorAll(`${this.contentSelector}`));
    for (const section of contentSections) {
      const text = section.textContent || '';
      const fragment = section.getAttribute('id') || '';
      this.headings.push({ page, text, fragment });
    }
  }

  navigateToPageAndFragment(page: string, fragment: string) {
    this.navService.navigateToPageAndFragment(page, fragment);
  }
}
