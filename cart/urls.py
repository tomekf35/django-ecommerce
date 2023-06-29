from django.urls import path
from .import views


app_name = 'cart'
urlpatterns = [
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('view/', views.view_cart, name='view_cart'),
]