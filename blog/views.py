from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import BuscarPageForm, PageForm
from .models import Page


def inicio(request):
    return render(request, "blog/inicio.html")


def about(request):
    return render(request, "blog/about.html")


class PageListView(ListView):
    model = Page
    template_name = "blog/page_list.html"
    context_object_name = "pages"

    def get_queryset(self):
        return Page.objects.select_related("autor")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_buscar"] = BuscarPageForm(self.request.GET or None)
        return context


class PageDetailView(DetailView):
    model = Page
    template_name = "blog/page_detail.html"
    context_object_name = "page"


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = "blog/page_form.html"
    success_url = reverse_lazy("page_list")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Crear página"
        return context


class PageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = "blog/page_form.html"
    success_url = reverse_lazy("page_list")

    def test_func(self):
        page = self.get_object()
        return self.request.user == page.autor or self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Editar página"
        return context


class PageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Page
    template_name = "blog/page_confirm_delete.html"
    success_url = reverse_lazy("page_list")

    def test_func(self):
        page = self.get_object()
        return self.request.user == page.autor or self.request.user.is_staff


def buscar_page(request):
    resultados = []
    titulo_buscado = ""

    if request.method == "GET" and request.GET:
        form = BuscarPageForm(request.GET)
        if form.is_valid():
            titulo_buscado = form.cleaned_data["titulo"]
            if titulo_buscado:
                resultados = Page.objects.filter(titulo__icontains=titulo_buscado)
    else:
        form = BuscarPageForm()

    return render(
        request,
        "blog/buscar_page.html",
        {
            "form": form,
            "resultados": resultados,
            "titulo_buscado": titulo_buscado,
        },
    )
