from django.shortcuts import render
from dashboard_admin.models import AcercaDe, Menu

def menu_view(request):
    menu = Menu.objects.first()
    return render(request, 'menu.html', {'menu': menu})

def acercaC_view(request):
    acerca_de = AcercaDe.objects.first()
    return render(request, 'AcercaC.html', {'acerca_de': acerca_de})