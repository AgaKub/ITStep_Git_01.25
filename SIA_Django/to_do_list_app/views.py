from django.shortcuts import render
from django.http import HttpResponse
from.models import Task

def witaj(request):
    return HttpResponse("<h1>Witaj na mojej stronie!<h1>")

def task_list(request):
    tasks = Task.objects.all()
    context = {"tasks":tasks}
    return render(request, "to_do_list_app/task_list.html", context)

def strona_statyczna(request):
    return render(request, "to_do_list_app/Statyczna_strona.html")

def powitanie(request):
    dane = {
        "imię":"Użytkownik Django",
        "wiadomość": "Witam cie na naszej stronie."
        }
    return render(request, "to_do_list_app/witaj.html", dane)