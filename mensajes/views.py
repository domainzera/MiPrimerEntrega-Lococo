from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import MensajeForm
from .models import Mensaje


class MensajeRecibidosListView(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = "mensajes/mensaje_list.html"
    context_object_name = "mensajes"

    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user).select_related(
            "remitente"
        )


class MensajeEnviadosListView(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = "mensajes/mensaje_enviados.html"
    context_object_name = "mensajes"

    def get_queryset(self):
        return Mensaje.objects.filter(remitente=self.request.user).select_related(
            "destinatario"
        )


class MensajeCreateView(LoginRequiredMixin, CreateView):
    model = Mensaje
    form_class = MensajeForm
    template_name = "mensajes/mensaje_form.html"
    success_url = reverse_lazy("mensaje_recibidos")

    def form_valid(self, form):
        form.instance.remitente = self.request.user
        return super().form_valid(form)


@login_required
def mensaje_detalle(request, pk):
    mensaje = get_object_or_404(
        Mensaje,
        pk=pk,
    )
    if request.user not in (mensaje.remitente, mensaje.destinatario):
        return redirect("mensaje_recibidos")

    if request.user == mensaje.destinatario and not mensaje.leido:
        mensaje.leido = True
        mensaje.save(update_fields=["leido"])

    return render(request, "mensajes/mensaje_detalle.html", {"mensaje": mensaje})
