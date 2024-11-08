from django.shortcuts import render

def menu_view(request):
    return render(request, 'menu.html')

def acercaC_view(request):
    return render(request, 'AcercaC.html')	