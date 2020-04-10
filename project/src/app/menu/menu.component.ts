import { Component, OnInit } from '@angular/core';
import { CATEGORY, PRODUCT } from '../data/interface';
import {MenuService} from '../service/menu.service';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {
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
    console.log(1);
    this.menuService.getProducts().subscribe(product => this.products = product);
    console.log(this.products);

  }
  getCategory(): void {
    console.log(2);
    this.menuService.getCategories().subscribe(category => this.categories = category);
    console.log(this.categories);

  }

}
