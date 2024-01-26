import { Component, OnInit } from '@angular/core';
import { RnRMonster } from '../../data_types/Classes/RnRMonster';
import { MonsterService } from '../../services/monster_service/monster.service';
import { MonsterRendererComponent } from '../../rendering/monster-renderer/monster-renderer.component';
import { NgFor, NgIf } from '@angular/common';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-monster-page',
  standalone: true,
  imports: [MonsterRendererComponent, CommonModule, NgFor, NgIf],
  templateUrl: './monster-page.component.html',
  styleUrl: './monster-page.component.scss'
})
export class MonsterPageComponent {
  monsters: RnRMonster[] = [];

  constructor(private monster_service: MonsterService) { }

  ngOnInit(): void {
    this.getMonsters();
  }

  getMonsters(): void {
    this.monster_service.getMonsters()
    .subscribe(monsters => {
      this.monsters = monsters;
      // Sort the weapons array by some criteria, e.g., by name
      this.monsters.sort((a, b) => a.name.localeCompare(b.name));
    });
  }

}

