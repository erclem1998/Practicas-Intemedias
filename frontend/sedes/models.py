from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

from .managers import CustomUserManager
from .custom_fields import NameField

# Usuario del sistema, este se utiliza para la autenticacion y permisos
# ademas de poder acceder al sistema con el
# para crear el primer usuario se puede usar el comando en el directorio donde se encuentra el modelo
# $ python manage.py createsuperuser
# y seguir las instrucciones que presenta este script en la consola de comandos
class Usuario(AbstractBaseUser, PermissionsMixin):
    dpi = models.BigIntegerField(
        unique=True,
        validators=[
            MaxValueValidator(9999999999999),

            MinValueValidator(100000000000)
        ]
    )

    nombre = models.CharField(max_length=300)
    fecha_nacimiento = models.DateField('Fecha Nacimiento')
    email = models.EmailField(_('Correo Electronico'), primary_key=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['dpi', 'fecha_nacimiento']

    objects = CustomUserManager()

    def __str__(self):
        return "%s (%s)" % (self.dpi, self.email)

    # Permisos asociados a un usuario
    # sirve para realizar toda la gestion de control de ORM
    class Meta:
        permissions = (("registrar_cliente", "Para registrar clientes de una sede"),
                   ("registrar_venta", "Para registrar ventas de productos"),
                   ("visualizar_reporte", "Para visualizar reportes de ventas"),
                   ("actualizar_inventario", "Para modificar la cantidad de productos del inventario"),
                   ("solicitar_transferencia", "Para solicitar una transferencia de productos"),
                   ("ordenes_transferencia_externa", "Para revisar ordenes de transferencias entre sedes"),
                   ("ordenes_transferencia_interna", "Para revisar ordenes de transferencias entre bodegas"),
                   ("ordenes_venta", "Para modificar el estado de entregado de una orden de venta"),
                   ("ordenes_transferencia", "Para modificar el estado de entregado de una orden de transferencia"))

# Sedes que contienen bodegas este es el modelo principal de la app
class Sede(models.Model):
    alias = models.CharField(max_length=200)
    direccion = models.CharField(max_length=500)
    departamento = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    encargado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    numero_bodegas = models.IntegerField(default=0)

    def __str__(self):
        return "%s [%s]" % (self.alias, self.encargado)


# Este modelo presenta una bodega perteneciente a una sede
# en esta se pueden encontrar productos relacionados a ella
class Bodega(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=500)
    activada = models.BooleanField(default= True)
    encargado = models.ForeignKey('Usuario', on_delete=models.CASCADE)

# Este modelo indica un producto dentro de una bodega
# es una especie de control de inventario
class Producto(models.Model):
    sku = models.CharField('SKU', max_length=50, unique=True)
    codigo_barras = models.CharField('Codigo de Barras', max_length=50)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    categorias = models.ManyToManyField('Categoria')

# Categoria de un producto
# este tiene una relacion de muchos a muchos asimetrica con el modelo Producto
class Categoria(models.Model):
    nombre = NameField('Nombre de categoria', unique=True, max_length=25)

# Venta de un producto, realizada por un usuario vendedor
class Venta(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    vendedor = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='vendedor')

    fecha_facturacion = models.DateField('Fecha de facturacion')

    DOMICILIO = 'D'
    LOCAL = 'L'
    VENTA_ESTADO_CHOICES = [
        (DOMICILIO, 'A domicilio'),
        (LOCAL, 'Local')
    ]

    tipo = models.CharField(
        max_length=1, choices=VENTA_ESTADO_CHOICES, default=LOCAL)
    repartidor = models.ForeignKey(
        'Usuario', null=True, on_delete=models.SET_NULL, related_name='repartidor')

    fecha_entrega = models.DateField('Fecha de entrega', auto_now=True)
    entregada = models.BooleanField(default=False)


# Cliente de una venta
class Cliente(models.Model):
    dpi = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=200)
    nit = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=500)
    sedes = models.ManyToManyField('Sede')

# En este se asocia un producto con una venta
# sirve para tomar en cuenta cuanto producto descontar del inventario
# y calcular el total de la factura
class ProductoVenta(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    venta = models.ForeignKey('Venta', null=True, on_delete=models.SET_NULL)
    cantidad = models.DecimalField('Cantidad', decimal_places=2, max_digits=12)

# Factura de una venta, contiene el total de la venta junto si esta fue
# a domicilio se recarga 10% del subtotal
class Factura(models.Model):
    venta = models.ForeignKey('Venta', on_delete=models.SET_NULL, null=True)
    subtotal = models.DecimalField(decimal_places=2, max_digits=12)
    recargo = models.DecimalField(decimal_places=2, max_digits=5)
    total = models.DecimalField(decimal_places=2, max_digits=12)

# Estos logs sirven para revisar la actualizacion del inventario por parte
# del usuario encargado de sede
class LogActualizacionInventario(models.Model):
    producto = models.ForeignKey(
        'Producto', on_delete=models.SET_NULL, null=True)
    cantidad_nueva = models.DecimalField(decimal_places=2, max_digits=12)
    cantidad_vieja = models.DecimalField(decimal_places=2, max_digits=12)
    descripcion = models.CharField(max_length=500)
    usuario = models.ForeignKey(
        'Usuario', on_delete=models.SET_NULL, null=True)
    fecha = models.DateField('Fecha de cambio', auto_now_add=True)
