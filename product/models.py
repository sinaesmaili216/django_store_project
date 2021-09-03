from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    is_exist = models.BooleanField(default=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class DiscountCode(models.Model):
    code_name = models.CharField(max_length=6)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.code_name} {self.product}'

