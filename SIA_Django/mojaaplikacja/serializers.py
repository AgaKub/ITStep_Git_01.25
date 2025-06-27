

from rest_framework import serializers
from .models import Produkty, Kategoria, Zamowienie, PozycjaZamowienia


#class ProduktSerializer(serializers.Serializer):
    #id = serializers.IntegerField(read_only = True)
    #nazwa = serializers.CharField(max_length=200)
    #opis = serializers.CharField(style={"base_template": "textarea"}, required=False)
    #cena = serializers.DecimalField(max_digits=10, decimal_places=2)
    #czy_dostepne = serializers.BooleanField(default=False)
    #data_dodania = serializers.DateTimeField(read_only=True)
    #liczba_odwiedzin = serializers.IntegerField(read_only=True)
    #kategoria = serializers.ForeignKey(Kategoria, on_delete=models.SET_NULL, null=True, blank=True)

    #def create(selfself, validated_data):
       # """
        #Tworzy i zwraca nowa instancje "Produkty" na podstawie zwalidoeanych danych.

        #"""
        #return Produkty.objects.create(**validated_data)

    #def update(selfself, instance, validated_data):
        #"""
        #aktualizuje i zwraca istniejąca instancje "produktu" na podtsawie zwalidowanych danych
        #"""
        #instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        #instance.opis = validated_data.get('opis', instance.opis)
        #instance.cena = validated_data('cena', instance.cena)
        #instance.czy_dostepne = validated_data('czy_dostepne', instance.czy_dostepne)
       # instance.save()
      #  return instance

class ProduktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkty
        fields = '__all__'
        #fields = ['id', 'nazwa', 'opis', itd - recznie mozna tak zrobic
        read_only_fields = ['data_dodania','liczba_odwiedzin']

class KategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoria
        fields = '__all__'

class PozycjaZamowieniaSerializer(serializers.ModelSerializer):
    produkt_nazwa = serializers.ReadOnlyField(source='produkt.nazwa')
    class Meta:
        model = PozycjaZamowienia
        fields = ['id', 'produkt_nazwa', 'ilosc', 'cena_jednostkowa', 'laczna_cena_pozycji']

        read_only_fields = ['laczna_cena_pozycji']




class ZamowienieSerializer(serializers.ModelSerializer):
    pozycje = PozycjaZamowieniaSerializer(many=True)

    class Meta:
       model = Zamowienie
       fields = ['id', 'data_zamowienia', 'calkowita_kwota', 'status', 'pozycje']
       read_only_fields = ['data_zamowienia', 'calkowita_kwota']


       def create(self, validated_data):
           pozycje_data = validated_data.pop('pozycje')
           zamowienie = Zamowienie.objects.create(**validated_data)
           total_kwota = 0
           for pozycja_data in pozycje_data:
               produkt = pozycja_data.get('produkt')
               if not produkt:
                   raise serializers.ValidationError('Produkt jest wymagany dla kazdej pozycji')

               cena_jednostkowa = produkt.cena

               PozycjaZamowienia.objects.create(zamowienie=zamowienie, cena_jednostkowa=cena_jednostkowa, **pozycja_data)
               total_kwota += pozycja_data['ilosc']

           zamowienie.calkowita_kwota = total_kwota
           zamowienie.save()

           return zamowienie

    def update(self, instance, validated_data):
        pozycje_data = validated_data.pop('pozycje')
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        instance.pozycje.all().delete()
        total_kwota = 0
        for pozycja_data in pozycje_data:
            produkt = pozycja_data.get('produkt')
            if not produkt:
                raise serializers.ValidationError('Produkt jest wymagany dla kazdej pozycji')

            cena_jednostkowa = produkt.cena
            PozycjaZamowienia.objects.create(zamowienie=instance, cena_jednostkowa=cena_jednostkowa, **pozycja_data)
            total_kwota += pozycja_data['ilosc'] *cena_jednostkowa

        instance.calkowita_kwota = total_kwota
        instance.save()
        return instance




