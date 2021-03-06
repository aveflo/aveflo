# Generated by Django 3.2 on 2021-05-10 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0003_auto_20210509_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ciudad',
            name='pais',
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito.pais')),
            ],
        ),
        migrations.AddField(
            model_name='ciudad',
            name='region',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='carrito.region'),
            preserve_default=False,
        ),
    ]
