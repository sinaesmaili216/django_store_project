from django.shortcuts import render
from product.models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'product/index.html', context={'products': products})
