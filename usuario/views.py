from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages

# Create your views here.
def login_view(request):
  return render(request, 'login.html')

def register_view(request):
  return render(request, 'registro.html')

def editar_view(request):
  return render(request, 'editar_perfilU.html')

def recuperar_view(request):
  return render(request, 'recuperar.html')