from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='customer/change_password.html'), name='change-password'),
    path('change-password-done/', auth_views.PasswordChangeDoneView.as_view(template_name='customer/change-password-done.html'), name='password_change_done')
]

