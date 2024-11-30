from django.urls import path
from . import views

urlpatterns = [
    path("modAdmin/", views.moduloadmin_view, name='modulo_admin'),
    path('inventario/', views.inventario_view, name='inventario'),
    path('inventario/agregar/', views.add_product, name='add_product'),
    path('inventario/editar/<int:pk>/', views.edit_product, name='edit_product'),
    path('inventario/eliminar/<int:pk>/', views.delete_product, name='delete_product'),
    path("hisCompras/", views.hisCompras_view, name='hisCompras'),
    path("gestionUsusarios/", views.gestionUsusarios_view, name='gestionUsuarios'),
    path("infoClientes/", views.infoClientes_view, name='infoClientes'),
    path('proveedores/', views.proveedores_view, name='proveedores'),
    path('proveedores/agregar/', views.add_provider, name='add_provider'),
    path('proveedores/editar/<int:pk>/', views.edit_provider, name='edit_provider'),
    path('proveedores/eliminar/<int:pk>/', views.delete_provider, name='delete_provider'),
    path('proveedores/catalogo/<int:proveedor_id>/', views.ver_catalogo, name='ver_catalogo'),
    path('proveedores/catalogo/agregar/<int:proveedor_id>/', views.agregar_producto_catalogo, name='agregar_producto_catalogo'),
    path('compras/agregar/', views.add_compra, name='add_compra'),
    path('get_productos_proveedor/<int:proveedor_id>/', views.get_productos_proveedor, name='get_productos_proveedor'),
    path('ventas/agregar/', views.add_venta, name='add_venta'),
    path('editar_acerca_de/', views.editar_acerca_de, name='editar_acerca_de'),
    path('editar_menu/', views.editar_menu, name='editar_menu'),
    path('Users/agregar/', views.add_user, name='add_user'),
    path('Users/editar/<int:pk>/', views.edit_user, name='edit_user'),
    path('Users/eliminar/<int:pk>/', views.delete_user, name='delete_user'),
    path("hisVentas/", views.hisVentas_view, name='hisVentas'),
    path('Reportes/', views.reportes_view, name='reportes'),

]