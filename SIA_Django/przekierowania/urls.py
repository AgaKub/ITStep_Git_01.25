from django.urls import path
from .import views

urlpatterns = [
    path("nowa/", views.nowa_strona, name="nowa_strona"),
    path("stara/", views.stara_strona, name="stara"),
    path("zewnetrzna/", views.przekieruj_na_zewnetrzna, name="zewnetrzna"),


]