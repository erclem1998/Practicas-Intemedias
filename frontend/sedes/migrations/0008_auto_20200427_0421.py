# Generated by Django 3.0.5 on 2020-04-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sedes', '0007_auto_20200427_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='dpi',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]