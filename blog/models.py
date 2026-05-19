from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=200)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to="pages/")
    fecha_publicacion = models.DateField()
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="pages",
    )

    class Meta:
        ordering = ["-fecha_publicacion"]
        verbose_name = "Página"
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.titulo
