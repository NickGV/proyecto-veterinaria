from django import forms
from .models import AcercaDe, Producto, Proveedor, Compra, Venta

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

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['producto', 'cantidad', 'cliente', 'telefono', 'correo']