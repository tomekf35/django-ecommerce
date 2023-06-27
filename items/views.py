from django.shortcuts import render
from .models import Product


def all_products_view(request):
    products = Product.objects.all()
    return render(request, 'items/item_list.html', {'products': products})
