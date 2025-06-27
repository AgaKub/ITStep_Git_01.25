from django.urls import path

from . import views

urlpatterns = [

    path("blad400/", views.widok_z_bledem_400, name='blad400'),

    path('nieznaleziona/', views.strona_nie_znaleziona, name='nieznaleziona'),

    path('brakdostepu/', views.widok_z_brakiem_dostepu, name='brakdostepu')

]
