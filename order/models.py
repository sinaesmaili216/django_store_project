from django.db import models
from customer.models import Customer, Address
from product.models import Product


class Cart(models.Model):
    costumer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.costumer.first_name} {self.costumer.last_name}'


# class OrderItem(models.Model):
#     products = models.ManyToManyField(Product)
#     count = models.IntegerField(default=1)
#
#     PAYMENT_STATUS_PENDING = 'P'
#     PAYMENT_STATUS_COMPLETE = 'C'
#     PAYMENT_STATUS_DELIVERED = 'D'
#
#     PAYMENT_CHOICES = [
#         (PAYMENT_STATUS_PENDING, 'Pending'),
#         (PAYMENT_STATUS_COMPLETE, 'Complete'),
#         (PAYMENT_STATUS_DELIVERED, 'Delivered')
#     ]
#     payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default=PAYMENT_STATUS_PENDING)
#     placed_at = models.DateTimeField(auto_now_add=True)
#


# class Order(models.Model):
#     order_item = models.ForeignKey(OrderItem)
#     costumer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    #products = models.ManyToManyField(Product)
    # count = models.IntegerField(default=1)

    # PAYMENT_STATUS_PENDING = 'P'
    # PAYMENT_STATUS_COMPLETE = 'C'
    # PAYMENT_STATUS_DELIVERED = 'D'
    #
    # PAYMENT_CHOICES = [
    #     (PAYMENT_STATUS_PENDING, 'Pending'),
    #     (PAYMENT_STATUS_COMPLETE, 'Complete'),
    #     (PAYMENT_STATUS_DELIVERED, 'Delivered')
    # ]
    # payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default=PAYMENT_STATUS_PENDING)
    # placed_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f'{self.costumer} {self.products}'


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    PAYMENT_STATUS_PENDING = 'در انتظار'
    PAYMENT_STATUS_COMPLETE = 'تایید شده'
    PAYMENT_STATUS_DELIVERED = 'تحویل داده شد'

    PAYMENT_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'در انتظار'),
        (PAYMENT_STATUS_COMPLETE, 'تایید شده'),
        (PAYMENT_STATUS_DELIVERED, 'تحویل داده شد')
    ]
    payment_status = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default=PAYMENT_STATUS_PENDING)
    products = models.ManyToManyField(Product)
    placed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer.first_name} {self.customer.last_name}'


