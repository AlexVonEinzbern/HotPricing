from django.urls import path
from . import views

urlpatterns = [
    # Otras rutas...
    path('api/hoteles/registrar', views.vista_registro, name='vista_registro'),
    path('api/hoteles/<int:pk>', views.eliminar_registro, name='eliminar_registro'),
    path('api/hoteles/eliminar', views.eliminar_registro_completo, name='eliminar_registro_completo'),
    path('api/hoteles/listar', views.listar_hoteles, name='listar_hoteles'),
    path('api/hoteles/listar/<str:ciudad>/', views.listar_hoteles_ciudad, name='listar_hoteles_ciudad'),
    path('api/hoteles/scrap', views.scrap_hoteles, name='scrap_hoteles'),
]