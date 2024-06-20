from django.urls import path
from .views import home, productos, exit,register

urlpatterns = [
    path('', home, name='home'),
    path('productos/', productos, name='productos'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
]