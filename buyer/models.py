from django.db import models

# Create your models here.

class Buyer(models.Model):

    name = models.CharField(max_length=50)
    email =  models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    address = models.TextField(null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name
