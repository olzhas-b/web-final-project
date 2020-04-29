import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientInMemoryWebApiModule } from 'angular-in-memory-web-api';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import { MenuComponent } from './menu/menu.component';
import { HttpClientModule } from '@angular/common/http';
// import {InMemoryDataService} from './service/in-memory-data.service';
import { FootBarComponent } from './foot-bar/foot-bar.component';
import { MainComponent } from './main/main.component';
import { LoginComponent } from './login/login.component';
import { CategoryComponent } from './category/category.component';
import { DetailsComponent } from './details/details.component';
import { ContactComponent } from './contact/contact.component';
import { BasketComponent } from './basket/basket.component';
import { ProfileComponent } from './profile/profile.component';
import { EditorComponent } from './editor/editor.component';
import {FormsModule} from '@angular/forms';


// @ts-ignore
// @ts-ignore
// @ts-ignore
// @ts-ignore
@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    TopBarComponent,
    FootBarComponent,
    MainComponent,
    LoginComponent,
    CategoryComponent,
    DetailsComponent,
    ContactComponent,
    BasketComponent,
    ProfileComponent,
    EditorComponent,
  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        HttpClientModule,
        FormsModule,
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
