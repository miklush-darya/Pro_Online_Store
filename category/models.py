from django.db import models

# Create your models here.


class Category(models.Model):
    
    name_category = models.CharField(max_length=200, db_index=True)
    
    def __str__(self):
        return self.name_category


class Product(models.Model):

    name_product = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)  

    
    def __str__(self):
        return self.name_product