from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Producto

class PagesListView(ListView):
    model = Producto
    template_name = "pages/pages_list.html"
    context_object_name = "productos"

class PageDetailView(DetailView):
    model = Producto
    template_name = "pages/page_detail.html"
    context_object_name = "producto"

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    fields = ['nombre', 'categoria', 'descripcion', 'precio', 'imagen']
    template_name = 'pages/producto_form.html'
    success_url = reverse_lazy('pages_list')

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    fields = ['nombre', 'categoria', 'descripcion', 'precio', 'imagen']
    template_name = 'pages/producto_form.html'
    success_url = reverse_lazy('pages_list')

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'pages/producto_confirm_delete.html'  # Crea este template si no existe
    success_url = reverse_lazy('pages_list')




