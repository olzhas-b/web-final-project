import { Component, OnInit } from '@angular/core';
import {MenuService} from '../service/menu.service';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {
  data = {
    UsernameOrTelephoneNumber: 'default',
    Email: 'olzhas@gmail.com',
    productID: 1,
    Message: 'message'
};
  constructor(private menuService: MenuService) { }

  ngOnInit(): void {
  }
  postFeedback() {
    this.menuService.addFeedBack(this.data).subscribe();
  }

}
