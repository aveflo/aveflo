from django.contrib import admin
from django.urls import path
from carrito.views import agregar_producto, agregar_producto_carrito, eliminar_producto, eliminar_producto_carrito, restar_producto, restar_producto_carrito, limpiar_carro, carrito, pagar, datos, resumentotal

urlpatterns = [
    path('<int:producto_id>', agregar_producto, name='agregar_producto'),
    path('vaciar_carrito', limpiar_carro, name='vaciar_carrito'),
    path('', carrito, name='carrito'),
    path('agregar/<int:producto_id>', agregar_producto_carrito, name='agregar_producto_carrito'),
    path('dejar/<int:producto_id>', restar_producto_carrito, name='dejar_producto_carrito'),
    path('eliminar/<int:producto_id>', eliminar_producto_carrito, name='eliminar_producto_carrito'),
    #path('pagar', pagar, name='pagar'),
    path('pagar', datos, name='datos'),
    path('resumentotal', resumentotal, name='resumen'),
]