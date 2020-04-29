import { Component, OnInit } from '@angular/core';
import {MenuService} from '../service/menu.service';
import {PRODUCT} from '../data/interface';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']
})
export class EditorComponent implements OnInit {

  data = {
    name: 'title',
    image: 'resoure',
    price: '15 - 20',
    category_id: 2,
    rating : 4.5,
    description: 'the best product',
    ref: 'no ref'
  }

  constructor(private menuService: MenuService) { }

  ngOnInit(): void {
  }

  add(): void {
      this.menuService.addItem(this.data).subscribe();
      console.log(this.data.category_id)
      this.menuService.addItem(this.data).subscribe(
        data => {
          this.data.category_id = data.category_id
          this.data.description = data.description
          this.data.name = data.name
          this.data.image = data.image
          this.data.rating = data.rating
          this.data.ref = data.ref
          this.data.price = data.price;
        }
    );
  }
}
