from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("artworks/", views.getArtworksAll, name="artworks"),
    path("accounts/profile/", views.index, name="index"),
    path("accounts/register/", views.register, name="register")
]
