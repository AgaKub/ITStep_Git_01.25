from django.shortcuts import render, redirect
from django.http import HttpResponse

def nowa_strona(request):
    return HttpResponse("To jest nowa strona!")

def stara_strona(request):
    return redirect("nowa_strona")

def przekieruj_na_zewnetrzna():
    return redirect("https://www.google.com")
