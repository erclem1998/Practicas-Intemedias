from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import *

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

# CRUD de los usuarios
class UsuarioList(LoginRequiredMixin, ListView): 
    model = Usuario
    raise_exception = True  # Raise exception when no access instead of redirect
    permission_denied_message = "You are not allowed here."

class UsuarioDetail(DetailView): 
    model = Usuario

class UsuarioCreate(UserPassesTestMixin, CreateView): 
    model = Usuario
    fields = '__all__'

    def test_func(self):
        return self.request.user.is_superuser

class UsuarioUpdate(UpdateView): 
    model = Usuario
    fields = '__all__'
    
    def test_func(self):
        return self.request.user.is_superuser

class UsuarioDelete(DeleteView): 
    model = Usuario


# CRUD del modelo SEDES 
# Accesible para todos los usuarios autenticados 

class SedeList(LoginRequiredMixin, ListView): 
    model = Sede
    raise_exception = True  # Raise exception when no access instead of redirect
    permission_denied_message = "You are not allowed here."

class SedeDetail(DetailView): 
    model = Sede

class SedeCreate(UserPassesTestMixin, CreateView): 
    model = Sede
    fields = '__all__'

    def test_func(self):
        return self.request.user.is_superuser

class SedeUpdate(UpdateView): 
    model = Sede
    fields = '__all__'
    
    def test_func(self):
        return self.request.user.is_superuser

class SedeDelete(DeleteView): 
    model = Sede

"""
# Vista general de todas las sedes que hay
def index(request):
    sedes_list = Sede.objects.order_by('alias')
    template = loader.get_template('sedes/index.html')
    context = {
        'sedes_list': sedes_list,
    }

    return HttpResponse(template.render(context, request))
    
# Detalle de una sede en especifico
def detail(request, sedes_id):
    sede = get_object_or_404(Sede, pk= sedes_id)
    return render(request, 'sedes/detail.html', {'sede': sede})

# Agregar una sede
def bodegas(request):
    return render('')

    """

