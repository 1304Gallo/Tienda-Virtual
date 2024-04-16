from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse
from Apps.almacen.models import Producto
from .models import *
from django.http import request
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Sum
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.models import User


def StoreView(request):
    if request.method == 'GET':
        cartArticulos = 0
        if request.user.is_authenticated:
            if hasattr(request.user, 'cliente'):
                cliente = request.user.cliente
                compra, created = Compra.objects.get_or_create(Cliente=cliente, complete=False)
                articulos = compra.articuloscompra_set.all()
                cartArticulos = ArticulosCompra.objects.filter(compra=compra).count()
            else:
                pass

        context = {
            'productos': Producto.objects.all(),
            'articulos': [],
            'cartArticulos': cartArticulos,
        }

        return render(request, 'store.html', context)

    elif request.method == 'POST':
        # Manejar la solicitud POST para actualizar el carrito
        data = json.loads(request.body)
        productoID = data['productoID']
        action = data['action']
        return JsonResponse({'success': True})

    else:
        articulos = []
        compra = {'get_cart_articulo': 0, 'get_cart_total': 0}
        cartArticulos = ArticulosCompra.objects.filter(compra=compra).count()


class CartView(View):
    def get(self, request):

        articulos = []
        cartArticulos = 0
        compra = {'get_cart_articulo': 0, 'get_cart_total': 0}

        if request.user.is_authenticated:
            if hasattr(request.user, 'cliente'):
                cliente = request.user.cliente
                compra, created = Compra.objects.get_or_create(Cliente=cliente, complete=False)
                articulos = compra.articuloscompra_set.all()
                cartArticulos = ArticulosCompra.objects.filter(compra=compra).count()

                # Debug para imprimir las cantidades de los artículos
                for articulo in articulos:
                    print(f"Cantidad de {articulo.productos.nombre}: {articulo.cantidad}")

                # Recargar los artículos después de las actualizaciones
                articulos = compra.articuloscompra_set.all()
            else:
                # Si el usuario no tiene un carrito, se mantienen los valores por defecto
                pass
        else:
            # Si el usuario no está autenticado, se mantienen los valores por defecto
            pass

        if not isinstance(compra, dict):
            compra = {'get_cart_articulo': cartArticulos, 'get_cart_total': 0}  # Ajusta los valores según sea necesario

        context = {'articulos': articulos, 'compra': compra, 'cartArticulos': cartArticulos}
        return render(request, 'Cart.html', context)


class SheckoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            cliente = request.user.cliente
            compra, created = Compra.objects.get_or_create(Cliente=cliente, complete=False)
            articulos = compra.articuloscompra_set.all()
            cartArticulos = ArticulosCompra.objects.filter(compra=compra).count()

            for articulo in articulos:
                articulo.total = articulo.productos.precio * articulo.cantidad
        else:
            articulos = []
            compra = {'get_cart_articulo': 0, 'get_cart_total': 0}

        context = {'articulos': articulos, 'compra': compra, 'cartArticulos': cartArticulos}
        return render(request, 'Checkout.html', context)


@require_POST
def actualizar_articulos(request):
    try:
        data = json.loads(request.body)
        productoID = data['productoID']
        action = data['action']

        print('action:', action)
        print('productoID:', productoID)

        # Asegurarse de que el usuario esté autenticado
        if not request.user.is_authenticated:
            return HttpResponseForbidden("No estás autenticado")

        cliente = request.user.cliente
        producto = Producto.objects.get(id=productoID)
        compra, created = Compra.objects.get_or_create(Cliente=cliente, complete=False)

        articulo_compra, created = ArticulosCompra.objects.get_or_create(compra=compra, productos=producto)
        total_articulos = ArticulosCompra.objects.filter(compra=compra).count()

        if action == 'add':
            articulo_compra.cantidad += 1

        elif action == 'remove':
            # Lógica para eliminar un producto del carrito
            articulo_compra.delete()
            total_articulos = ArticulosCompra.objects.filter(compra=compra).count()
            return JsonResponse({'total_articulos': total_articulos}, safe=False)

        elif action == 'decrement':
            if articulo_compra.cantidad > 1:
                articulo_compra.cantidad -= 1
            else:
                print("La cantidad no puede ser menor que  1")

        articulo_compra.save()

        # Devolver la nueva cantidad en la respuesta JSON
        return JsonResponse({'nueva_cantidad': articulo_compra.cantidad, 'total_articulos': total_articulos},
                            safe=False)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
