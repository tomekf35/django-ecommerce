from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from items.models import Product
from .models import CartItem


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:view_cart')


@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items})

