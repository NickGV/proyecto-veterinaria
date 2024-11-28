from django.urls import path
from . import views

urlpatterns = [
    path("modAdmin/", views.moduloadmin_view, name='modulo_admin'),
    path('inventario/', views.inventario_view, name='inventario'),
    path('inventario/agregar/', views.add_product, name='add_product'),
    path('inventario/editar/<int:pk>/', views.edit_product, name='edit_product'),
    path('inventario/eliminar/<int:pk>/', views.delete_product, name='delete_product'),
    path("hisVentas/", views.hisVentas_view, name='hisVentas'),
    path("hisCompras/", views.hisCompras_view, name='hisCompras'),
    path("gestionUsusarios/", views.gestionUsusarios_view, name='gestionUsuarios'),
    path("infoClientes/", views.infoClientes_view, name='infoClientes'),
    path("proveedores/", views.proveedores_view, name='proveedores'),
    path('proveedores/agregar/', views.add_provider, name='add_provider'),
    path('proveedores/editar/<int:pk>/', views.edit_provider, name='edit_provider'),
    path('proveedores/eliminar/<int:pk>/', views.delete_provider, name='delete_provider'),
    path('compras/agregar/', views.add_compra, name='add_compra'),
    path('ventas/agregar/', views.add_venta, name='add_venta'),
    path('editar_acerca_de/', views.editar_acerca_de, name='editar_acerca_de'),
    path('editar_menu/', views.editar_menu, name='editar_menu'),
]