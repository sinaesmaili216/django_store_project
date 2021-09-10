from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views import View, generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from customer.models import Customer
from order.models import Order, OrderItem
from product.api.serializers import ProductSerializer
from product.models import Product, DiscountCode


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def cart(request, pk):
    if request.method == 'GET':
        response = dict()
        response['products'] = ProductSerializer(Product.objects.filter(id=pk), many=True).data

        request.session['products'] = response
        print(request.session['products'])

    return redirect('home')


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def cart_items(request):
    products = request.session['products']['products']
    return render(request, 'order/show_cart_items.html', context={'products': products})


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def order(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        discount = DiscountCode.objects.get(code_name=request.POST.get('discount-code'))
        discount = discount.percent
        final_price = quantity * product.price * (100 - discount) / 100

        return render(request, 'order/order_payment.html',
                      context={'product': product, 'final_price': final_price, 'quantity': quantity})

    return render(request, 'order/order.html', context={'product': product})


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
@login_required(login_url='/customer/login/')
def create_order(request, pk):
    product = Product.objects.get(id=pk)
    print(product)
    order = Order.objects.create(customer=Customer.objects.get(user=request.user))
    order_item = OrderItem.objects.create(order=order, product=product)
    order_item.save()

    return redirect('customer:profile')
