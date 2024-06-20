from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'core/home.html')

@login_required
def productos(request):
    return render(request, 'core/productos.html')