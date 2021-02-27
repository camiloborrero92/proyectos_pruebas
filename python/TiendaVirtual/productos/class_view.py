from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.urls import reverse_lazy
from .forms import ProductoForm
from .models import Producto

class ProductoList(ListView):
    model = Producto
    template_name = 'index.html'
    
    def get_queryset(self):
        return self.model.objects.all()[:]
    
    
# class ProductoCreate(CreateView):
#     model = Producto
#     form_class = ProductoForm
#     template_name = 'crear_Producto.html'
#     success_url = reverse_lazy('index')


# class ProductoUpdate(UpdateView):
#     model = Producto
#     form_class = ProductoForm
#     template_name = 'crear_Producto.html'
#     success_url = reverse_lazy('index')
    
# class ProductoDelete(DeleteView):
#     model = Producto
#     template_name = 'verificacion.html'
#     success_url = reverse_lazy('index')