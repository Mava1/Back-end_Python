from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import IndexPage , Contacto, Perros, Productos, Gatos

urlpatterns = [

    path("admin/", admin.site.urls),
    path("", IndexPage.as_view(), name = "index"),
    path("contacto/", Contacto.as_view(), name="contacto"),
    path("perros/" , Perros.as_view(), name= "perros"),
    path("gatos/" , Gatos.as_view(), name= "gatos"),
    path("productos/" , Productos.as_view(), name= "productos"),
    path("producto/", include("app_tienda.urls")),

]




    
