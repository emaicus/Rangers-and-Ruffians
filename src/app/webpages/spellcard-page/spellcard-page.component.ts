import { Component, OnInit } from '@angular/core';
import { SpellcardRendererComponent } from '../../rendering/spellcard-renderer/spellcard-renderer.component';
import { RnRClass } from '../../data_types/Classes/RnRClass';
import { RnRClassService } from '../../services/rnr_class_service/rnr-class.service';
import { RnRAbility } from '../../data_types/Classes/RnRAbility';
import { NgFor } from '@angular/common';

export interface AnnotatedAbility {
  ability: RnRAbility;
  class: string;
  level: string;
  path: string;
}

@Component({
  selector: 'app-spellcard-page',
  imports: [SpellcardRendererComponent, NgFor],
  templateUrl: './spellcard-page.component.html',
  styleUrl: './spellcard-page.component.scss'
})
export class SpellcardPageComponent implements OnInit{
  rnrClasses: RnRClass[] = [];
  activeCards: AnnotatedAbility[] = [];
  pagedAbilities: AnnotatedAbility[][] = [];
  readonly CARDS_PER_PAGE = 9;

  constructor(private rnrClassService: RnRClassService) {
  }

  ngOnInit(): void {
    this.getRnRClasses();
  }


  getRnRClasses(): void {
    this.rnrClassService.getClasses(true)
      .subscribe(rnr_classes => {
        this.rnrClasses = rnr_classes
          .sort((a, b) => a.name.localeCompare(b.name));
        this.selectClass("Bard");
      });
  
  }

  selectClass(className: string): void {
    const selectedClass = this.rnrClasses
      .find(c => c.name === className);
    if (!selectedClass) return;
  
    this.activeCards =
      this.extractAbilities(selectedClass);
  
    this.pagedAbilities =
      this.chunkArray(
        this.activeCards,
        this.CARDS_PER_PAGE
      );
  
  }
  
  
  // extractAbilities(rnrClass: RnRClass): RnRAbility[] {
  //   // Casting classes use spell tiers
  //   if (rnrClass.is_casting_class) {
  //     return Object
  //       .values(rnrClass.instantiated_spells)
  //       .flat();
  //   }
  
  //   // Martial classes
  //   return Object
  //     .values(rnrClass.instantiated_levels)
  //     .flatMap(level =>
  //       Object.values(level)
  //         .flatMap(bucket => bucket ?? [])
  //     )
  //     .filter((a): a is RnRAbility => a !== undefined);
  // }

  extractAbilities(rnrClass: RnRClass): AnnotatedAbility[] {

    const className = rnrClass.name;
  
    // =========================
    // Casting classes
    // =========================
    if (rnrClass.is_casting_class) {
    
      return Object.entries(rnrClass.instantiated_spells)
        .flatMap(([tier, abilities]) =>
          abilities.map((a: RnRAbility) => ({
            ability: a,
            class: className,
            level: tier,
            path: null
          }))
        );
    }
  
    // =========================
    // Martial classes
    // =========================
    const levels = rnrClass.instantiated_levels as Record<
      string,
      Record<string, RnRAbility[]>
    >;
  
    return Object.entries(levels)
      .flatMap(([level, buckets]) =>
        Object.entries(buckets ?? {}).flatMap(([bucket, abilityList]) =>
          (abilityList ?? [])
            .filter((a): a is RnRAbility => a !== undefined)
            .map((a: RnRAbility) => ({
              ability: a,
              class: className,
              level: this.formatLevel(level),
              path: (bucket !== "standard" ? bucket : "")
           }))
        )
      );
  }

  private formatLevel(level: string): string {
    return level
      .replace(/_/g, " ")
      .replace(/\b\w/g, c => c.toUpperCase());
  }
  
  
  chunkArray<T>(array: T[], chunkSize: number): T[][] {
    const result: T[][] = [];
    for (let i = 0; i < array.length; i += chunkSize) {
      result.push(
        array.slice(i, i + chunkSize)
      );
    }
    return result;
  }

  onClassChange(event: Event): void {
    const selectedName =
      (event.target as HTMLSelectElement).value;
    this.selectClass(selectedName);
  }
}
