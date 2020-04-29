import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';
import { PRODUCT, CATEGORY } from '../data/interface';
@Injectable({
  providedIn: 'root'
})
export class MenuService {

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  constructor(private http: HttpClient) {
  }
  private categoriesUrl = 'http://localhost:8000/api/categories/';  // URL to web api
  private productsUrl = 'http://localhost:8000/api/products/';
  private feedbackUrl = 'http://localhost:8000/api/feedback/';
  getOrders(): Observable<any[]> {
    return this.http.get<any[]>('api/order').pipe();
  }
  postOrder(product: any): Observable<any> {
    return this.http.post<any>('api/order', product, this.httpOptions);
  }
  getCategoryId(): Observable<any[]> {
    const url = `${this.categoriesUrl}`;
    return this.http.get<any[]>(this.categoriesUrl);
  }
  getProducts(): Observable<any[]> {
    return this.http.get<any[]>(this.productsUrl);
  }
  getProduct(body: any): Observable<any> {
    return this.http.put(this.productsUrl, this.httpOptions);
  }
  getProductsByCategory(): Observable<any[]> {
    return this.http.get<any[]>(this.productsUrl);
  }
  getDetails(id: number): Observable<PRODUCT> {
    const url = `${this.productsUrl}${id}`;
    return this.http.get<any>(url);
  }
  addFeedBack(feedback: any): Observable<any> {
    return this.http.post<any>(this.feedbackUrl, feedback, this.httpOptions);
  }
  getCategories(): Observable<any[]> {
    return this.http.get<any[]>(this.categoriesUrl);
  }
  addItem(product: any): Observable<any> {
    return this.http.post<any>(this.productsUrl, product, this.httpOptions);
  }
  deleteProductById(id: number): Observable<any> {
    console.log(`${this.productsUrl}${id}/`);
    return this.http.delete(`${this.productsUrl}${id}/`);
  }
  deleteCategoryById(id: number): Observable<any> {
    return this.http.delete(`${this.categoriesUrl}${id}/`);
  }
}
