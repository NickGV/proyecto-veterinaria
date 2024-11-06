from django.urls import path
from . import views

urlpatterns = [
  path("tienda/", views.tienda_view, name='tienda'),
  path("carrito/", views.carrito_view, name='carrito'),
]