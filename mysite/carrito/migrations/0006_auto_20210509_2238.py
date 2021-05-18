# Generated by Django 3.2 on 2021-05-10 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0005_alter_pais_nombre'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='calle',
            unique_together={('nombre', 'municipio')},
        ),
        migrations.AlterUniqueTogether(
            name='ciudad',
            unique_together={('nombre', 'region')},
        ),
        migrations.AlterUniqueTogether(
            name='municipio',
            unique_together={('nombre', 'ciudad')},
        ),
        migrations.AlterUniqueTogether(
            name='region',
            unique_together={('nombre', 'pais')},
        ),
    ]