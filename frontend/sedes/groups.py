from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Usuario

"""
Funcion para asignar los permisos de cada grupo de los usuarios

Esta funcion se llama con la consola de comandos utilizando los siguientes comandos

En el directorio /frontend
$ python manage.py shell

Luego, dentro de la consola de comandos de python

>>> from sedes.groups import load_groups
>>> load_groups()

Si todo salio bien, se mostrara un mensaje, de lo contrario, se mostrara un traceback
"""
def load_groups():
    
    print("Creando u obteniendo roles del usuario")
    
    vendedor_group, created = Group.objects.get_or_create(name ='Vendedor')
    bodeguero_group, created2 = Group.objects.get_or_create(name ='Bodeguero')
    repartidor_group, created3 = Group.objects.get_or_create(name ='Repartidor')
    encargado_bodega_group, created4 = Group.objects.get_or_create(name ='Encargado Bodega')
    encargado_sede_group, created5 = Group.objects.get_or_create(name ='Encargado Sede')

    print("Agregando los permisos de cada rol")

    # Agregar permisos al grupo Vendedores
    # estos permisos estan creados en el archivo models.py en el modelo Usuario
    # en la clase "Meta" del usuario   
    vendedor_group.permissions.add(Permission.objects.get(codename ='registrar_cliente').id)
    vendedor_group.permissions.add(Permission.objects.get(codename ='registrar_venta').id)
    vendedor_group.permissions.add(Permission.objects.get(codename ='visualizar_reporte').id)

    bodeguero_group.permissions.add(Permission.objects.get(codename ='actualizar_inventario').id)
    bodeguero_group.permissions.add(Permission.objects.get(codename ='solicitar_transferencia').id)
    bodeguero_group.permissions.add(Permission.objects.get(codename ='ordenes_transferencia_externa').id)
    bodeguero_group.permissions.add(Permission.objects.get(codename ='ordenes_transferencia_interna').id)

    repartidor_group.permissions.add(Permission.objects.get(codename ='ordenes_venta').id)
    repartidor_group.permissions.add(Permission.objects.get(codename ='ordenes_transferencia').id)

    print("Todos los permisos agregados a cada rol correctamente")