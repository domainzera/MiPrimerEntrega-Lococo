from django.shortcuts import render

from .forms import AutorForm, BuscarPostForm, CategoriaForm, PostForm
from .models import Post


def inicio(request):
    return render(request, "blog/inicio.html")


def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                "blog/form_exito.html",
                {"mensaje": "Autor creado correctamente."},
            )
    else:
        form = AutorForm()
    return render(
        request,
        "blog/formulario.html",
        {"form": form, "titulo": "Crear autor"},
    )


def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                "blog/form_exito.html",
                {"mensaje": "Categoria creada correctamente."},
            )
    else:
        form = CategoriaForm()
    return render(
        request,
        "blog/formulario.html",
        {"form": form, "titulo": "Crear categoria"},
    )


def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                "blog/form_exito.html",
                {"mensaje": "Post creado correctamente."},
            )
    else:
        form = PostForm()
    return render(
        request,
        "blog/formulario.html",
        {"form": form, "titulo": "Crear post"},
    )


def buscar_post(request):
    resultados = []
    titulo = ""

    if request.method == "GET":
        form = BuscarPostForm(request.GET)
        if form.is_valid():
            titulo = form.cleaned_data["titulo"]
            if titulo:
                resultados = Post.objects.filter(titulo__icontains=titulo)
    else:
        form = BuscarPostForm()

    return render(
        request,
        "blog/buscar_post.html",
        {"form": form, "resultados": resultados, "titulo_buscado": titulo},
    )
