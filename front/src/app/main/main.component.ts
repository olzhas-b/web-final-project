import { Component, OnInit } from '@angular/core';
import {CATEGORY, PRODUCT} from '../data/interface';
import {MenuService} from '../service/menu.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  categories: CATEGORY[] = [];
  products: PRODUCT[] = [];
  constructor(private menuService: MenuService) {
  }

  ngOnInit(): void {
    this.getCategory();
    this.getProduct();
  }
  share(product: PRODUCT): void {
    window.open(`//api.whatsapp.com/send?phone=77478865590_NUMBER&text=${product.ref}`, '_blank');
  }
  details(product: PRODUCT): void {
    // my code in future
  }
  getProduct(): void {
    this.menuService.getProducts().subscribe(product => this.products = product);
  }
  add(product: any): void {
    this.menuService.postOrder(product).subscribe(dish => this.products.push(dish) );
  }
  getCategory(): void {
    this.menuService.getCategories().subscribe(category => this.categories = category);
  }

}
