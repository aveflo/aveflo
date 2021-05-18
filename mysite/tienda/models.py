from django.db import models

# Create your models here.
class CatProducto(models.Model):
    nombre = models.CharField(max_length=50, blank = True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50, blank = True)
    descripcion = models.TextField()
    disponibilidad = models.IntegerField(default=0)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='tienda')
    categoria = models.ManyToManyField(CatProducto)
    
    def __str__(self):
        return self.nombre

