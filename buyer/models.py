from django.db import models
from myapp.models import Product

# Create your models here.

class Buyer(models.Model):

    name = models.CharField(max_length=50)
    email =  models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    address = models.TextField(null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    uid = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

# class Buy(models.Model):

#     j = models.CharField(max_length=56)