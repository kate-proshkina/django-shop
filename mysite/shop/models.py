from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    price = models.FloatField(default=0)

class Order(models.Model):
    product = models.ForeignKey(Product)
    amount = models.IntegerField(default=0)
    buyer = models.TextField(max_length=400)
    
