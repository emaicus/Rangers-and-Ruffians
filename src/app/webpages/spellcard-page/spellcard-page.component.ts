import { Component, OnInit } from '@angular/core';
import { SpellcardRendererComponent } from '../../rendering/spellcard-renderer/spellcard-renderer.component';
import { RnRClass } from '../../data_types/Classes/RnRClass';
import { RnRClassService } from '../../services/rnr_class_service/rnr-class.service';
import { RnRAbility } from '../../data_types/Classes/RnRAbility';
import { NgFor } from '@angular/common';

@Component({
  selector: 'app-spellcard-page',
  imports: [SpellcardRendererComponent, NgFor],
  templateUrl: './spellcard-page.component.html',
  styleUrl: './spellcard-page.component.scss'
})
export class SpellcardPageComponent implements OnInit{
  rnrClasses: RnRClass[] = [];
  activeCards: RnRAbility[] = [];
  pagedAbilities: RnRAbility[][] = [];
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
        this.selectClass("Barbarian");
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

  extractAbilities(rnrClass: RnRClass): RnRAbility[] {

    // Casting classes
    const spellAbilities = rnrClass.is_casting_class
      ? Object.values(rnrClass.instantiated_spells ?? {}).flat()
      : [];
  
    // Martial classes
    const levelAbilities = Object.values(
      (rnrClass.instantiated_levels ?? {}) as Record<string, RnRAbility[]>
    ).flat();
  
    // Discoverable abilities
    const discoverableAbilities = Object.values(
      rnrClass.instantiated_discoverable_abilities ?? {}
    ).flat();
  
    // Combine all sources
    return [
      ...spellAbilities,
      ...levelAbilities,
      ...discoverableAbilities
    ];
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
