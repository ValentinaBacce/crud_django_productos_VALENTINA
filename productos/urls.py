from django.urls import path
from .views import (
    ProductoListView, ProductoDetailView,
    ProductoCreateView, ProductoUpdateView, ProductoDeleteView,
    api_productos_list, api_productos_create,  #  importamos las nuevas funciones
)

app_name = 'productos'

urlpatterns = [
    # --- Vistas HTML (interfaz web) ---
    path('', ProductoListView.as_view(), name='lista'),
    path('nuevo/', ProductoCreateView.as_view(), name='crear'),
    path('<int:pk>/', ProductoDetailView.as_view(), name='detalle'),
    path('<int:pk>/editar/', ProductoUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='eliminar'),

    # --- Endpoints API (para Postman) ---
    path('api/productos/', api_productos_list, name='api_list'),
    path('api/productos/create/', api_productos_create, name='api_create'),
]
