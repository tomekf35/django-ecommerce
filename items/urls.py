from django.urls import path
from . import views

app_name = 'items'
urlpatterns = [
    path('all/', views.all_products_view, name="products_all"),
]