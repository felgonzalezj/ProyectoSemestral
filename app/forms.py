from django.db import models
from django import forms
from django.forms import ModelForm, fields
from .models import Producto

class ProductoForm(ModelForm):

    nombre = forms.CharField(min_length=5, max_length=25)
    precio = forms.IntegerField(min_value=3000)
    oferta = forms.IntegerField(min_value=2000)
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','precio','oferta','tipo','imagen']
        
