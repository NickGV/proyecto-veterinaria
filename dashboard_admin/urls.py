from django.urls import path
from .templates import views

urlpatterns = [
  path("modAdmin/", views.moduloadmin_view, name='modulo_admin'),
  path("Inventario/", views.Inventario_view, name='inventario'),
  path("hisVentas/", views.hisVentas_view, name='hisVentas'),
  path("hisCompras/", views.hisCompras_view, name='hisCompras'),
  path("GestionUsusarios/", views.GestionUsusarios_view, name='GestionUsuarios'),
  path("infoClientes/", views.infoClientes_view, name='infoClientes'),
]