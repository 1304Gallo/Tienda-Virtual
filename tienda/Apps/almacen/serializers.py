from rest_framework import serializers
from Apps.almacen.models import Producto

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'codigo', 'cantidad', 'precio', 'fecha_vencimiento', 'foto')
        read_only_fields = ['codigo', ]