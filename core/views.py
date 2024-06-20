from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def productos(request):
    return render(request, 'core/productos.html')