from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Address(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f'نام:{self.customer.first_name} {self.customer.last_name} آدرس:{self.city} {self.street}'
