from django.urls import path, include

urlpatterns = [
    path('account/', include('account.api.urls')),
    path('customer/', include('customer.api.urls')),
    path('order/', include('order.api.urls'))
]
