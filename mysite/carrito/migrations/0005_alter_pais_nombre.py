# Generated by Django 3.2 on 2021-05-10 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0004_auto_20210509_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]