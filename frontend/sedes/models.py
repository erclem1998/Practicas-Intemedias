from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

from .managers import CustomUserManager

# Create your models here.

class Sede(models.Model):
    alias = models.CharField(max_length= 200)
    direccion = models.CharField(max_length= 500)
    departamento = models.CharField(max_length= 50)
    municipio = models.CharField(max_length= 50)
    encargado = models.ForeignKey('Usuario', on_delete= models.CASCADE)
    numero_bodegas = models.IntegerField(default= 0)

    def __str__(self):
        return self.alias

class Usuario(AbstractBaseUser, PermissionsMixin):
    dpi = models.BigIntegerField(
        unique= True, 
        validators=[
            MaxValueValidator(9999999999999),
         
            MinValueValidator(100000000000)
        ]
    )

    nombre = models.CharField(max_length= 100)
    fecha_nacimiento = models.DateField('Fecha Nacimiento')
    email = models.EmailField(_('Correo Electronico'), primary_key= True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default= timezone.now)
        
    #groups = models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='usuario_set', related_query_name='user', to='auth.Group', verbose_name='groups')
    #user_permissions = models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='usuario_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')
            
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['dpi', 'fecha_nacimiento']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class Rol(models.Model):
    VENDEDOR = 'VE'
    BODEGUERO = 'BO'
    REPARTIDOR = 'RE'
    ENCARGADO = 'EN'
    
    ROL_CHOICES = [
        (VENDEDOR, 'Vendedor'),
        (BODEGUERO, 'Bodeguero'),
        (REPARTIDOR, 'Repartidor'),
        (ENCARGADO, 'Encargado')
    ]

    descripcion = models.CharField(max_length= 2, choices= ROL_CHOICES, default= VENDEDOR)

class Bodega(models.Model):
    nombre = models.CharField(max_length= 50)
    direccion = models.CharField(max_length= 500)

    ACTIVA = 'A'
    INACTIVA = 'I'

    BODEGA_ESTADO_CHOICES = [
        (ACTIVA, 'Activa'),
        (INACTIVA, 'Inactiva')        
    ]

    estado = models.CharField(max_length= 1, choices= BODEGA_ESTADO_CHOICES, default= ACTIVA)
    encargado = models.ForeignKey('Usuario', on_delete= models.CASCADE)

class Producto(models.Model):    
    sku = models.CharField('SKU', max_length= 50, unique= True)
    codigo_barras = models.CharField('Codigo de Barras', max_length= 50)
    nombre = models.CharField(max_length= 50)
    descripcion = models.CharField(max_length= 500)
    precio = models.DecimalField(max_digits= 12, decimal_places= 2)
    categorias = models.ManyToManyField('Categoria')

class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()

class Categoria(models.Model):
    nombre = NameField('Nombre de categoria', unique= True, max_length= 25)

class Cliente(models.Model):
    dpi = models.CharField(max_length= 100, primary_key= True)
    nombre = models.CharField(max_length= 200)
    nit = models.CharField(max_length= 15)
    descripcion = models.CharField(max_length= 500)
    sedes = models.ManyToManyField('Sede')

class Venta(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete= models.CASCADE)
    vendedor = models.ForeignKey('Usuario', on_delete= models.CASCADE, related_name= 'vendedor')
    fecha_facturacion = models.DateField('Fecha de facturacion')
    
    DOMICILIO = 'D'
    LOCAL = 'L'
    VENTA_ESTADO_CHOICES = [
        (DOMICILIO, 'A domicilio'),
        (LOCAL, 'Local')        
    ]

    tipo = models.CharField(max_length= 1, choices= VENTA_ESTADO_CHOICES, default= LOCAL)
    repartidor = models.ForeignKey('Usuario', null= True, on_delete= models.SET_NULL, related_name= 'repartidor')
        
    fecha_entrega = models.DateField('Fecha de entrega', auto_now= True)
    entregada = models.BooleanField(default= False)

class ProductoVenta(models.Model):
    producto = models.ForeignKey('Producto', on_delete= models.CASCADE)
    venta = models.ForeignKey('Venta', null= True, on_delete= models.SET_NULL)
    cantidad = models.DecimalField('Cantidad', decimal_places= 2, max_digits= 12)

class Factura(models.Model):
    venta = models.ForeignKey('Venta', on_delete= models.SET_NULL, null= True)
    subtotal = models.DecimalField(decimal_places= 2, max_digits= 12)
    recargo = models.DecimalField(decimal_places= 2, max_digits= 5)
    total = models.DecimalField(decimal_places= 2, max_digits= 12)

class LogActualizacionInventario(models.Model):
    producto = models.ForeignKey('Producto', on_delete= models.SET_NULL, null= True)
    cantidad_nueva = models.DecimalField(decimal_places= 2, max_digits= 12)
    cantidad_vieja = models.DecimalField(decimal_places= 2, max_digits= 12)
    descripcion = models.CharField(max_length= 500)
    usuario = models.ForeignKey('Usuario', on_delete= models.SET_NULL, null= True)
    fecha = models.DateField('Fecha de cambio', auto_now_add= True)

    
    

