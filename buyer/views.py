from django.shortcuts import render
from .models import *
from myapp import models as sm

# Create your views here.
def index(request):
    products = sm.Product.objects.all().order_by('?')
    categories = sm.Category.objects.all()
    return render(request,'buyer-index.html',{'products':products,'categories':categories})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')