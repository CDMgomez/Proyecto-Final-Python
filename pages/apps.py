from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'pages'

    def ready(self):
        from django.contrib import admin
        from .models import Producto
        admin.site.register(Producto)
