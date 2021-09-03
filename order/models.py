from django.db import models
from customer.models import Customer
from product.models import Product


class Cart(models.Model):
    costumer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.costumer.first_name} {self.costumer.last_name}'


class Order(models.Model):
    costumer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    count = models.IntegerField(default=1)

    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_DELIVERED = 'D'

    PAYMENT_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_DELIVERED, 'Delivered')
    ]
    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default=PAYMENT_STATUS_PENDING)
    placed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.costumer} {self.products}'

