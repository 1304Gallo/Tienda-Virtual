from django import forms
from .models import *
from datetime import datetime, timedelta

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'codigo',
            'cantidad',
            'precio',
            'fecha_vencimiento',
            'foto',
        ]
        labels = {
            'nombre': 'Nombre',
            'codigo': 'Codigo',
            'cantidad': 'Cantidad',
            'precio': 'Precio',
            'fecha_vencimiento': 'Fecha de vencimiento',
            'foto': 'Foto',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'precio': forms.TextInput(attrs={'class': 'form-control','type': 'number', 'step': '0.01', 'required': True}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': True}),
            'foto': forms.FileInput(attrs={'class': 'form-control', 'required': True}),
        }

  