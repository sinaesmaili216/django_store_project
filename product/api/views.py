from django.shortcuts import render
from django.views import View, generic

from product.models import Product, Category


class HomePagination(generic.ListView):
    template_name = 'product/index.html'
    queryset = Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.all().order_by('is_exist')[:8]

        context = {
            'categories': categories,
            'products': products,
        }
        return context

