# Generated by Django 3.0.5 on 2020-04-28 17:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sedes', '0013_auto_20200428_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoventa',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='productos',
            field=models.ManyToManyField(through='sedes.ProductoVenta', to='sedes.Producto'),
        ),
    ]
