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

    #bodegas
    path('bodegas', views.BodegaList.as_view(), name='lista_bodegas'),
    path('bodegas/ver/<int:pk>', views.BodegaDetail.as_view(), name='detalle_bodega'),
    path('bodegas/crear', views.BodegaCreate.as_view(), name='crear_bodega'),
    path('bodegas/modificar/<int:pk>', views.BodegaUpdate.as_view(), name='modificar_bodega'),
    path('bodegas/eliminar/<int:pk>', views.BodegaDelete.as_view(), name='eliminar_bodega'),

    #categorias
    path('categorias', views.CategoriaList.as_view(), name='lista_categorias'),
    path('categorias/ver/<int:pk>', views.CategoriaDetail.as_view(), name='detalle_categoria'),
    path('categorias/crear', views.CategoriaCreate.as_view(), name='crear_categoria'),
    path('categorias/modificar/<int:pk>', views.CategoriaUpdate.as_view(), name='modificar_categoria'),
    path('categorias/eliminar/<int:pk>', views.CategoriaDelete.as_view(), name='eliminar_categoria'),

    #clientes
    path('clientes', views.ClienteList.as_view(), name='lista_clientes'),
    path('cliente/crear', views.ClienteCreate.as_view(), name='crear_cliente'),
    path('cliente/modificar/<int:pk>', views.ClienteUpdate.as_view(), name='modificar_cliente'),
    path('cliente/eliminar/<int:pk>', views.ClienteDelete.as_view(), name='eliminar_cliente'),

    #ventas
    path('ventas', views.VentasList.as_view(), name='lista_ventas'),
    path('venta/crear', views.VentaCreate, name='crear_venta'),
    path('venta/ver/<int:pk>', views.ClienteUpdate.as_view(), name='ver_venta'),
    

    #Otros URLS de vistas   


]

