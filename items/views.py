from django.shortcuts import render
from .models import Product


def all_products_view(request):
    products = Product.objects.all()
    return render(request, 'items/item_list.html', {'products': products, 
                                                    'category': 'All Products'})
    
def rig_products_view(request):
    products = Product.objects.filter(category__name='Rig')
    return render(request, 'items/item_list.html', {'products': products, 
                                                    'category': 'Rig'})
    
def procesor_products_view(request):
    products = Product.objects.filter(category__name='Processor')
    return render(request, 'items/item_list.html', {'products': products, 
                                                    'category': 'Procesor'})
    
    
def gpu_products_view(request):
    products = Product.objects.filter(category__name='GPU')
    return render(request, 'items/item_list.html', {'products': products, 
                                                    'category': 'GPU Procesor'})
    
    
def ram_products_view(request):
    products = Product.objects.filter(category__name='RAM')
    return render(request, 'items/item_list.html', {'products': products, 
                                                    'category': 'RAM'})


def motherboard_products_view(request):
    products = Product.objects.filter(category__name='Motherboard')
    return render(request, 'items/item_list.html', {'products': products, 
                                                    'category': 'Motherboard'})
    
    
def ssd_products_view(request):
    products = Product.objects.filter(category__name='SSD')
    return render(request, 'items/item_list.html', {'products': products, 
                                                    'category': 'SSD'})
    
    
def psu_products_view(request):
    products = Product.objects.filter(category__name='PSU')
    return render(request, 'items/item_list.html', {'products': products, 
                                                    'category': 'PSU'})
    
    
def tower_products_view(request):
    products = Product.objects.filter(category__name='Tower')
    return render(request, 'items/item_list.html', {'products': products, 
                                                    'category': 'Tower'})