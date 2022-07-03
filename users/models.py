from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from category.models import Product


class CustomUser(AbstractUser):

    haveshop = models.BooleanField(default=False)



class Shop(models.Model):

    name_shop = models.CharField(max_length=255)
    unp = models.IntegerField()
    city = models.CharField(max_length=255)
    product_shop = models.CharField(max_length=255)
    quantity_product = models.PositiveIntegerField(default=1)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name_shop