from .models import Producto
from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.

@admin.register (Producto)
class ProductoAdmin(ModelAdmin):
    ...