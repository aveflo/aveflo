from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def tienda(request):

    return render(request, 'tienda/tienda.html')