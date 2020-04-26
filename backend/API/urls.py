from django.contrib import admin
from django.urls import path, include
import API.views as views
urlpatterns = [
    path('products/', views.products),
    path('products/<int:id>/', views.getProductById),
    path('user/<int:id>/products/', views.getUserByComment),
    path('comment/', views.list_comment),
    path('comment/<int:id>/', views.getCommentById),
    path('products/top_ten/',  views.getTopTen),
]
