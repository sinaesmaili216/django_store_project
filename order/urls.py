from django.urls import path

from order.views import cart_items

app_name = 'order'
urlpatterns = [
    path('cart_items/', cart_items, name='cart-items')
]
