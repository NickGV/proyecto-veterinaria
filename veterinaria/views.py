from django.shortcuts import render

def menu_view(request):
    return render(request, '../templates/menu.html')

def acercaC_view(request):
    return render(request, '../templates/AcercaC.html')	