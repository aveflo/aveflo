from django.db import models
from django.contrib.auth.models import User
from markdown_deux import markdown

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, blank = True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='blog')
    instagram = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    resumen = models.CharField(max_length=150)
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Category)
    imagen = models.ImageField(upload_to='blog')
    contenido = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo
    
    def get_markdown(self):
        content = self.contenido
        return markdown(content)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, blank = True) 
    contenido = models.CharField(max_length=200, blank = True)

class Follower(models.Model):
    nombre = models.CharField(max_length=50, blank = True) 
    mail = models.EmailField(unique=True)

    def __str__(self):
        return self.mail