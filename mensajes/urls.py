from django.urls import path

from . import views

urlpatterns = [
    path("", views.MensajeRecibidosListView.as_view(), name="mensaje_recibidos"),
    path("enviados/", views.MensajeEnviadosListView.as_view(), name="mensaje_enviados"),
    path("nuevo/", views.MensajeCreateView.as_view(), name="mensaje_nuevo"),
    path("<int:pk>/", views.mensaje_detalle, name="mensaje_detalle"),
]
