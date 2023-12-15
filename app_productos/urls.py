from django.contrib import admin
from django.urls import path
from .views import ListaProductosView

app_name = 'app_productos'

urlpatterns = [

    path('productos/', ListaProductosView.as_view(), name='lista_productos'),
]
