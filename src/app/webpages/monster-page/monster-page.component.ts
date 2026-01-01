import { Component, OnInit } from '@angular/core';
import { RnRMonster } from '../../data_types/Classes/RnRMonster';
import { MonsterService } from '../../services/monster_service/monster.service';
import { MonsterRendererComponent } from '../../rendering/monster-renderer/monster-renderer.component';
import { NgFor, NgIf } from '@angular/common';
import { CommonModule } from '@angular/common';
import {MatCheckboxModule} from '@angular/material/checkbox';
import {MatInputModule} from '@angular/material/input';
import {MatSelectModule} from '@angular/material/select';
import {MatFormFieldModule} from '@angular/material/form-field';
import {FormControl, FormsModule, ReactiveFormsModule} from '@angular/forms';
import {KeyValue} from '@angular/common';

interface GroupedMonsters {
  [key: string]: RnRMonster[]; // Each property represents a monster family, with an array of monster objects
}

@Component({
    selector: 'app-monster-page',
    imports: [MonsterRendererComponent, CommonModule, NgFor, NgIf, MatCheckboxModule, MatInputModule, MatSelectModule, MatFormFieldModule, FormsModule, ReactiveFormsModule],
    templateUrl: './monster-page.component.html',
    styleUrl: './monster-page.component.scss'
})
export class MonsterPageComponent {
  monsters: RnRMonster[] = [];
  selectedMonsters: GroupedMonsters = {};


  tierOptions: string[] = ['All', 'Tier 1', 'Tier 2', 'Tier 3'];
  chosenTier: string = 'All'; // Initialize to the default value 'All'

  specialTypeOptions: string[] = ['All', 'Druid Wildshape', "Ranger Companion"];
  chosenSpecialTypes: string = "All";

  constructor(private monster_service: MonsterService) { 
  }

  ngOnInit(): void {
    this.getMonsters();
  }

  getMonsters(): void {
    this.monster_service.getMonsters()
    .subscribe(monsters => {
      this.monsters = monsters;
      // Sort the weapons array by some criteria, e.g., by name
      this.monsters.sort((a, b) => a.name.localeCompare(b.name));
      this.selectedMonsters = this.groupMonsters(this.monsters);
    });
  }

  applyFilter(): void {
    console.log(this.chosenTier);
    let tmpmonsters: RnRMonster[] = [];

    if (this.chosenTier === 'All') {
      tmpmonsters = this.monsters.slice(); // Show all items
    } else {
      tmpmonsters = this.monsters.filter(item => item.metadata.tier === this.chosenTier);
    }

    if(this.chosenSpecialTypes === "Druid Wildshape") {
      tmpmonsters = tmpmonsters.filter(item => item.summons.wildshape);
    } else if (this.chosenSpecialTypes == "Ranger Companion") {
      tmpmonsters = tmpmonsters.filter(item => item.summons.ranger_companion);
    }

    this.selectedMonsters = this.groupMonsters(tmpmonsters);
  }

  groupMonsters(monsters: RnRMonster[]): GroupedMonsters {
    const groupedMonsters: GroupedMonsters = {};

    monsters.forEach((item) => {
      const group = item.metadata.monster_class;
      if (!groupedMonsters[group]) {
        groupedMonsters[group] = [];
      }
      groupedMonsters[group].push(item);
    });

    for (const group in groupedMonsters) {
      if (groupedMonsters.hasOwnProperty(group)) {
        groupedMonsters[group].sort((a, b) => {
          // Compare primary sort key
          if (a.metadata.monster_family < b.metadata.monster_family) {
            return -1;
          }
          if (a.metadata.monster_family > b.metadata.monster_family) {
            return 1;
          }
          
          // If primary sort keys are equal, perform secondary sort
          if (a.metadata.tier < b.metadata.tier) {
            return -1;
          }
          if (a.metadata.tier > b.metadata.tier) {
            return 1;
          }
          
          // If secondary sort keys are also equal, return 0 for no change in order
          return 0;
        });
      }
    }
    return groupedMonsters;
  }
}

