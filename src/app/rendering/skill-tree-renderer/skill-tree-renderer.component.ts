import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-skill-tree-renderer',
  standalone: true,
  imports: [],
  templateUrl: './skill-tree-renderer.component.html',
  styleUrl: './skill-tree-renderer.component.scss'
})
export class SkillTreeRendererComponent implements OnInit{
  skill_tree_path?: string;
  @Input() rnr_class_name? : string;

  ngOnInit(){
    this.skill_tree_path = "assets/images/skill_trees/" + this.rnr_class_name?.toLowerCase() + ".jpg";
  }

}
