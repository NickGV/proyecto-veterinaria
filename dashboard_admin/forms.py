from django import forms
from .models import AcercaDe

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
