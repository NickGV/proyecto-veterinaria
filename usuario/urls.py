from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth_view, name='auth'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('eliminar_usuario/', views.eliminar_usuario, name='eliminar_usuario'),
    path('editar_perfilU/', views.editar_view, name='editar_perfilU'), 
    path('recuperar/', views.recuperar_view, name='recuperar'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/modificar/<int:producto_id>/', views.modificar_cantidad, name='modificar_cantidad'),
    path('carrito/', views.ver_carrito, name='carrito'),
]