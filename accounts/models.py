from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    biografia = models.TextField(blank=True)
    link = models.URLField(blank=True, verbose_name="Sitio web o red social")
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
