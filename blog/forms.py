from django import forms

from .models import Page


class PageForm(forms.ModelForm):
    fecha_publicacion = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Page
        fields = ["titulo", "subtitulo", "contenido", "imagen", "fecha_publicacion"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["imagen"].required = False


class BuscarPageForm(forms.Form):
    titulo = forms.CharField(max_length=150, required=False, label="Buscar por título")
