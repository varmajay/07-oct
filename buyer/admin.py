from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['uid']
