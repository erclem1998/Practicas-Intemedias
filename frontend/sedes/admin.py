from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Sede)
admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Bodega)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(ProductoVenta)
admin.site.register(Factura)
admin.site.register(LogActualizacionInventario)
