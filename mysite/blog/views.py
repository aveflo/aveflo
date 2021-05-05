from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post, Category, Author, Comment
from django.contrib.auth.models import User

# Create your views here.
def blog(request):
    
    categoria = Category.objects.all()
    post = Post.objects.all()

    return render(request, 'blog/blog.html', {'post': post, 'categorias':categoria})

def entrada(request, entrada_id):
    
    if request.method == 'POST':

        comentario = Comment(post = Post.objects.get(id = entrada_id),
        nombre = request.POST['nombre'], 
        contenido = request.POST['comentario'])
        comentario.save()

    entrada = Post.objects.get(id=entrada_id)
    autor = Author.objects.get(user = User.objects.get(id = entrada.autor.id))
    comment = Comment.objects.filter(post = Post.objects.get(id = entrada_id))

    return render(request, 'blog/entrada.html', {'entrada': entrada, 'autor': autor, 'comment':comment})

def autor(request, autor_id):

    autor = Author.objects.get(user = User.objects.get(id = autor_id))

    return render(request, 'blog/autor.html', {'autor': autor})

def categoria(request, categoria_id):
    
    categoria = Category.objects.get(id=categoria_id)
    post = Post.objects.filter(categoria=categoria)

    return render(request, 'blog/categoria.html', {'post': post, 'categoria':categoria})