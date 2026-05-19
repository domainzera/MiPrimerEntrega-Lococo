from django.contrib import admin

from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("titulo", "subtitulo", "autor", "fecha_publicacion")
    list_filter = ("fecha_publicacion", "autor")
    search_fields = ("titulo", "subtitulo", "contenido")
