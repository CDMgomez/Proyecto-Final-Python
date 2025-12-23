from django.urls import path
from .views import PagesListView, PageDetailView
from . import views
from .views import (
    PagesListView,
    PageDetailView,
    ProductoUpdateView,
    ProductoDeleteView,
    ProductoCreateView,
)

urlpatterns = [
    path('', PagesListView.as_view(), name='pages_list'),  # Cambiado de views.pages_list a PagesListView.as_view()
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('crear/', ProductoCreateView.as_view(), name='producto_crear'),
    path('editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_editar'),
    path('borrar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_borrar'),
]

