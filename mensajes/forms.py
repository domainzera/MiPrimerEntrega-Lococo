from django import forms
from django.contrib.auth.models import User

from .models import Mensaje


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ["destinatario", "asunto", "cuerpo"]
        widgets = {
            "cuerpo": forms.Textarea(attrs={"rows": 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["destinatario"].queryset = User.objects.order_by("username")
