from django.urls import path

from . import views

urlpatterns = [
    #usuarios
    path('', views.UsuarioDetail.as_view(template_name= 'usuarios/usuario_detail.html'), name= 'profile'),
    path('usuario/modificar', views.UsuarioUpdate.as_view(template_name= 'usuarios/usuario_form.html'), name= 'modificar_usuario'),
    path('usuario/<int:pk>', views.UsuarioDetail.as_view(template_name= 'usuarios/usuario_detail.html'), name= 'ver_usuario'),
    path('usuario/crear', views.UsuarioCreate.as_view(template_name= 'usuarios/registro.html'), name= 'crear_usuario'),
    
    #sedes
    path('sedes', views.SedeList.as_view(), name='lista_sedes'),
    path('sedes/ver/<int:pk>', views.SedeDetail.as_view(), name='detalle_sede'),
    path('sedes/crear', views.SedeCreate.as_view(), name='crear_sede'),
    path('sedes/modificar/<int:pk>', views.SedeUpdate.as_view(), name='modificar_sede'),
    path('sedes/eliminar/<int:pk>', views.SedeDelete.as_view(), name='eliminar_sede'),

    #productos
    path('productos', views.ProductoList.as_view(), name='lista_productos'),
    path('productos/ver/<int:pk>', views.ProductoDetail.as_view(), name='detalle_producto'),
    path('productos/crear', views.ProductoCreate.as_view(), name='crear_producto'),
    path('productos/modificar/<int:pk>', views.ProductoUpdate.as_view(), name='modificar_producto'),
    path('productos/eliminar/<int:pk>', views.ProductoDelete.as_view(), name='eliminar_producto'),

    #Otros URLS de vistas   
]

