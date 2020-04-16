from django.urls import path

from . import views

urlpatterns = [
    path('sedes', views.SedeList.as_view(), name='lista_sedes'),
    path('sedes/ver/<int:pk>', views.SedeDetail.as_view(), name='detalle_sede'),
    path('sedes/crear', views.SedeCreate.as_view(), name='crear_sede'),
    path('sedes/modificar/<int:pk>', views.SedeUpdate.as_view(), name='modificar_sede'),
    path('sedes/eliminar/<int:pk>', views.SedeDelete.as_view(), name='eliminar_sede'),
]

