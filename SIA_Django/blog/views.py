from django.shortcuts import render
from django.http import HttpResponse

def o_nas(request):
    return HttpResponse("To jest strona o nas.")

def lista_postow(request):
    return HttpResponse("Lista postów na blogu")

def szczegoly_postu(request):
    return HttpResponse("Szczególy postu o ID: {posrt_id}")

def dodaj_post(request):
    return HttpResponse("Formularz dodawania nowego postu.")


