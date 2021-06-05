from django.urls import path
from .views import Home, index, Ofertas, Productos, agregar_producto, modificar_producto, eliminar_producto

urlpatterns = [
    path('', Home, name="Home"),
    path('index/', index, name="index"),
    path('Ofertas/', Ofertas, name="Ofertas"),
    path('Productos/', Productos, name="Productos"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
]
