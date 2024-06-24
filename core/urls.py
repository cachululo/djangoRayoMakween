from django.urls import path
from .views import agregar_producto, eliminar_producto, home, limpiar_carrito, productos, exit,register, restar_producto, tienda

urlpatterns = [
    path('', home, name='home'),
    path('productos/', productos, name='productos'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
    path('tienda/', tienda, name='tienda'),
    path('agregar/<int:producto_id>/', agregar_producto,name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto,name="Del"),
    path('restar/<int:producto_id>/', restar_producto,name="Sub"),
    path('limpiar/', limpiar_carrito,name="CLS"),
]