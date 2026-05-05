from django import forms

from .models import Autor, Categoria, Post


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre", "email", "biografia"]


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre", "descripcion"]


class PostForm(forms.ModelForm):
    fecha_publicacion = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Post
        fields = ["titulo", "contenido", "fecha_publicacion", "autor", "categoria"]


class BuscarPostForm(forms.Form):
    titulo = forms.CharField(max_length=150, required=False)
