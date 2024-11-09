from django.shortcuts import render

# Create your views here.
def moduloadmin_view(request):
     return render(request, 'modAdmin.html')

def Inventario_view(request):
     return render(request, 'Inventario.html')

def hisVentas_view(request):
     return render(request, 'hisVentas.html')

def hisCompras_view(request):
     return render(request, 'hisCompras.html')

def GestionUsusarios_view(request):
     return render(request, 'GestionUsuarios.html')
def infoClientes_view(request):
     return render(request, 'infoClient.html')
