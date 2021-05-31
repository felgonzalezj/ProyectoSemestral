from django.urls import path
from .views import Home, index, Ofertas, Productos, agregar_producto

urlpatterns = [
    path('', Home, name="Home"),
    path('index/', index, name="index"),
    path('Ofertas/', Ofertas, name="Ofertas"),
    path('Productos/', Productos, name="Productos"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
]
