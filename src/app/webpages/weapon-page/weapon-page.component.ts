import { CommonModule } from '@angular/common';
import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { Weapon } from "../../data_types/Classes/Weapon";
import { WeaponsService } from '../../services/weapon_service/weapons.service';
import { WeaponRendererComponent } from '../../rendering/weapon-renderer/weapon-renderer.component';

import { TableOfContentsComponent } from '../../rendering/table-of-contents/table-of-contents.component';

import { RnRItem } from '../../data_types/Classes/RnRItem';
import { ItemService } from '../../services/item_service/item.service';
import { ItemRendererComponent } from '../../rendering/item-renderer/item-renderer.component';

import { NgFor, NgIf } from '@angular/common';

@Component({
    selector: 'app-weapon-page',
    imports: [WeaponRendererComponent, ItemRendererComponent, NgFor, NgIf, CommonModule, TableOfContentsComponent],
    templateUrl: './weapon-page.component.html',
    styleUrl: './weapon-page.component.scss'
})
export class WeaponPageComponent implements OnInit, AfterViewInit{
  weapons: Weapon[] = [];
  items: RnRItem[] = [];
  @ViewChild(TableOfContentsComponent) tocComponent!: TableOfContentsComponent;
  constructor(private weapon_service: WeaponsService, private item_service: ItemService) { }

  ngOnInit(): void {
    this.getWeapons();
    this.getItems();
  }

  ngAfterViewInit(): void {
    setTimeout(() => {
      this.childRendered(true); // Check if all child components are rendered
    });
  }

  childRendered(isRendered: boolean) {
    this.tocComponent.generateTableOfContents("weapons");
  }

  getWeapons(): void {
    this.weapon_service.getWeapons()
    .subscribe(weapons => {
      this.weapons = weapons;
      // Sort the weapons array by some criteria, e.g., by name
      this.weapons.sort((a, b) => a.name.localeCompare(b.name));
    });
  }

  getItems(): void {
    this.item_service.getItems()
    .subscribe(items => {
      this.items = items;
      // Sort the weapons array by some criteria, e.g., by name
      this.items.sort((a, b) => a.name.localeCompare(b.name));
    });
  }
}