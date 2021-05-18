import re
from .carro import Carro
from .in_cdmx import within_cdmx

from geopy.geocoders import Nominatim

def importe_total_carro(request):

    Carro(request)

    total = 0

    #if request.user.is_authenticated:

    for key in request.session['carro'].keys():

        value = request.session['carro'][key]


        total = total + float(value['precio'])*float(value['cantidad'])


    return {'importe_total_carro': total}


def costo_de_envio(request):

    try:

        calle = request.POST['calle']
        numero = request.POST['numero']
        cp = request.POST['CP']
        municipio = request.POST['municipio']
        ciudad = request.POST['ciudad'].lower()
        region = request.POST['region'].lower()
        pais = request.POST['pais'].lower()

        geolocator = Nominatim(user_agent="me")

        dirn = {'street':calle, 
            'city':ciudad, 
            'state':region, 
            'country':pais, 
            'postalcode':cp
            }
        
        location = geolocator.geocode(dirn)
        coords = (location.longitude, location.latitude)

        precio = importe_total_carro(request)
        precio = float(precio['importe_total_carro'])

        envio = 0

        if precio <= 300:
            if within_cdmx(coords):
                envio = 50

            else:
                envio = 200

        elif 300 < precio <= 600:
            if within_cdmx(coords):
                envio = 0

            else:
                envio = 200
        

        return {'costo_de_envio':envio}

    except:

        return {'costo_de_envio':200}

def costo_total(request):
    total = importe_total_carro(request)['importe_total_carro'] + costo_de_envio(request)['costo_de_envio']
    return {'costo_total':total}