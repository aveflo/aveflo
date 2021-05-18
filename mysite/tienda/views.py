from django.http import HttpResponse
from django.shortcuts import render

from tienda.models import Producto, CatProducto

# Create your views here.
def tienda(request):

    producto = Producto.objects.all().filter(disponibilidad__gt=0)
    cat = CatProducto.objects.all()

    #return render(request, 'tienda/tienda.html', {'producto': producto, 'categoria':cat})
    return render(request, 'tienda/construccion.html')

def categoria(request, categoria_id):

    producto = Producto.objects.all().filter(disponibilidad__gt=0)
    producto = producto.filter(categoria = CatProducto(id = categoria_id))
    cat = CatProducto.objects.all()

    return render(request, 'tienda/tienda.html', {'producto': producto, 'categoria':cat})