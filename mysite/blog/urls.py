from django.contrib import admin
from django.urls import path
from blog.views import blog, entrada, autor, categoria

urlpatterns = [
    path('', blog, name = 'blog'),
    path('<int:entrada_id>', entrada, name='entrada'),
    path('auth/<int:autor_id>', autor, name='autor'),
    path('cat/<int:categoria_id>', categoria, name='categoria'),

]