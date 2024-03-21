from django.urls import path, include
from .views import ListarProductos, Index, CrearProductos, EliminarProductos
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
from .api import ProductoViewsets


routers = DefaultRouter()

routers.register(r'almacen', ProductoViewsets, basename='almacen')

urlpatterns = [
    
    path('base', Index.as_view(), name='base'),
    

    #productos
    path('listar/', login_required(ListarProductos.as_view()) , name='listar_productos'),
    path('crear/', CrearProductos.as_view(), name='crear'),
    path('eliminar/<int:pk>/', EliminarProductos.as_view(), name='eliminar_producto'),
    path('api/', include(routers.urls)), 
]