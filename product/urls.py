from django.urls import path

from .views import product_view_by_category #index,

app_name = 'product'
urlpatterns = [
   # path('index/', index, name='index'),
    path('category_products/<category>', product_view_by_category, name='category_products')
]
