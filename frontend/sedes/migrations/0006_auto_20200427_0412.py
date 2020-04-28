# Generated by Django 3.0.5 on 2020-04-27 10:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sedes', '0005_auto_20200427_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='id',
            field=models.AutoField(auto_created=True, default=1111111111111, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='dpi',
            field=models.BigIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(9999999999999), django.core.validators.MinValueValidator(100000000000)]),
        ),
    ]