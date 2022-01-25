from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index, name='index'),
    path('',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('profile/',views.profile, name='profile'),
    path('tables/',views.tables, name='tables'),
    path('otp/',views.otp, name='otp'),
    path('logout/',views.logout, name='logout'),
    path('forgot-password/',views.forgot_password, name='forgot-password'),
    path('add-product',views.add_product,name='add-product'),
    path('my-products',views.my_products,name='my-products'),
]
