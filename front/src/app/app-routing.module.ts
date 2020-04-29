import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {MenuComponent} from './menu/menu.component';
import {AppComponent} from './app.component';
import {MainComponent} from './main/main.component';
import {LoginComponent} from './login/login.component';
import {CategoryComponent} from './category/category.component';
import {DetailsComponent} from './details/details.component';
import {BasketComponent} from './basket/basket.component';
import {ContactComponent} from './contact/contact.component';
import {ProfileComponent} from './profile/profile.component';
import {EditorComponent} from './editor/editor.component';


const routes: Routes = [
  {path: 'main', component: MainComponent},
  {path: '', redirectTo: 'main', pathMatch: 'full'},
  {path: 'category/:id', component: CategoryComponent},
  {path: 'menu', component: MenuComponent},
  {path: 'profile', component: ProfileComponent},
  {path: 'details/:id', component: DetailsComponent},
  {path: 'basket', component: BasketComponent},
  {path: 'contact', component: ContactComponent},
  {path: 'login', component: LoginComponent},
  {path: 'editor', component: EditorComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
