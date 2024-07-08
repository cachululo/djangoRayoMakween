from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from core.Carrito import Carrito 
from core.models import Producto
from .forms import CustomUserCreationForm, UserForm
import requests
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

def get_weather(api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Viña%20del%20Mar,cl&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    return round(temperature)

def base_context(request):
    api_key = settings.OPENWEATHERMAP_API_KEY
    temperature = get_weather(api_key)
    return {
        'temperature': temperature
    }

@login_required
def lista_user(request):
    if request.user.username == 'julian':  
        users = User.objects.all()
        return render(request, 'listar/lista_user.html', {'users': users, 'temperature': base_context(request)['temperature']})
    else:
        messages.error(request, 'No tienes permiso, ingresa con tu cuenta de administrador.')
        return redirect('home')

@login_required
def home(request):
    return render(request, 'core/home.html', {'temperature': base_context(request)['temperature']})

@login_required
def productos(request):
    productoss = Producto.objects.all()
    return render(request, 'core/productos.html', {'productoss': productoss, 'temperature': base_context(request)['temperature']})

@login_required
def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    data = {'form': CustomUserCreationForm()}
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form
    return render(request, 'registration/register.html', {'temperature': base_context(request)['temperature'], **data})

@login_required
def tienda(request):
    productoss = Producto.objects.all()
    return render(request, 'carrito/tienda.html', {'productoss': productoss, 'temperature': base_context(request)['temperature']})

@login_required
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('tienda')

@login_required
def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('tienda')

@login_required
def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('tienda')

@login_required
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('tienda')

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('lista_user')
    else:
        form = UserForm(instance=user)
    return render(request, 'listar/edit_user.html', {'form': form, 'temperature': base_context(request)['temperature']})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Usuario eliminado con éxito.')
        return redirect('lista_user')
    return render(request, 'listar/confirm_delete.html', {'user': user, 'temperature': base_context(request)['temperature']})
