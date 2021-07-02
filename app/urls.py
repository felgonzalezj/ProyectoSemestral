from django.db import router
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos', ProductoViewSet)


urlpatterns = [
    path('', Home, name="Home"),
    path('index/', index, name="index"),
    path('Ofertas/', Ofertas, name="Ofertas"),
    path('Productos/', Productos, name="Productos"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro-user/', registro_user, name="registro_user"),
    path('api/', include(router.urls)),
]
