from django.urls import path

from .views import index, product_view_by_category

app_name = 'product'
urlpatterns = [
    path('index/', index, name='index'),
    path('category_products/<category>', product_view_by_category, name='category_products')
]
