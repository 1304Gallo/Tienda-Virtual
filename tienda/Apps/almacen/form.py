from django import forms
from .models import *
from datetime import datetime, timedelta

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'codigo',
            'categoria',
            'cantidad',
            'precio',
            'fecha_vencimiento',
            'foto',
        ]
        labels = {
            'nombre': 'Nombre',
            'codigo': 'Codigo',
            'categoría':'Categoria',
            'cantidad': 'Cantidad',
            'precio': 'Precio',
            'fecha_vencimiento': 'Fecha de vencimiento',
            'foto': 'Foto',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'categoría': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'precio': forms.TextInput(attrs={'class': 'form-control','type': 'number', 'step': '0.01', 'required': True}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': True}),
            'foto': forms.FileInput(attrs={'class': 'form-control', 'required': True}),
        }

  