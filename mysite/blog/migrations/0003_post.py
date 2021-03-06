# Generated by Django 3.2 on 2021-05-03 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('resumen', models.CharField(max_length=150)),
                ('imagen', models.ImageField(upload_to='')),
                ('contenido', models.TextField(blank=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('comentarios', models.CharField(blank=True, max_length=200)),
                ('autor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
                ('categoria', models.ManyToManyField(to='blog.Category')),
            ],
        ),
    ]
