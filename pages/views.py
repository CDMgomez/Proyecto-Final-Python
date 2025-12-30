from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Producto
from django.contrib.auth.mixins import UserPassesTestMixin


class PagesListView(ListView):
    model = Producto
    template_name = "pages/pages_list.html"
    context_object_name = "productos"

class PageDetailView(DetailView):
    model = Producto
    template_name = "pages/page_detail.html"
    context_object_name = "producto"

class ProductoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Producto
    fields = ['nombre', 'categoria', 'descripcion', 'precio', 'imagen']
    template_name = 'pages/producto_form.html'
    success_url = reverse_lazy('pages_list')

    def test_func(self):
        return self.request.user.is_staff


class ProductoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Producto
    fields = ['nombre', 'categoria', 'descripcion', 'precio', 'imagen']
    template_name = 'pages/producto_form.html'
    success_url = reverse_lazy('pages_list')

    def test_func(self):
        return self.request.user.is_staff

class ProductoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Producto
    template_name = 'pages/producto_confirm_delete.html'
    success_url = reverse_lazy('pages_list')

    def test_func(self):
        return self.request.user.is_staff



