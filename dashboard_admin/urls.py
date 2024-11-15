from django.urls import path
from . import views

urlpatterns = [
    path("modAdmin/", views.moduloadmin_view, name='modulo_admin'),
    path("inventario/", views.inventario_view, name='inventario'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/:id', views.edit_product, name='edit_product'),
    path("hisVentas/", views.hisVentas_view, name='hisVentas'),
    path("hisCompras/", views.hisCompras_view, name='hisCompras'),
    path("gestionUsusarios/", views.gestionUsusarios_view, name='gestionUsuarios'),
    path("infoClientes/", views.infoClientes_view, name='infoClientes'),
    path("proveedores/", views.proveedores_view, name='proveedores'),
    path('add_provider/', views.add_provider, name='add_provider'),
    path('editar_acerca_de/', views.editar_acerca_de, name='editar_acerca_de'),
]