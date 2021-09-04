from django import forms
from .models import Customer


class RegisterCustomer(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='رمز عبور')

    class Meta:
        model = Customer
        exclude = ('user',)
        labels = {'first_name': 'نام', 'last_name': 'نام خانوادگی', 'email': 'ایمیل', 'phone': 'شماره تلفن'}


class LoginCustomer(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='رمز عبور')

    class Meta:
        model = Customer
        fields = ('email',)
        labels = {'email': 'ایمیل'}

