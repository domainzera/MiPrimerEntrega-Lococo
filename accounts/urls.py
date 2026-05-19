from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("perfil/", views.perfil, name="perfil"),
    path("perfil/editar/", views.ProfileUpdateView.as_view(), name="perfil_editar"),
    path(
        "perfil/cambiar-password/",
        views.CustomPasswordChangeView.as_view(),
        name="password_change",
    ),
]
