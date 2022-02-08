from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='buyer-index'),
    path('buyer-login/',views.buyer_login,name='buyer-login'),
    path('buyer-logout/',views.buyer_logout,name='buyer-logout'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('view-product/<int:pk>',views.view_product,name='view-product'),
    path('add-to-cart/<int:pk>',views.add_to_cart,name='add-to-cart'),
    path('buyer-cart',views.buyer_cart,name='buyer-cart'),
    path('remove-from-cart/<int:pk>',views.remove_from_cart,name='remove-from-cart'),
    path('search/',views.search,name='search'),

]