from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.login_view, name='login'),
  path('registro/', views.register_view, name='registro'),
  path('editar_perfilU/', views.editar_view, name='editar_perfilU'), 
  path('recuperar/', views.recuperar_view, name='recuperar'),
]
