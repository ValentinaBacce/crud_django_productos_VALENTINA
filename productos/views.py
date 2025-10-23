from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto

# --- CBVs (interfaz HTML) ---
class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/producto_list.html'
    context_object_name = 'productos'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'productos/producto_detail.html'
    context_object_name = 'producto'

class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'stock']
    template_name = 'productos/producto_form.html'

class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'stock']
    template_name = 'productos/producto_form.html'

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/producto_confirm_delete.html'
    success_url = reverse_lazy('productos:lista')


# --- API minima para Postman (JSON) ---
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

def api_productos_list(request):
    """GET: devuelve lista de productos en JSON."""
    if request.method != 'GET':
        return JsonResponse({'detail': 'Metodo no permitido'}, status=405)
    data = [
        {
            'id': p.id,
            'nombre': p.nombre,
            'descripcion': p.descripcion,
            'precio': float(p.precio),
            'stock': p.stock,
        }
        for p in Producto.objects.all()
    ]
    return JsonResponse({'count': len(data), 'results': data}, status=200)

@csrf_exempt
def api_productos_create(request):
    """POST: crea un producto a partir de JSON."""
    if request.method != 'POST':
        return JsonResponse({'detail': 'Metodo no permitido'}, status=405)
    try:
        payload = json.loads(request.body.decode('utf-8'))
        nombre = payload.get('nombre')
        descripcion = payload.get('descripcion', '')
        precio = payload.get('precio')
        stock = payload.get('stock', 0)

        if not nombre or precio is None:
            return HttpResponseBadRequest('Campos requeridos: nombre, precio')

        producto = Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock
        )
        return JsonResponse({
            'id': producto.id,
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': float(producto.precio),
            'stock': producto.stock,
        }, status=201)
    except json.JSONDecodeError:
        return HttpResponseBadRequest('JSON invalido')
