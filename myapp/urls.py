from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index, name='index'),
    path('',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('profile/',views.profile, name='profile'),
    path('tables/',views.tables, name='tables'),
    path('otp/',views.otp, name='otp'),
]
