from django.db import models
from datetime import datetime, timedelta


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.FloatField(null=True)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    fecha_vencimiento = models.DateField(default=datetime.today() + timedelta(days=365))
    foto = models.ImageField( blank=True, null=True)

    def __str__(self):
        return self.nombre