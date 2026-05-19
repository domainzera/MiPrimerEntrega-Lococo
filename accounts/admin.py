from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "link", "fecha_nacimiento")
    search_fields = ("user__username", "user__email", "biografia")
