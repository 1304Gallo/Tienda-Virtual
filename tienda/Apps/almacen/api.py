from Apps.almacen.models import Producto
from rest_framework import viewsets, permissions
from .serializers import ProductoSerializers

class ProductoViewsets(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializers