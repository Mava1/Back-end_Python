from django.views.generic import TemplateView

class IndexPage (TemplateView):
    template_name = "index.html"

class Contacto (TemplateView):
    template_name = "contacto.html"    

class Perros (TemplateView):
    template_name = "perros.html"    

class Gatos (TemplateView):
    template_name = "gatos.html"    

class Tienda (TemplateView):
    template_name = "tienda.html"   

  