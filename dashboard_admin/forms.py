from django import forms
from .models import AcercaDe, Producto, Proveedor, Compra, Menu

class AcercaDeForm(forms.ModelForm):
    mision = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    ubicacion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    instagram = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    facebook = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    whatsapp = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = AcercaDe
        fields = ['mision', 'ubicacion', 'instagram', 'facebook', 'telefono', 'whatsapp']

class MenuForm(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    subtitulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    servCaninos = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    servFelinos = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    testimonios = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    class Meta:
        model = Menu
        fields = ['titulo', 'subtitulo', 'servCaninos', 'servFelinos', 'testimonios']
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad_disponible', 'categoria', 'imagen']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'contacto', 'direccion', 'telefono', 'catalogo']

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['proveedor', 'producto', 'cantidad']

