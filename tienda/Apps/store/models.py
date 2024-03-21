from django.db import models
from django.contrib.auth.models import User
from Apps.almacen.models import Producto

# Create your models here.

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null= True)
    email = models.CharField(max_length=200, null= True)

    def __str__(self):
        return self.name


class Compra(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL,blank=True, null=True)
    eliminar_orden = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    id_transaccion = models.CharField(max_length=200, null=True)


    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        articuloscompra = self.articuloscompra_set.all()
        total = sum([articulo.get_total for articulo in articuloscompra])
        return total
    
    @property
    def get_cart_articulo(self):
        articuloscompra = self.articuloscompra_set.all()
        total = sum([articulo.cantidad for articulo in articuloscompra])
        return total

class ArticulosCompra(models.Model):
    productos = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    compra = models.ForeignKey(Compra, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=False)
    fecha_añadido = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.productos.precio * self.cantidad
        return total
    
class DireccionCompra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    compra = models.ForeignKey(Compra, on_delete=models.SET_NULL, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True)
    provincia = models.CharField(max_length=200, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.direccion


   
