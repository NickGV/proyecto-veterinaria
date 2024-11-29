from django.shortcuts import render
from dashboard_admin.models import Producto
# Create your views here.

def tienda_view(request):
  productos = Producto.objects.all()
  return render(request, 'tienda.html', {'productos': productos})

