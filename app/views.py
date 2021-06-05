from app.forms import ProductoForm
from app.models import Producto
from django.http import request
from django.shortcuts import redirect, render

# Create your views here.

def Home(request):
    return render(request, 'app/Home.html')


def index(request):
    return render(request, 'app/index.html')


def Ofertas(request):
    OfertasAll = Producto.objects.all()
    datos = {
        'listaOfertas' : OfertasAll
    }
    return render(request, 'app/Ofertas.html', datos)


def Productos(request):
    ProductosAll = Producto.objects.all()
    datos = {
        'listasProductos' :  ProductosAll
    }
    return render(request, 'app/Productos.html', datos)


def agregar_producto(request):
    datos = {
        'form' :  ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto guardado correctamente"
    return render(request, 'app/agregar_productos.html', datos)


def modificar_producto(request,id):
    producto = Producto.objects.get(id=id)
    datos = {
        'form' :  ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto modificado correctamente"
            datos['form'] = formulario
    return render(request, 'app/modificar_productos.html', datos)


def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to="Productos")