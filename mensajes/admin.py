from django.contrib import admin

from .models import Mensaje


@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ("asunto", "remitente", "destinatario", "fecha", "leido")
    list_filter = ("leido", "fecha")
    search_fields = ("asunto", "cuerpo", "remitente__username", "destinatario__username")
