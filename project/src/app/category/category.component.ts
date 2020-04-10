import { Component, OnInit } from '@angular/core';
import {CATEGORY, PRODUCT} from '../data/interface';
import {MenuService} from '../service/menu.service';
import {ActivatedRoute, Router} from '@angular/router';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {
  products: any[] = [];
  // tslint:disable-next-line:variable-name
  last_part = '';
  id: PRODUCT[] = [];
  constructor(private menuService: MenuService, private route: ActivatedRoute, private router: Router) {
  }

  ngOnInit(): void {

    this.router.events.subscribe( (val) => {
      const id = +this.route.snapshot.paramMap.get('id');
      console.log(id)
      this.getProductsById(id);
  });
  }
  getProductsById(id): void {
    this.menuService.getProducts().subscribe(product => this.products = product.filter(o => o.category_id === id));
  }

  share(product: PRODUCT): void {
    window.open(`//api.whatsapp.com/send?phone=77478865590_NUMBER&text=${product.ref}`, '_blank');
  }
  details(product: PRODUCT): void {
    window.open(`//api.whatsapp.com/send?phone=77478865590_NUMBER&text=${product.ref}`);
  }


}
