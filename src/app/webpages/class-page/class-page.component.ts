import { AfterViewInit, Component,  OnInit, ViewChild} from '@angular/core';
import { TopmatterComponent } from '../../rendering/topmatter/topmatter.component';
import { NgFor, NgIf, CommonModule, KeyValue } from '@angular/common';
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
  classesByType: Record<string, RnRClass[]> = {}
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
      this.classesByType = this.groupByType(this.rnrClasses);
    });
  }

  // Group by type
  private readonly typeOrder = [
    'Tank',
    'Striker',
    'Battle Mage',
    'Support',
  ] as const;

  private readonly typeRank: Record<string, number> = Object.fromEntries(
    this.typeOrder.map((t, i) => [t, i])
  );

  typeOrderCompare = (
    a: KeyValue<string, RnRClass[]>,
    b: KeyValue<string, RnRClass[]>
  ): number => {
    const ra = this.typeRank[a.key] ?? 999;
    const rb = this.typeRank[b.key] ?? 999;
    return ra !== rb ? ra - rb : a.key.localeCompare(b.key);
  };

  private groupByType(classes: RnRClass[]): Record<string, RnRClass[]> {
    // seed so headers always appear even if empty
    const acc: Record<string, RnRClass[]> = Object.fromEntries(
      this.typeOrder.map(t => [t, [] as RnRClass[]])
    );

    for (const c of classes) {
      const key = c.class_type ?? 'Unknown';
      (acc[key] ??= []).push(c);
    }

    // optional: sort within each bucket by name
    for (const key of Object.keys(acc)) {
      acc[key].sort((a, b) => a.name.localeCompare(b.name));
    }

    return acc;
  }

}