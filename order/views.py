# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from product.models import Product
#
#
# def cart(request, pk):
#     request.session['products'] = Product.objects.get(id=pk)
#     print(request.session['products'])
#
#     return redirect('product:index')
