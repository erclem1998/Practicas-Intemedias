from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import *

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.forms import ModelForm

from django.urls import reverse

# CRUD de los usuarios

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

# Ver todas las sedes disponibles


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
