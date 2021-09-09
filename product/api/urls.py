from django.urls import path

from product.api.views import HomePagination

urlpatterns = [
    path('', HomePagination.as_view(), name='home')
]
