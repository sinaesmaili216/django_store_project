from django.urls import path
from order.api.views import cart

urlpatterns = [
    path('cart/<pk>', cart, name='cart')
]
