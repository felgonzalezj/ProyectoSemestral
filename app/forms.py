from django.db import models
from django import forms
from django.forms import ModelForm, fields
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .validators import TamanoMaximoValidator
class ProductoForm(ModelForm):

    nombre = forms.CharField(min_length=5, max_length=25)
    precio = forms.IntegerField(min_value=3000)
    oferta = forms.IntegerField(min_value=2000)
    imagen = forms.ImageField(validators=[TamanoMaximoValidator(1)], required=False)

    def clean_nombre(self):
        nom = self.cleaned_data["nombre"]
        aux = Producto.objects.filter(nombre__iexact=nom).exists()

        if aux:
            raise ValidationError("Este Producto ya existe.")

        return nom
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','precio','oferta','tipo','imagen']
        

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']