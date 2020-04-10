import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';
import { PRODUCT, CATEGORY } from '../data/interface';
@Injectable({
  providedIn: 'root'
})
export class MenuService {
  private categoriesUrl = 'api/categories';  // URL to web api
  private productsUrl = 'api/products';
  private detailsUrl = 'api/products';
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  constructor(private http: HttpClient) {
  }

  getOrders(): Observable<any[]> {
    return this.http.get<any[]>('api/order').pipe();
  }
  postOrder(product: any): Observable<any> {
    return this.http.post<any>('api/order', product, this.httpOptions);
  }
  getCategoryId(): Observable<any[]> {
    const url = `${this.categoriesUrl}`;
    return this.http.get<any[]>(this.categoriesUrl).pipe();
  }
  getProducts(): Observable<any[]> {
    return this.http.get<any[]>(this.productsUrl).pipe();
  }
  getProductsByCategory(): Observable<any[]> {
    return this.http.get<any[]>(this.productsUrl);
  }
  getDetails(id: number): Observable<PRODUCT> {
    const url = `api/products/${id}`;
    return this.http.get<PRODUCT>(url);
  }
  getCategories(): Observable<CATEGORY[]> {
    return this.http.get<CATEGORY[]>(this.categoriesUrl).pipe();
  }
}
