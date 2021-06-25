from django.db import models
from django import forms
from django.forms import ModelForm, fields
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(ModelForm):

    nombre = forms.CharField(min_length=5, max_length=25)
    precio = forms.IntegerField(min_value=3000)
    oferta = forms.IntegerField(min_value=2000)
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','precio','oferta','tipo','imagen']
        

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']