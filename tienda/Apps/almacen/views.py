from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponse as HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, TemplateView
from .models import *
from .form import ProductoForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
categoriasList = ['Electrodomésticos', 'Comida', 'Bebida', 'Limpieza', 'Cárnicos', 'ropa']




class ListarProductos(ListView):
    model = Producto
    template_name = 'listar_producto.html'


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CrearProductos(CreateView):
    model = Producto
    template_name = 'crear_producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('listar_productos')

    def form_valid(self, form):
        foto = self.request.FILES['foto']
        return super().form_valid(form)


class EliminarProductos(DeleteView):
    model = Producto
    template_name = 'eliminar_producto.html'
    success_url = reverse_lazy('listar_productos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar producto'
        context['entity'] = 'Producto'
        context['list_url'] = reverse_lazy('almacen:ListarProductos')

        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        return obj


class Index(TemplateView):
    template_name = 'base.html'
