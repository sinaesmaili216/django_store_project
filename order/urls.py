from django.urls import path

from order.views import cart_items, order

app_name = 'order'
urlpatterns = [
    path('cart_items/', cart_items, name='cart-items'),
    path('order/<pk>', order, name='order')
]
