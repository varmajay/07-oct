from django.contrib import admin
from myapp.models import *

# Register your models here.


# admin.site.register(Seller)

@admin.register(Seller)
class AdminSeller(admin.ModelAdmin):
    list_display = ['name','email','mobile','verify']

admin.site.register(Product)
admin.site.register(Category)