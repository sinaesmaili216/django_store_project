from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from account.models import User
from .forms import RegisterCustomer, LoginCustomer
from .models import Customer


def register_customer(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        create_user = User.objects.create_user(email=email, password=password)
        create_user.is_customer = True
        create_user.save()

        create_customer = Customer.objects.create(user=create_user, first_name=first_name, last_name=last_name, phone=phone)
        create_customer.save()
        login(request, create_user)

        return redirect('product:index')

    return render(request, 'customer/register_customer.html', context={})


def login_customer(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect('product:index')
        else:
            return HttpResponse('email or password is incorrect')

    return render(request, 'customer/login_customer.html', context={})


def logout_customer(request):
    logout(request)
    return redirect('product:index')


def profile(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    return render(request, 'customer/profile.html', context={'customer': customer})


def edit_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')

        user = request.user
        customer = Customer.objects.get(user=user)

        customer.first_name = first_name
        customer.last_name = last_name
        customer.phone = phone
        customer.save()

        return redirect('customer:profile')

    return render(request, 'customer/edit_profile.html')


