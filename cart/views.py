from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from items.models import Product
from .models import CartItem

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if created:
        cart_item.quantity = 1
    else:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart:view_cart')


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart_item.delete()

    return redirect('cart:view_cart')


@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = cart_items.aggregate(total_price=Sum(F('product__price') * F('quantity')))['total_price']
    if total_price is None:
        total_price = 0
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items, 'total_price': total_price})
