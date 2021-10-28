from django.contrib import admin
from django.urls import path
from myapp import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('contact', views.contactUs, name='contact'),

    #old code

    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('signup', views.signupPage, name='signup'),
    path('products', views.products, name='products'),
    path('create_product', views.createProduct, name='createproduct'),
    path('membership', views.membershipForm, name='membership'),
    
]