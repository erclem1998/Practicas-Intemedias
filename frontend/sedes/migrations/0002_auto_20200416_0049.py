# Generated by Django 3.0.5 on 2020-04-16 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sedes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'permissions': (('registrar_cliente', 'Para registrar clientes de una sede'), ('registrar_venta', 'Para registrar ventas de productos'), ('visualizar_reporte', 'Para visualizar reportes de ventas'), ('actualizar_inventario', 'Para modificar la cantidad de productos del inventario'), ('solicitar_transferencia', 'Para solicitar una transferencia de productos'), ('ordenes_transferencia_externa', 'Para revisar ordenes de transferencias entre sedes'), ('ordenes_transferencia_interna', 'Para revisar ordenes de transferencias entre bodegas'), ('ordenes_venta', 'Para modificar el estado de entregado de una orden de venta'), ('ordenes_transferencia', 'Para modificar el estado de entregado de una orden de transferencia'))},
        ),
    ]
