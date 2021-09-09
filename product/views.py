from django.shortcuts import render
from product.models import Product, Category


def product_view_by_category(request, category):
    products = Product.objects.filter(category__name=category)
    return render(request, 'product/category_products.html', context={'products': products})


