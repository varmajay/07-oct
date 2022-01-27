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
    path('add-product/',views.add_product,name='add-product'),
    path('my-products/',views.my_products,name='my-products'),
    path('delete-product/<int:pk>',views.delete_product,name='delete-product'),
    path('edit-product/<int:pk>',views.edit_product,name='edit-product'),
    path('disable-product/<int:pk>',views.disable_product,name='disable-product'),
    path('enable-product/<int:pk>',views.enable_product,name='enable-product'),
]
