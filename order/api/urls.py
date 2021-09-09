from django.urls import path
from order.api.views import cart, cart_items, order, create_order

urlpatterns = [
    path('cart/<pk>', cart, name='cart'),
    path('cart_items/', cart_items, name='cart-items'),
    path('order/<pk>', order, name='order'),
    path('create_order/<pk>', create_order, name='create_order')
]
