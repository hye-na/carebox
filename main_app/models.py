from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORIES = (
    ('S', 'Snacks'),
    ('P', 'Personal Care'),
    ('G', 'Gift Cards'),
    ('H', 'Home Goods'),
    ('A', 'Accessories')
)


class Recipient(models.Model):
    name = models.CharField(max_length=60)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    # orders = models.ManyToManyField()
    category = models.CharField(
        max_length=1,
        choices=CATEGORIES,
        default='S',
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.id
