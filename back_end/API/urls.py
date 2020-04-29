from django.contrib import admin
from django.urls import path, include
from API.views import list_products, list_categories, getProductById, deleteCategoryById, list_feedback
from API.cbv_views import PostFeedBack

urlpatterns = {

    path('products/', list_products),
    path('categories/', list_categories),
    path('categories/<int:id>/', deleteCategoryById),
    path('products/<int:id>/', getProductById),
    path('feedback/', list_feedback)
}