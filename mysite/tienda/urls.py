from django.contrib import admin
from django.urls import path
from tienda.views import tienda, categoria

urlpatterns = [
    path('', tienda, name = 'tienda'),
    path('<int:categoria_id>', categoria, name = 'tienda'),
    path('carrito/<int:categoria_id>', categoria, name='categoria'),
]