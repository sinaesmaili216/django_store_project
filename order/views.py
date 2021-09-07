from django.http import HttpResponse
from django.shortcuts import render, redirect
from product.models import Product


def cart_items(request):
    products = request.session['products']['products']

    return render(request, 'order/show_cart_items.html', context={'products': products})


def order(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'order/order.html', context={'product': product})

