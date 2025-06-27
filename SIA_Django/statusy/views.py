from django.shortcuts import render
from django.http import HttpResponse

def widok_z_bledem_400(request):
    return HttpResponse("Nieprawidlowe żadanie", status=400)


def widok_z_brakiem_dostepu(request):
    return HttpResponse("Brak dostępu", status=403)

def strona_nie_znaleziona(request):
    return HttpResponse("Strona nie zostala znaleziona.")


