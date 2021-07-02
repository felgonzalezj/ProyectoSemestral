from django.db import models
from django.db.models import fields
from django.db.models.query import QuerySet
from .models import Producto, TipoProducto
from rest_framework import serializers


#class TipoProductoSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = TipoProducto
#        fields = ['tipo']
        

class ProductoSerializer(serializers.ModelSerializer):
    #tipo = TipoProductoSerializer(read_only=True)
    #TipoProducto = serializers.PrimaryKeyRelatedField(queryset=TipoProducto.objects.all(), source="tipo")

    class Meta:
        model = Producto
        fields = ['nombre','descripcion','precio','oferta','tipo','imagen']
        