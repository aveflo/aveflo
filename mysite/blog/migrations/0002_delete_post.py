# Generated by Django 3.2 on 2021-05-03 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]