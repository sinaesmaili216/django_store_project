from django.db import models

from store_project.utils import image_path_generator


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
    image = models.ImageField(upload_to=image_path_generator, null=True, default=None, verbose_name='product images')

    def __str__(self):
        return self.name


class DiscountCode(models.Model):
    code_name = models.CharField(max_length=6)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    percent = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.code_name} {self.product}'



