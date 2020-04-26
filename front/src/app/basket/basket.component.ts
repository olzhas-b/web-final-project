import { Component, OnInit } from '@angular/core';
import {CATEGORY, PRODUCT} from '../data/interface';
import {MenuService} from '../service/menu.service';

@Component({
  selector: 'app-basket',
  templateUrl: './basket.component.html',
  styleUrls: ['./basket.component.css']
})
export class BasketComponent implements OnInit {
  products: any[] = [];
  constructor(private menuService: MenuService) {
  }

  ngOnInit(): void {
    this.getOrder();
    console.log(1)
  }
  share(product: PRODUCT): void {
    window.open(`//api.whatsapp.com/send?phone=77478865590_NUMBER&text=${product.ref}`, '_blank');
  }
  details(product: PRODUCT): void {
    // my code in future
  }
  getOrder(): void {
    this.menuService.getOrders().subscribe(product => this.products = product);
    console.log(this.products);
  }
  getProduct(): void {
    this.menuService.getProducts().subscribe(product => this.products = product);
  }
  delete(product: PRODUCT): void {

  }


}
