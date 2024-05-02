from django.urls import path
from .views import *

urlpatterns = [
    
    path('', StoreView, name='store'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', SheckoutView.as_view(), name='checkout'),

    
    path('actualizar_articulos/', actualizar_articulos, name='actualizar_articulos'),
    
]