from django.urls import path

from . import views

urlpatterns = [
    #usuarios
    path('', views.UsuarioDetail.as_view(template_name= 'usuarios/usuario_detail.html'), name= 'profile'),
    path('usuario/modificar', views.UsuarioUpdate.as_view(template_name= 'usuarios/usuario_form.html'), name= 'modificar_usuario'),
    path('usuario/<int:pk>', views.UsuarioDetail.as_view(template_name= 'usuarios/usuario_detail.html'), name= 'ver_usuario'),
    
    #sedes
    path('sedes', views.SedeList.as_view(), name='lista_sedes'),
    path('sedes/ver/<int:pk>', views.SedeDetail.as_view(), name='detalle_sede'),
    path('sedes/crear', views.SedeCreate.as_view(), name='crear_sede'),
    path('sedes/modificar/<int:pk>', views.SedeUpdate.as_view(), name='modificar_sede'),
    path('sedes/eliminar/<int:pk>', views.SedeDelete.as_view(), name='eliminar_sede'),

    #Otros URLS de vistas   
]

