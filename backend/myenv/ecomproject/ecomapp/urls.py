from ecomapp import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.getRoutes, name="getRoutes"),
    path('products/', views.getProducts, name="getProducts"),
    path('products/<int:product_id>/', views.get_product_by_id, name="getProduct"),
    path('cart/add/', views.postCart, name="postCart"),
    path('cart/', views.getCartItems, name="getCartItems"),
    path('cart/<int:cart_item_id>/', views.removeCartItem, name="removeCartItem"),
]
