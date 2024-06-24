from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from core.Carrito import Carrito
from core.models import Producto
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'core/home.html')

@login_required
def productos(request):
    return render(request, 'core/productos.html')

def exit (request):
    logout(request)
    return redirect('home')

def register(request):
    data={
        'form':CustomUserCreationForm()
    }

    if request.method== 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        
        if user_creation_form.is_valid():
            user_creation_form.save()
            
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form']= user_creation_form

    return render (request, 'registration/register.html',data)

@login_required
def tienda(request):
    productoss= Producto.objects.all()
    return render(request, 'carrito/tienda.html', {'productoss':productoss})

def agregar_producto(request,producto_id):
    carrito= Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('Tienda')

def eliminar_producto (request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('Tienda')

def restar_producto (request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('Tienda')

def limpiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect('Tienda')