from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views import View, generic

from django.shortcuts import render, redirect

from customer.models import Customer
from order.models import Order
from product.api.serializers import ProductSerializer
from product.models import Product


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

#
# class CartItems(generic.ListView):
#     template_name = 'order/show_cart_items.html'
#     #queryset = Product.objects.all()
#
#     def get_context_data(self,request, *, object_list=None, **kwargs):
#         products = request.session['products']['products']
#
#         context = {
#             'products': products,
#         }
#         return context
#


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def order(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        discount = int(request.POST.get('discount-code'))
        final_price = quantity * product.price * (100 - discount) / 100

        return render(request, 'order/order_payment.html', context={'product': product, 'final_price': final_price, 'quantity': quantity})

    return render(request, 'order/order.html', context={'product': product})

# @api_view(['GET', 'POST'])
# @permission_classes((permissions.AllowAny,))
# def order_detail(request, pk):
#     product = Product.objects.get(id=pk)
#     if request.method == 'POST':
#         quantity = int(request.POST.get('quantity'))
#         discount = int(request.POST.get('discount-code'))
#         print(type(quantity))
#         print(type(discount))
#         final_price = quantity * product.price * (100 - discount) / 100
#
#         return render(request, 'order/order_payment.html', context={'product': product, 'final_price': final_price})
#
#     return render(request, 'order/order.html', context={'product': product})


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def create_order(request, pk):
    product = Product.objects.filter(id=pk)
    print((product))
    #create order for customer who want to buy his first product
    try:
        Order.objects.create(costumer=Customer.objects.get(user=request.user))
    except:
        pass
    order = Order.objects.get(costumer__user=request.user)
    order.products.add(1)
    order.save()
    return redirect('customer:profile')
