from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages

# Create your views here.
def auth_view(request):
  return render(request, 'auth.html')

def editar_view(request):
  return render(request, 'editar_perfilU.html')

def recuperar_view(request):
  return render(request, 'recuperar.html')