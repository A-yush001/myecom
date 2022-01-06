from django.db import models
# noinspection PyUnresolvedReferences
from api.category.models import *


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=50)
    stocks = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# Create your models here.
    def __str__(self):
        return self.name
