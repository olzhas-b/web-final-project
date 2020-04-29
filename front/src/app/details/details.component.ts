import { Component, OnInit } from '@angular/core';
import {CATEGORY, PRODUCT} from '../data/interface';
import {MenuService} from '../service/menu.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.css']
})
export class DetailsComponent implements OnInit {
  product: PRODUCT;
  constructor(private menuService: MenuService, private route: ActivatedRoute) {
  }

  ngOnInit(): void {
    this.getDetails();
  }
  share(product: PRODUCT): void {
    window.open(`//api.whatsapp.com/send?phone=77478865590_NUMBER&text=${product.ref}`, '_blank');
  }
  details(product: PRODUCT): void {
    // my code in future
  }
  getDetails(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    console.log(id)
    this.menuService.getDetails(id).subscribe(product => this.product = product);
  }
  delete(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.menuService.deleteProductById(id).subscribe();
    window.open(`http://localhost:4200/main`, '_self');
  }


}
