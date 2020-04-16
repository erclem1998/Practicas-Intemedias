from django.contrib import admin

from .models import Usuario
from .models import Sede
from .models import Bodega
from .models import Producto
from .models import Categoria
from .models import Cliente
from .models import Venta
from .models import ProductoVenta
from .models import Factura
from .models import LogActualizacionInventario

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Realizar un formulario de creacion y modificacion de usuario
# diferente al default
# esto debido que no estamos utilizando el modelo propuesto por django
# para guardar un usuario, sino que estamos utilizando
# un usuario creado como modelo, que extiende las capacidades del usuario base de django

# formulario de creacion inicial (este se muestra cuando se creara un nuevo usuario)
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmacion contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('dpi', 'email', 'fecha_nacimiento')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contrasenas ingresadas no coincidieron")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# formulario de modificacion de usuario (este se muestra cuando se edite la informacion de un usuario)
# para modificar un usuario se requerira 
class UserChangeForm(forms.ModelForm):

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmacion contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('nombre', 'email', 'password', 'dpi', 'fecha_nacimiento', 'is_active', 'is_admin')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if (not password1 or not password2):
            return None

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contrasenas ingresadas no coincidieron")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)

        pwd = self.cleaned_data["password1"]
        if (pwd):
            user.set_password()

        if commit:
            user.save()

        return user

# El nuevo formulario del usuario
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'dpi', 'nombre', 'fecha_nacimiento', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_superuser', 'is_active', 'is_staff')
    fieldsets = (
        ('Credenciales', {'fields': ('email', 'dpi', 'password1', 'password2')}),
        ('Informacion Personal', {'fields': ('nombre', 'fecha_nacimiento',)}),
        ('Tipo de Usuario', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
        ('Roles y permisos del Usuario', {'fields': ('groups', )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'dpi', 'fecha_nacimiento', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    def get_form(self, request, obj=None, change=False, **kwargs):
        kwargs['labels'] = {'groups': 'roles'}
        return super().get_form(request, obj=obj, change=change, **kwargs)


# Registrar modelos a mostrar en el admin

admin.site.register(Sede)
admin.site.register(Bodega)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(ProductoVenta)
admin.site.register(Factura)
admin.site.register(LogActualizacionInventario)
admin.site.register(Usuario, UserAdmin)
admin.site.register(Permission)