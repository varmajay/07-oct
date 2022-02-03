from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='buyer-index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('view-product/<int:pk>',views.view_product,name='view-product'),
]