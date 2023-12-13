
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Producto

# Create your views here.


class ProductoBaseView(View):
    template_name = 'producto.html'
    model = Producto
    fields = '__all__'
    success_url = reverse_lazy('Producto:all')


class ProductoListView(ProductoBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS VINOS
    """

class ProductoDetailView(ProductoBaseView,DetailView):
    template_name = "producto_detail.html"

class ProductoCreateView(ProductoBaseView,CreateView):
    template_name = "producto_create.html"
    extra_context = {
        "tipo": "Crear vino"
    }


class ProductoUpdateView(ProductoBaseView,UpdateView):
    template_name = "producto_create.html"
    extra_context = {
        "tipo": "Actualizar vino"
    }

class ProductoDeleteView(ProductoBaseView,DeleteView):
    template_name = "producto_delete.html"
    extra_context = {
        "tipo": "Borrar vino"
    }

