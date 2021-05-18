from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre

class Region(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        unique_together = ('nombre', 'pais',)

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        unique_together = ('nombre', 'region',)

class Municipio(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        unique_together = ('nombre', 'ciudad',)

class Calle(models.Model):
    nombre = models.CharField(max_length=50)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        unique_together = ('nombre', 'municipio',)

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank = True)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50, blank = True)

    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=10)

    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)    
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)    
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)    
    calle = models.ForeignKey(Calle, on_delete=models.CASCADE)    
    CP = models.CharField(max_length=5)   
    numero = models.CharField(max_length=15)

    referencias = models.TextField()  

    def __str__(self):
        return self.nombre + ' ' + self.apellido1

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    carro = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=False)
    enviado = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return self.cliente.nombre + ' ' + self.cliente.apellido1 + ' ' + str(self.creado)
