
# app_productos/views.py

from django.views.generic import ListView, DetailView
from .models import Producto

class ListaProductosView(ListView):
    model = Producto
    template_name = 'lista_productos.html'
    context_object_name = 'productos'

from django.shortcuts import render
from .models import Producto

def home(request):
    return render(request, 'index.html')