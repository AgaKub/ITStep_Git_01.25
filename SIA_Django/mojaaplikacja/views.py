import datetime

from django.core.serializers import serialize
from django.shortcuts import render
import datetime

from django.template.context_processors import request
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.utils.representation import serializer_repr

from .forms import FormularzKontaktowy
from .forms import FormularzRejestracji
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProduktSerializer, KategoriaSerializer, ZamowienieSerializer,PozycjaZamowieniaSerializer
from .models import Produkty, Kategoria, Zamowienie, PozycjaZamowienia

from rest_framework.views import APIView
from django.http import Http404
from rest_framework import viewsets



class ProduktyViewSet(viewsets.ModelViewSet):
    queryset = Produkty.objects.all()
    serializer_class = ProduktSerializer

class KategoriaViewSet(viewsets.ModelViewSet):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer


class ZamowienieViewSet(viewsets.ModelViewSet):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer

class PozycjaZamowieniaViewset(viewsets.ModelViewSet):
    queryset = PozycjaZamowienia.objects.all()
    serializer_class = PozycjaZamowieniaSerializer

class ProduktList(APIView):
    '''
    widok do obslugi list produktow (GET) i tworzenia produktu(POST)
    '''

def get(self, request, format=None):
    produkty = Produkty.objects.all()
    serializer = ProduktSerializer(produkty, many=True)
    return Response(serializer.data)

def post(self, request, format=None):
    serializer = ProduktSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProduktDetail(APIView):
    '''
    widok do obslugi pojedyunczego produktu (GET, PUT, DELETE)
    '''

    def get_object(selfself, pk):
        try:
            return Produkty.objects.get(pk=pk)
        except Produkty.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        produkt = self.get_object(pk=pk)
        serializer = ProduktSerializer(produkt)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        produkt = self.get_object(pk=pk)
        serializer = ProduktSerializer(produkt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        produkt = self.get_object(pk=pk)
        produkt.delete()
        return Response(staus=status.HTTP_204_NO_CONTENT)





@api_view(['GET', 'POST'])
def produkt_list(request):
    '''
       wyswietla liste produktow lub tworzy nowy produkt
        '''
    if request.method =="GET":
        produkt = Produkty.objects.all()
        serializer = ProduktSerializer(produkt,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProduktSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])

def produkt_detail(request, pk):    #primerki
    '''
    pobiera, aktualizuje lub usuwa pojedynczy produkt
    '''
    try:
        produkt = Produkty.objects.get(pk=pk)
    except Produkty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProduktSerializer(produkt)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProduktSerializer(produkt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        produkt.delet()
        return Response(status=status.HTTP_204_NO_CONTENT)

class KategoriaList(APIView):
    '''
    widok do obslugi listy kategorii (GET) i twoirzenia nowej kategorii
    '''
    def get(self, request, format=None):
        kategorie = Kategoria.objects.all()
        serializer = KategoriaSerializer(kategorie, many=True)
        return Response(serializer.data)

    def post(self, request,format=None):
        serializer = ProduktSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KategoriaDetail(APIView):
    def get_object(self, pk):
        try:
            return Kategoria.objects.get(pk=pk)
        except Kategoria.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        kategoria = self.get_object(pk=pk)
        serializer = KategoriaSerializer(kategoria)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        kategoria = self.get_object(pk=pk)
        serializer = KategoriaSerializer(kategoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        kategoria = self.get_object(pk=pk)
        kategoria.delete()
        return Response(staus=status.HTTP_204_NO_CONTENT)





def powitanie(request):
    teraz = datetime.datetime.now()
    imie_uzytkownika = request.GET.get("imie")
    wiadomosc = 'Milo Cie widziec!'
    dane = {"imie": imie_uzytkownika,
            "wiadomosc":wiadomosc}
    return render(request, "mojaaplikacja/powitanie.html", dane)

def wyswietl_info(request):
    dane = {
        "strona": {
            "tytul": "informacje o naszej stronie",
            "opis":" To jest strona z wieloma ciekawymi informacjami",
            "cechy": ["szybka", "responsywna", "Łatwa", "bogata w tresc"],
                "autor": {
                "imie": "Jan",
                "nazwisko": "Kowalski"
                    }
               },
        "wersja": "1.0"
                   }
    return render(request, "mojaaplikacja/info.html", dane)

def witaj(request):
    teraz = datetime.datetime.now()
    czy_jest_rano = teraz.hour < 12
    dane = {
        "imie": "Anna",
        "wiadomosc": "Milo Cie widzieć",
        "teraz": teraz,
        "czy_jest_rano": czy_jest_rano
    }
    return render(request, "mojaaplikacja/witaj.html", dane)

def lista_produktow(request):
    produkty = ["Produkt1", "Produkt2", "Produkt3"]
    return render(request, "mojaaplikacja/produkty.html", {"produkty":produkty})

def kontakt(request):
    if request.method == "POST":
        form = FormularzKontaktowy(request.POST)
        if form.is_valid():
            imie = form.cleaned_data["imie"]
            email = form.cleaned_data["email"]
            wiadomosc = form.cleaned_data["wiadomosc"]
            return render(request, "mojaaplikacja/kontakt_sukces.html", {"imie": imie})
        else:
            return render(request, 'mojaaplikacja/kontakt.html', {"form": form})
    else:
        form = FormularzKontaktowy()
        return render(request, 'mojaaplikacja/kontakt.html', {"form": form})



def rejestracja(request):
    if request.method == "POST":
        form = FormularzRejestracji(request.POST)
        if form.is_valid():
            return render(request, "mojaaplikacja/rejestracja_sukces.html")
        else:
            return render(request, "mojaaplikacja/rejestracja.html", {"form": form})
    else:
        form = FormularzRejestracji()
        return render(request, "mojaaplikacja/rejestracja.html", {"form": form})
