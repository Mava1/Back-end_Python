
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Producto



class ProductoBaseView(View):
    template_name = 'producto.html'
    model = Producto
    fields = '__all__'
    success_url = reverse_lazy('producto:all')


class ProductoListView(ProductoBaseView,ListView):
    ...

class ProductoDetailView(ProductoBaseView,DetailView):
    template_name = "producto_detail.html"

class ProductoCreateView(ProductoBaseView,CreateView):
    template_name = "producto_create.html"
    extra_context = {
        "tipo": "Crear producto"
    }


class ProductoUpdateView(ProductoBaseView,UpdateView):
    template_name = "producto_create.html"
    extra_context = {
        "tipo": "Actualizar "
    }

class ProductoDeleteView(ProductoBaseView,DeleteView):
    template_name = "producto_delete.html"
    extra_context = {
        "tipo": "Borrar "
    }

