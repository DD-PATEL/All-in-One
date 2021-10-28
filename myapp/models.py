from django.db import models
from django.contrib.auth.models import User

# makemigrations - create changes and save it to a file 
# migrate - apply the changes which were created by makemigrations 

# Create your models here. 


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    product_name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product_name


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    byear = models.CharField(max_length=4)
    date = models.DateField()

    def __str__(self):
        return self.name
    