# Generated by Django 3.0.5 on 2020-04-14 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('dpi', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha Nacimiento')),
                ('correo', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('alias', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=500)),
                ('departamento', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50)),
                ('encargado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedes.Usuario')),
            ],
        ),
    ]
