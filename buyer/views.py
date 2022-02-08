from itertools import product
from django.shortcuts import redirect, render
from .models import *
from myapp import models as sm

# Create your views here.
def index(request):
    products = sm.Product.objects.all().order_by('?')
    categories = sm.Category.objects.all()
    try:
        uid = Buyer.objects.get(email=request.session['bemail'])
        return render(request,'buyer-index.html',{'products':products,'uid':uid,'categories':categories})
    except:

        return render(request,'buyer-index.html',{'products':products,'categories':categories})

def about(request):
    return render(request,'about.html')

def buyer_login(request):
    try:
        uid = Buyer.objects.get(email=request.POST['email'])
        if uid.password == request.POST['password']:
            request.session['bemail'] = request.POST['email']
            if 'id' in request.POST:
                Product.objects.get(id=request.POST['id'])
            return render(request,'buyer-index.html',{'uid':uid})
    except:
        return render(request,'buyer-login.html',{'msg':'Email is not register'})    

def buyer_logout(request):
    del request.session['bemail']
    return redirect('buyer-index')

def contact(request):
    return render(request,'contact.html')

def view_product(request,pk):
    product = sm.Product.objects.get(id=pk)
    reco = sm.Product.objects.filter(category=product.category)[:4]
    return render(request,'view-product.html',{'product':product,'reco':reco})

def add_to_cart(request,pk):
    
    try:
        uid = Buyer.objects.get(email=request.session['bemail'])
        product = Product.objects.get(id=pk)
        try:
            cart = Cart.objects.get(uid=uid)
            cart.product.add(product)
            cart.save()
        except:
            Cart.objects.create(uid=uid)
            cart = Cart.objects.get(uid=uid)
            cart.product.add(product)
            cart.save()

        return render(request,'view-product.html',{'msg':'Product added','product':product})
    except:
        return render(request,'buyer-login.html')


def buyer_cart(request):
    uid = Buyer.objects.get(email=request.session['bemail'])
    cart = Cart.objects.get(uid=uid)
    return render(request,'buyer-cart.html',{'uid':uid,'cart':cart})


def remove_from_cart(request,pk):
    product = Product.objects.get(id=pk)
    uid = Buyer.objects.get(email = request.session['bemail'])
    cart = Cart.objects.get(uid=uid)
    cart.product.remove(product)
    cart.save()
    return redirect('buyer-cart')

def search(request):
    if request.method == 'POST':
        query = request.POST['search']
        products = list(Product.objects.filter(name=query))
        a = query.split()
            
        temp = list(products)[0]
        # for i in products:
        pro = list(Product.objects.filter(category =temp.category)) + products
        print(list(pro))
        return render(request,'search.html', {'pro':pro})
    return render(request,'search.html')