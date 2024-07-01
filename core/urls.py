from django.urls import path
from .views import agregar_producto, eliminar_producto, home, limpiar_carrito, lista_user, productos, exit, register, restar_producto, tienda, edit_user, delete_user

urlpatterns = [
    path('', home, name='home'),
    path('productos/', productos, name='productos'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
    path('tienda/', tienda, name='tienda'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('users/', lista_user, name='lista_user'),
    path('users/edit/<int:user_id>/', edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),
]
