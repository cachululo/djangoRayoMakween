from django.urls import path
from .views import home, productos

urlpatterns = [
    path('', home, name='home'),
    path('productos/', productos, name='productos'),
]