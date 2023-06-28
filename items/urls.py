from django.urls import path
from . import views

app_name = 'items'
urlpatterns = [
    path('rig/', views.rig_products_view, name="products_rig"),
    path('procesor/', views.procesor_products_view, name="products_procesor"),
    path('gpu/', views.gpu_products_view, name="products_gpu"),
    path('ram/', views.ram_products_view, name="products_ram"),
    path('motherboard/', views.motherboard_products_view, name="products_motherboard"),
    path('ssd/', views.ssd_products_view, name="products_ssd"),
    path('psu/', views.psu_products_view, name="products_psu"),
    path('tower/', views.tower_products_view, name="products_tower"),
    path('all/', views.all_products_view, name="products_all"),
    path('search_results/', views.search_results, name='search_results'),
    path('<int:pk>/', views.item_detail, name='product_detail'),
]