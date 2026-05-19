from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("about/", views.about, name="about"),
    path("pages/", views.PageListView.as_view(), name="page_list"),
    path("pages/<int:pk>/", views.PageDetailView.as_view(), name="page_detail"),
    path("pages/nueva/", views.PageCreateView.as_view(), name="page_create"),
    path("pages/<int:pk>/editar/", views.PageUpdateView.as_view(), name="page_update"),
    path("pages/<int:pk>/eliminar/", views.PageDeleteView.as_view(), name="page_delete"),
    path("pages/buscar/", views.buscar_page, name="page_buscar"),
]
