from django.urls import path
from .views import *

urlpatterns = [
    
    path('', StoreView, name='store'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', SheckoutView.as_view(), name='checkout'),

    
    path('Actualizar_Articulos/', actualizar_articulos, name='Actualizar_Articulos'), 
    
]