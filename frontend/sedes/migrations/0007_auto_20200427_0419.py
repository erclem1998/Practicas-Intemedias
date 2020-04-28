# Generated by Django 3.0.5 on 2020-04-27 10:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sedes', '0006_auto_20200427_0412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='id',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='dpi',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MaxValueValidator(9999999999999), django.core.validators.MinValueValidator(100000000000)]),
        ),
    ]
