from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

