from django.shortcuts import render
from django.http import HttpResponse

def wyswietl_artykul(request, rok, tytul):
    return HttpResponse(f"Artykuł z roku: {rok}, tytuł: {tytul}")

def profil_uzytkownika(request, username):
    return HttpResponse(f"Profil użytkownika: {username}")

def przekaz_sciezke(request, reszta_sciezki):
    return HttpResponse(f"Przekazana ścieżka: {reszta_sciezki}")

def szczegoly_wpisu_uuid(request, id_wpisu):
    return HttpResponse(f"Szczegóły wpisu o ID: {id_wpisu}")