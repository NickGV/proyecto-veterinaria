from django.shortcuts import render

# Create your views here.

def tienda_view(request):
  return render(request, 'tienda.html')

def carrito_view(request):
  return render(request, 'carrito.html')