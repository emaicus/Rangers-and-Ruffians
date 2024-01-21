import { Component, OnInit } from '@angular/core';
import { Weapon } from "../../data_types/Weapon";
import { WeaponsService } from '../../services/weapons.service';
import { WeaponRendererComponent } from '../../rendering/weapon-renderer/weapon-renderer.component';
import { NgFor, NgIf } from '@angular/common';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-weapon-page',
  standalone: true,
  imports: [WeaponRendererComponent, NgFor, NgIf, CommonModule],
  templateUrl: './weapon-page.component.html',
  styleUrl: './weapon-page.component.scss'
})
export class WeaponPageComponent implements OnInit {
  weapons: Weapon[] = [];
  constructor(private weapon_service: WeaponsService) { }

  ngOnInit(): void {
    this.getWeapons();
  }

  getWeapons(): void {
    this.weapon_service.getWeapons()
    .subscribe(weapons => {
      this.weapons = weapons;
      // Sort the weapons array by some criteria, e.g., by name
      this.weapons.sort((a, b) => a.name.localeCompare(b.name));
    });
  }
}