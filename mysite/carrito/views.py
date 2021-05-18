from django.shortcuts import render
from .carro import Carro
from tienda.models import Producto
from .models import *
from django.shortcuts import redirect


# Create your views here.
def agregar_producto(request, producto_id):
    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto)
    return redirect('tienda')

def agregar_producto_carrito(request, producto_id):
    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto)
    return redirect('carrito')

def eliminar_producto(request, producto_id):
    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto)
    return redirect('tienda')

def eliminar_producto_carrito(request, producto_id):
    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto)
    return redirect('carrito')

def restar_producto(request, producto_id):
    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)
    carro.restar(producto)
    return redirect('tienda')

def restar_producto_carrito(request, producto_id):
    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)
    carro.restar(producto)
    return redirect('carrito')

def limpiar_carro(request):
    carro = Carro(request)
    carro.vaciar()
    return redirect('tienda')

def limpiar_carro_carrito(request):
    carro = Carro(request)
    carro.vaciar()
    return redirect('carrito')

def carrito(request):
    carro = Carro(request).carro.values()
      
    return render(request, 'carrito/carrito.html', {'carro':carro})

def pagar(request):
    carro = Carro(request).carro.values()
      
    return render(request, 'carrito/pagar.html', {'carro':carro})

def resumentotal(request):
    carro = Carro(request).carro.values()
    observaiones = request.POST['observaciones']
    correo = request.POST['email']
    
    pais  = request.POST['pais'].lower()
    region = request.POST['region'].lower()
    ciudad = request.POST['ciudad'].lower()
    municipio = request.POST['municipio'].lower()
    CP = request.POST['CP'].lower()
    calle = request.POST['calle'].lower()
    numero = request.POST['numero'].lower()
    referencias = request.POST['referencias'].lower()

    nombre = request.POST['nombre'].lower()
    nombre2 = request.POST['nombre2'].lower()
    apellido1 = request.POST['apellido1'].lower()
    apellido2 = request.POST['apellido2'].lower()
    telefono = request.POST['telefono'].lower()
        
    try:
        PAIS = Pais(nombre = pais).save()
        PAIS.save()
    except:
        pass

    id_pais = Pais.objects.only('id').get(nombre = pais).id

    try:
        REGION = Region(nombre = region, pais = Pais.objects.get(id = id_pais))
        REGION.save()
    except:
        pass

    id_region = Region.objects.only('id').get(nombre = region, pais = Pais.objects.get(id = id_pais)).id

    try:
        CIUDAD = Ciudad(nombre = ciudad, region = Region.objects.get(id = id_region))
        CIUDAD.save()
    except:
        pass

    id_ciudad = Ciudad.objects.only('id').get(nombre = ciudad, region = Region.objects.get(id = id_region)).id

    try:
        MUNICIPIO = Municipio(nombre = municipio, ciudad = Ciudad.objects.get(id = id_ciudad))
        MUNICIPIO.save()
    except:
        pass

    id_municipio = Municipio.objects.only('id').get(nombre = municipio, ciudad = Ciudad.objects.get(id = id_ciudad)).id

    try:
        CALLE = Calle(nombre = calle, municipio = Municipio.objects.get(id = id_municipio))
        CALLE.save()
    except:
        pass

    id_calle = Calle.objects.only('id').get(nombre = calle, municipio = Municipio.objects.get(id = id_municipio)).id

    CLIENTE = Cliente(nombre=nombre,
        pais=Pais.objects.get(id=id_pais), 
        ciudad=Ciudad.objects.get(id=id_ciudad),
        municipio=Municipio.objects.get(id=id_municipio),
        calle=Calle.objects.get(id=id_calle),
        numero=numero,
        segundo_nombre=nombre2,
        apellido1=apellido1,
        apellido2=apellido2,
        telefono=telefono,
        referencias=referencias,
        correo=correo)
    
    try:
        CLIENTE.save()
    except:
        pass

    #preparar resumen
    CLIENTE = Cliente.objects.get(correo=correo)

    context = {'carro':carro,
    'telefono': telefono,
    'correo':correo,
    'nombre': nombre,
    'nombre2': nombre2,
    'apellido1':apellido1,
    'apellido2':apellido2,
    'observaciones':observaiones,
    
    'referencias':referencias,
    'calle':calle,
    'numero':numero,
    'municipio':municipio,
    'CP':CP,
    'ciudad':ciudad,
    'region':region,
    'pais':pais}
    #falta calcular precio de envio


    return render(request, 'carrito/resumen.html', context)

def datos(request):
    carro = Carro(request).carro.values()

    return render(request, 'carrito/datos.html', {'carro':carro})