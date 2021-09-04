from django import forms
from .models import Customer


class RegisterCustomer(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Customer
        exclude = ('user',)


class LoginCustomer(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Customer
        fields = ('email',)

