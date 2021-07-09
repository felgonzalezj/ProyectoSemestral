from app.forms import ProductoForm
from app.models import Producto, TipoProducto, Suscriptor
from django.contrib import admin

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'precio', 'oferta', 'tipo',]
    search_fields = ['tipo']
    list_per_page = 6
    form = ProductoForm


admin.site.register(TipoProducto)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Suscriptor)