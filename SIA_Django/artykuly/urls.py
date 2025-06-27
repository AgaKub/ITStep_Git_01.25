from django.urls import path
from. import views

urlpatterns = [
    path("sciezka/<path:reszta_sciezki>/",views.przekaz_sciezke, name="sciezka"),
    path("artykul/<int:rok>/<slug:tytul>/",views.wyswietl_artykul, name="artykul"),
    path("profil/<str:username>/", views.profil_uzytkownika, name="profil"),
    path("id/<uuid:id_wpisu>/", views.szczegoly_wpisu_uuid, name="wpis_uuid)")
]