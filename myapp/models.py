from unicodedata import category
from django.db import models
from django.shortcuts import render

# Create your models here.

class Seller(models.Model):

    doc_choice = (('pan','PAN Card '), ('aadhar','AAdhar Card'))

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile =  models.CharField(max_length=14)
    password = models.CharField(max_length=20)
    doc = models.CharField(max_length=20,choices=doc_choice)
    doc_number = models.CharField(max_length=20)
    address = models.TextField()
    verify = models.BooleanField(default=False)
    pic = models.FileField(upload_to='Profile',default='avtar.png')

    def __str__(self):
        return self.name + ' @  ' + self.email


class Product(models.Model):

    uid = models.ForeignKey(Seller,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    des = models.TextField()
    pic = models.FileField(upload_to='Products',null=True,blank=True)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.uid.name + ' @ ' + self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.name

