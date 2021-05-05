from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Follower

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):

    if request.method == 'POST':

        try:
            nombre, email = request.POST['name'], request.POST['email']
            new_follower = Follower(nombre=nombre, mail=email)
            new_follower.save()

            emailhost = settings.EMAIL_HOST_USER

            asunto = 'Bienvenido a tu DataScience'
            mensaje = 'Gracias por tu interés en la comunidad.\nEste correo tiene la unica finalidad de confirmar tu suscripción a nuestro blog.'

            send_mail(asunto, mensaje, emailhost, [email])

        except:
            pass

    return render(request, 'mysite/home.html')