from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

class Venta(models.Model):
    cantidad_productos = models.IntegerField()
    nombre_producto = models.CharField(max_length=50)
    numero_serie_productos = models.IntegerField(null=True)
    id_venta = models.AutoField(primary_key=True)
    precio_producto = models.IntegerField(default=0)
    dinero_recaudado = models.IntegerField()
    fecha_hora_venta = models.DateTimeField(default=timezone.now)
    cliente = models.CharField(max_length=100, default="Cliente Anónimo")

def __str__(self):
        return f"Venta #{self.id_venta} - {self.nombre_producto}"