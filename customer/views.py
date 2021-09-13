from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from account.models import User
from order.models import Order, OrderItem
from .forms import RegisterCustomer, LoginCustomer, AddressForm
from .models import Customer, Address


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

        return redirect('home')

    return render(request, 'customer/register_customer.html', context={})


def login_customer(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            if 'next' in request.GET:
                return HttpResponseRedirect(request.GET['next'])
            return redirect('home')
        else:
            return HttpResponse('email or password is incorrect')

    return render(request, 'customer/login_customer.html', context={})


def logout_customer(request):
    logout(request)
    return redirect('home')


def profile(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    orders = OrderItem.objects.filter(order__customer__user_id=user.id)
    return render(request, 'customer/profile.html', context={'customer': customer, 'orders': orders})


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


def add_address(request):
    if request.method == 'POST':
        customer = Customer.objects.get(user=request.user)
        form = AddressForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data.get('city')
            street = form.cleaned_data.get('street')
            new_address = Address.objects.create(customer=customer, city=city, street=street)
            new_address.save()
    else:
        form = AddressForm()

    return render(request, 'customer/add_address.html', context={'form': form})




