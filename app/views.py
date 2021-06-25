from django.contrib.auth import authenticate, login
from app.forms import ProductoForm, UsuarioCreationForm
from app.models import Producto
from django.http import request
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import permission_required

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

@permission_required('app.view_producto')
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

@permission_required('app.add_producto')
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

@permission_required('app.change_producto')
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

@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to="Productos")

def registro_user(request):
    datos = {
        'form' :  UsuarioCreationForm()
    }

    if request.method == 'POST':
        formulario = UsuarioCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, usuario)
            return redirect(to="Home")
        datos['form'] = formulario

    return render(request, 'registration/singin.html', datos)