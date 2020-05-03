from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import *

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.conf import settings

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.forms import ModelForm

from io import BytesIO
from django.template.loader import get_template
from django_xhtml2pdf.views import PdfMixin


from django.urls import reverse
from django import forms

import json
from django.core.serializers.json import DjangoJSONEncoder
import decimal


# CRUD de los usuarios


class UsuarioModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioModelForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }

    class Meta:
        model = Usuario
        fields = ['dpi', 'nombre', 'fecha_nacimiento', 'email', 'password']


class UsuarioCreate(CreateView):
    form_class = UsuarioModelForm
    model = Usuario

    # Redirigir registro al start
    def get_success_url(self):
        return reverse('profile')

# ver el perfil de usuario en el que esta actualmente autenticado el usuario


class UsuarioDetail(LoginRequiredMixin, DetailView):
    model = Usuario

    # en vez de utilizar la llave primaria enviada por default a esta vista,
    # se utiliza el usuario en el request
    def get_object(self, queryset=None):
        dpi = self.kwargs.get('pk')
        if dpi:
            return get_object_or_404(Usuario, dpi=dpi)
        return self.request.user

# modificar el perfil de usuario en el que esta actualmente autenticado el usuario


class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['dpi', 'fecha_nacimiento']

    # en vez de utilizar la llave primaria enviada por default a esta vista,
    # se utiliza el usuario en el request
    def get_object(self, queryset=None):
        return self.request.user

    # Redirigir al usuario a su perfil
    def get_success_url(self):
        return '/'

# CRUD del modelo SEDES
# Accesible para todos los usuarios autenticados

# Esta clase sirve para asignarle una clase CSS a cada uno de los campos en un form


class SedeModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SedeModelForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }

    class Meta:
        model = Sede
        fields = '__all__'

# Ver todas las sedes disponibles


class SedeList(LoginRequiredMixin, ListView):
    model = Sede

# Ver una sede en especifico


class SedeDetail(DetailView):
    model = Sede

# Crear sedes (esta funcion es unicamente para encargados de sede)


class SedeCreate(CreateView):
    form_class = SedeModelForm
    model = Sede

    # Redirigir al usuario a su perfil
    def get_success_url(self):
        return reverse('lista_sedes')

# Modificar sedes (esta funcion es unicamente para encargados de sede)


class SedeUpdate(UpdateView):
    model = Sede
    form_class = SedeModelForm

    # Redirigir al usuario a su perfil
    def get_success_url(self):
        return reverse('lista_sedes')

# Eliminar una sede (esta funcion es unicamente para encargados de sede)


class SedeDelete(DeleteView):
    model = Sede

    # Redirigir al usuario a su perfil
    def get_success_url(self):
        return reverse('lista_sedes')

# Vista Productos


class ProductoModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductoModelForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }

        self.fields['precio'].widget.attrs = {
            'step': 'any',
            'class': 'form-control'
        }

    class Meta:
        model = Producto
        fields = '__all__'

# Ver todas los productos disponibles


class ProductoList(ListView):
    model = Producto
    template_name = 'productos/producto_list.html'

# Ver un producto en especifico


class ProductoDetail(DetailView):
    model = Producto
    template_name = 'productos/producto_detail.html'

# Crear Producto


class ProductoCreate(CreateView):
    form_class = ProductoModelForm
    model = Producto
    template_name = 'productos/producto_form.html'

    # Redirigir al listado de productos
    def get_success_url(self):
        return reverse('lista_productos')

# Modificar Producto


class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoModelForm
    template_name = 'productos/producto_form.html'

    # Redirigir al listado de productos
    def get_success_url(self):
        return reverse('lista_productos')

# Eliminar un producto


class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'productos/producto_confirm_delete.html'

    # Redirigir al listado de productos
    def get_success_url(self):
        return reverse('lista_productos')

# Vista Bodegas


class BodegaModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(BodegaModelForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }

    class Meta:
        model = Bodega
        fields = '__all__'

# Ver todas los Bodegas disponibles


class BodegaList(ListView):
    model = Bodega
    template_name = 'bodegas/bodegas_list.html'

# Ver un Bodega en especifico


class BodegaDetail(DetailView):
    model = Bodega
    template_name = 'bodegas/bodegas_detail.html'

# Crear Bodega


class BodegaCreate(CreateView):
    form_class = BodegaModelForm
    model = Bodega
    template_name = 'bodegas/bodegas_form.html'

    # Redirigir al listado de Bodegas
    def get_success_url(self):
        return reverse('lista_bodegas')

# Modificar Bodega


class BodegaUpdate(UpdateView):
    model = Bodega
    form_class = BodegaModelForm
    template_name = 'bodegas/bodegas_form.html'

    # Redirigir al listado de Bodegas
    def get_success_url(self):
        return reverse('lista_bodegas')

# Eliminar un Bodega


class BodegaDelete(DeleteView):
    model = Bodega
    template_name = 'bodegas/bodegas_confirm_delete.html'

    # Redirigir al listado de Bodegas
    def get_success_url(self):
        return reverse('lista_bodegas')

# Vista Categorias


class CategoriasModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CategoriasModelForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }

    class Meta:
        model = Categoria
        fields = '__all__'

# Ver todas los Categorias disponibles


class CategoriaList(ListView):
    model = Categoria
    template_name = 'categorias/categorias_list.html'


# Ver un Categoria en especifico
class CategoriaDetail(DetailView):
    model = Categoria
    template_name = 'categorias/categorias_detail.html'

# Crear Categoria


class CategoriaCreate(CreateView):
    form_class = CategoriasModelForm
    model = Categoria
    template_name = 'categorias/categorias_form.html'

    # Redirigir al listado de Categoria
    def get_success_url(self):
        return reverse('lista_categorias')

# Eliminar una categoria


class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'categorias/categorias_confirm_delete.html'

    # Redirigir al listado de Bodegas
    def get_success_url(self):
        return reverse('lista_categorias')

# Modificar Categoria


class CategoriaUpdate(UpdateView):
    model = Categoria
    form_class = CategoriasModelForm
    template_name = 'categorias/categorias_form.html'

    # Redirigir al listado de Bodegas
    def get_success_url(self):
        return reverse('lista_categorias')

# Clientes
# Accesible por usuarios de ventas


class ClientesModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClientesModelForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }

    class Meta:
        model = Cliente
        fields = '__all__'

# Ver todas los Categorias disponibles


class ClienteList(ListView):
    model = Cliente
    template_name = 'clientes/clientes_list.html'

# Crear cliente


class ClienteCreate(CreateView):
    form_class = ClientesModelForm
    model = Cliente
    template_name = 'clientes/clientes_form.html'

    # Redirigir al listado de clientes
    def get_success_url(self):
        return reverse('lista_clientes')

# Eliminar un cliente


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'clientes/clientes_confirm_delete.html'

    # Redirigir al listado de clientes
    def get_success_url(self):
        return reverse('lista_clientes')

# Modificar cliente


class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClientesModelForm
    template_name = 'clientes/clientes_form.html'

    # Redirigir al listado de productos
    def get_success_url(self):
        return reverse('lista_clientes')


# VENTAS

# Lista de ventas

class VentasModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(VentasModelForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }

        self.fields['fecha_facturacion'].input_formats = ['%d/%m/%Y']

    class Meta:
        model = Venta
        fields = '__all__'

# Ver todas los Categorias disponibles


class VentasList(ListView):
    model = Venta
    template_name = 'ventas/ventas_list.html'

# ver una unica venta

class VentaDetail(DetailView):
    model = Venta
    template_name = 'ventas/venta_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        venta = context['venta']
        factura = []
        print(venta.productoventa_set)

        producto_ventas = ProductoVenta.objects.filter(venta= venta)

        total_actual = 0
        for pv in producto_ventas:
            reglon_factura = {}
            reglon_factura['producto'] = pv.producto
            reglon_factura['cantidad'] = pv.cantidad
            reglon_factura['subtotal'] = round(pv.cantidad * pv.producto.precio, 2)
            total_actual += reglon_factura['subtotal']
            reglon_factura['total'] = total_actual

            factura.append(reglon_factura)

        context['factura'] = factura
        context['total'] = total_actual
        context['total_10p'] = round(decimal.Decimal(total_actual) * decimal.Decimal(0.1), 2)

        context['total_recargo'] = round(decimal.Decimal(total_actual) * decimal.Decimal(1.1), 2)

        return context

class PDFVentaDetail(PdfMixin, DetailView):
    model = Venta
    template_name = 'ventas/venta_pdf.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        venta = context['venta']
        factura = []
        print(venta.productoventa_set)

        producto_ventas = ProductoVenta.objects.filter(venta= venta)

        total_actual = 0
        for pv in producto_ventas:
            reglon_factura = {}
            reglon_factura['producto'] = pv.producto
            reglon_factura['cantidad'] = pv.cantidad
            reglon_factura['subtotal'] = round(pv.cantidad * pv.producto.precio, 2)
            total_actual += reglon_factura['subtotal']
            reglon_factura['total'] = total_actual

            factura.append(reglon_factura)

        context['factura'] = factura
        context['total'] = total_actual
        context['total_10p'] = round(decimal.Decimal(total_actual) * decimal.Decimal(0.1), 2)

        context['total_recargo'] = round(decimal.Decimal(total_actual) * decimal.Decimal(1.1), 2)

        return context


# Crear venta


def VentaCreate(request):
    if (request.method == 'GET'):
        
        bodegas = Bodega.objects.all()
        bodega_productos = []
        pindex = 1
        for bodega in bodegas:
            productos = []
            for bps in bodega.bodegaproducto_set.all():
                productos.append({'id': bps.producto.id, 'index': pindex, 'nombre': bps.producto.nombre, 'cantidad': bps.cantidad })
                pindex = pindex + 1

            bodega = {
                'productos': productos,
                'nombre': bodega.nombre,
                'id': bodega.id,
                'activada': bodega.activada 
            }

            bodega_productos.append(bodega)
        
        context = {
            'clientes': Cliente.objects.all(),
            'productos': Producto.objects.all(),
            'repartidores': Usuario.objects.filter(groups__name='Repartidor'),
            'bodegas': bodegas,
            'bodega_productos': json.dumps(list(bodega_productos), cls=DjangoJSONEncoder),
        }

        return render(request, 'ventas/venta_form.html', context)
    
    elif (request.method == 'POST'):

        cliente_id = request.POST.get('cliente')
        cliente = get_object_or_404(Cliente, dpi= cliente_id)

        vendedor = request.user

        fecha_facturacion = request.POST.get('fecha_facturacion')
        
        productos_agregados = dict(request.POST)["productos_agregados"]

        tipo = request.POST.get('tipo')
        a_domicilio = tipo == 'D'

        repartidor_id = request.POST.get('repartidor') if a_domicilio else None
        repartidor = get_object_or_404(Usuario, email= repartidor_id) if repartidor_id else None
        
        fecha_entrega = fecha_facturacion if not a_domicilio else None 

        venta = Venta(
            cliente=cliente,
            vendedor=vendedor,
            fecha_facturacion=fecha_facturacion,
            tipo= tipo,
            entregada= not a_domicilio, #si el tipo es local, sera verdadero, de lo contrario, falso,
            repartidor= repartidor,
            fecha_entrega= fecha_entrega,
        )

        venta.save()

        for producto in productos_agregados:
            data = producto.split('#_v_#')
            
            id_producto = data[0]
            id_bodega = data[2]

            producto = get_object_or_404(Producto, id= id_producto)
            bodega = get_object_or_404(Bodega, id= id_bodega)

            prod_bodega = get_object_or_404(BodegaProducto, producto= producto, bodega= bodega)

            cantidad = int(data[1])
            cantidad = cantidad if cantidad > 0 and cantidad <= prod_bodega.cantidad else 0

            prod_bodega.cantidad = prod_bodega.cantidad - cantidad
            prod_bodega.save()
            if (cantidad != 0):
                prodventa  = ProductoVenta(venta= venta, producto= producto, cantidad = cantidad)
                prodventa.save()

        return HttpResponseRedirect(reverse('lista_ventas'))

# Inventario

class InventarioModelForm(ModelForm):
    descripcion = forms.CharField(max_length= 500, required= True)

    def __init__(self, *args, **kwargs):
        super(InventarioModelForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }

    class Meta:
        model = BodegaProducto
        fields = ['cantidad']

# Modificar inventario

class InventarioUpdate(UpdateView):
    model = BodegaProducto
    form_class = InventarioModelForm
    template_name = 'inventario/inventario_form.html'

    def form_valid(self, form):
        
        bp = self.object
        descripcion = form.cleaned_data['descripcion']
        cvieja = form.initial['cantidad']

        log_inv = LogActualizacionInventario(
            producto= bp.producto,
            cantidad_nueva= float(form.cleaned_data['cantidad']),
            cantidad_vieja= cvieja,
            descripcion= descripcion,
            usuario= self.request.user,
        )

        log_inv.save()

        return super().form_valid(form)

    # Redirigir al listado de productos
    def get_success_url(self):
        return reverse('detalle_bodega', args=[self.object.bodega.id])


# REPORTES
def reporte_ventas(request):
    context= {}

    ventas = []

    for venta_bd in Venta.objects.all():
        total = 0
        for pv in venta_bd.productoventa_set.all():
            total += pv.producto.precio * pv.cantidad
            
        venta = { 
            "id": venta_bd.id,
            'vendedor': venta_bd.vendedor.dpi,
            'total': total
        }

        ventas.append(venta)

    repartidores = []

    for repartidor in Usuario.objects.filter(groups__name='Repartidor'):
        repartidores.append({
            "nombre": repartidor.nombre,
            "dpi": repartidor.dpi
        })

    context['ventas'] = json.dumps(list(ventas), cls=DjangoJSONEncoder),
    context["vendedores"] = json.dumps(list(repartidores), cls=DjangoJSONEncoder);

    return render(request, 'reportes/reporte_venta.html', context)
