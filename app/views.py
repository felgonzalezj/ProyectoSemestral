from app.forms import ProductoForm
from app.models import Producto
from django.http import request
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.http import Http404

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
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(ProductosAll, 4)
        ProductosAll = paginator.page(page)
    except:
        raise Http404

    datos = {
        'listasProductos' :  ProductosAll,
        'paginator' : paginator
    }
    return render(request, 'app/Productos.html', datos)


def agregar_producto(request):
    datos = {
        'form' :  ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
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
        formulario = ProductoForm(data=request.POST,instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto modificado correctamente"
            datos['form'] = formulario
    return render(request, 'app/modificar_productos.html', datos)


def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to="Productos")