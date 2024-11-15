from django.shortcuts import render
from dashboard_admin.models import AcercaDe

def menu_view(request):
    return render(request, 'menu.html')

def acercaC_view(request):
    acerca_de = AcercaDe.objects.first()
    return render(request, 'AcercaC.html', {'acerca_de': acerca_de})