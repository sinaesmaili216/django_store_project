from django.urls import path
from .views import register_customer, login_customer, profile, logout_customer, edit_profile, add_address, order_history

app_name = 'customer'
urlpatterns = [
    path('register/', register_customer, name='register'),
    path('login/', login_customer, name='login'),
    path('logout/', logout_customer, name='logout'),
    path('profile/', profile, name='profile'),
    path('edit_profile', edit_profile, name='edit_profile'),
    path('add_address/', add_address, name='add_address'),
    path('order_history/', order_history, name='order_history')

]
