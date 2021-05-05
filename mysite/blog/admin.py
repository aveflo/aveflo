from django.contrib import admin
from .models import Author, Category, Post, Comment, Follower

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Follower)

