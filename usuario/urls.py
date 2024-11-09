from django.urls import path
from . import views

urlpatterns = [
  path('auth/', views.auth_view, name='auth'),
  path('editar_perfilU/', views.editar_view, name='editar_perfilU'), 
  path('recuperar/', views.recuperar_view, name='recuperar'),
]
