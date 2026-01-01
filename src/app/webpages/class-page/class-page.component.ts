import { AfterViewInit, Component,  OnInit, ViewChild} from '@angular/core';
import { TopmatterComponent } from '../../rendering/topmatter/topmatter.component';
import { NgFor, NgIf, CommonModule } from '@angular/common';
import { TableOfContentsComponent } from '../../rendering/table-of-contents/table-of-contents.component';

import { ClassRendererComponent } from '../../rendering/class-renderer/class-renderer.component';
import { RnRClass } from '../../data_types/Classes/RnRClass';
import { RnRClassService } from '../../services/rnr_class_service/rnr-class.service';

@Component({
    selector: 'app-class-page',
    imports: [TopmatterComponent, ClassRendererComponent, NgFor, NgIf, CommonModule, TableOfContentsComponent],
    templateUrl: './class-page.component.html',
    styleUrl: './class-page.component.scss'
})
export class ClassPageComponent implements OnInit, AfterViewInit{
  rnrClasses: RnRClass[] = [];
  @ViewChild(TableOfContentsComponent) tocComponent!: TableOfContentsComponent;
  constructor(private rnrClassService: RnRClassService) {}

  ngOnInit(): void {
    this.getRnRClasses();
  }

  ngAfterViewInit(): void {
    setTimeout(() => {
      this.childRendered(true); // Check if all child components are rendered
    });
  }

  childRendered(isRendered: boolean) {
    this.tocComponent.generateTableOfContents("classes");
  }

  getRnRClasses(): void {
    this.rnrClassService.getClasses(true)
    .subscribe(rnr_classes => {
      this.rnrClasses = rnr_classes;
      // Sort the weapons array by some criteria, e.g., by name
      this.rnrClasses.sort((a, b) => a.name.localeCompare(b.name));
    });
  }

}