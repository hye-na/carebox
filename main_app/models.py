from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    recipient = models.CharField(max_length=60)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=100)


# class Product(models.Model):
