# Generated by Django 2.2.24 on 2022-10-17 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
        migrations.AlterModelTable(
            name='productoption',
            table='products_options',
        ),
        migrations.AlterModelTable(
            name='tag',
            table='tags',
        ),
    ]