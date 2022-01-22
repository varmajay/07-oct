import re
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from random import choices, randrange
from django.conf import settings
from django.core.mail import send_mail
from json import loads

# Create your views here.

def index(request):
    uid = Seller.objects.get(email=request.session['email'])
    return render(request,'index.html',{'uid':uid})

def login(request):
    try:
        uid = Seller.objects.get(email=request.session['email'])
        return redirect('index')
    except:
        if request.method == 'POST':
            try:
                uid = Seller.objects.get(email=request.POST['email'])
                if request.POST['password'] == uid.password:
                    request.session['email'] = request.POST['email']
                    return redirect('index')
                return render(request,'login.html',{'msg':'incorrect password'})
            except:
                msg = 'Email is not register'
                return render(request,'login.html',{'msg':msg})
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        try:
            Seller.objects.get(email=request.POST['email'])
            msg = 'Email is Already register'
            return render(request,'register.html',{'msg':msg})
        except:
            # if len(request.POST['password']) > 7:
                if request.POST['password'] == request.POST['cpassword']:
                    otp = randrange(1000,9999)
                    subject = 'welcome to Ecomm'
                    message = f"""Hello {request.POST['name']},
                    Your OTP is {otp}"""
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [request.POST['email'], ]
                    send_mail( subject, message, email_from, recipient_list )
                    global data
                    data = {
                        "name" : request.POST['name'],
                        "email" : request.POST['email'],
                        "mobile" : request.POST['mobile'],
                        "doc" : request.POST['doc'],
                        "doc_number" : request.POST['doc_number'],
                        "address" : request.POST['address'],
                        "password" : request.POST['password'],
                    }
                    return render(request,'otp.html',{'otp':otp})

                return render(request,'register.html',{'msg':'both should be same'})
            # return render(request,'register.html',{'msg':'Atleast 8 char.'})

    return render(request,'register.html')

def profile(request):
    uid = Seller.objects.get(email=request.session['email'])
    if request.method == 'POST':
        uid.name = request.POST['name']
        uid.email = request.POST['email']
        uid.mobile = request.POST['mobile']
        uid.address = request.POST['address']
        if 'pic' in request.FILES:
            uid.pic = request.FILES['pic']
        uid.save()

    return render(request,'profile.html',{'uid':uid})

def tables(request):
    return render(request,'tables.html')

def otp(request):
    if request.method == 'POST':
        if request.POST['otp'] == request.POST['uotp']:
            # data = loads(request.POST['data'])
            # print(type(request.POST['data']))
            # print(type(data))
            global data
            Seller.objects.create(
                name = data['name'],
                email = data['email'],
                mobile = data['mobile'],
                password = data['password'],
                doc = data['doc'],
                doc_number = data['doc_number'],
                address = data['address'],
            )
            del data
            return render(request,'login.html',{'msg':'Account is created'})
        return render(request,'otp.html',{'msg':'Invalid OTP','otp':request.POST['otp'],'data':request.POST['data']})

    return render(request,'login.html')

def logout(request):
    del request.session['email']
    return redirect('login')

def forgot_password(request):
    if request.method == 'POST':
        try:
            uid = Seller.objects.get(email=request.POST['email'])
            password = ''.join(choices('qwyertovghlk34579385',k=8))
            subject = 'Reset Password'
            message = f"""Hello {uid.name},
            Your Password  is {password}"""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail( subject, message, email_from, recipient_list )
            uid.password = password
            uid.save()
            return JsonResponse({'msg':'New pass is sent on your email'})
        except:
            msg = 'Email is not register'
            return JsonResponse({'msg':msg})
    return render(request,'forgot-password.html')

