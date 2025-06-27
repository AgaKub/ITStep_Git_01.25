from django.urls import path
from .import views

urlpatterns = [
    path("", views.lista_postow, name="blog_list"),
    path("<int:post_id>", views.szczegoly_postu, name ="blog_szczegoly"),
    path("dodaj/", views.dodaj_post, name="blog_dodaj"),
    path("o nas", views.o_nas, name="o_nas"),
    ]