from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from account.models import User
from .forms import RegisterCustomer, LoginCustomer
from .models import Customer


def register_customer(request):
    if request.method == 'POST':
        form = RegisterCustomer(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password')

            create_user = User.objects.create_user(email=email, password=password)
            create_user.is_customer = True
            create_user.save()

            create_customer = Customer.objects.create(user=create_user, first_name=first_name, last_name=last_name, phone=phone)
            create_customer.save()
            login(request, create_user)

            return redirect('product:index')

    else:
        form = RegisterCustomer()

    return render(request, 'customer/register_customer.html', context={'form': form})


def login_customer(request):
    if request.method == 'POST':
        form = LoginCustomer(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('product:index')
            else:
                return HttpResponse('email or password is incorrect')
    else:
        form = LoginCustomer()

    return render(request, 'customer/login_customer.html', context={'form': form})


def logout_customer(request):
    logout(request)
    return redirect('product:index')


def profile(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    return render(request, 'customer/profile.html', context={'customer': customer})
