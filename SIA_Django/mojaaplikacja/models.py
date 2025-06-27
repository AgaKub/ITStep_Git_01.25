from email.policy import default

from django.db import models

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100, unique=True)
    opis = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nazwa

class Produkty(models.Model):
    nazwa = models.CharField(max_length=200)
    opis = models.TextField(blank=True, null=True)
    cena = models.DecimalField(max_digits=10,decimal_places=2)
    czy_dostepne = models.BooleanField(default=False)
    data_dodania = models.DateTimeField(auto_now_add=True)
    liczba_odwiedzin = models.IntegerField(default=0)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.nazwa

class Zamowienie(models.Model):
    data_zamowienia = models.DateTimeField(auto_now_add=True)
    nr_zamowienia = models.CharField(max_length=50)
    calkowita_kwota = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'Zamowienie {self.id} - {self.status}'


class PozycjaZamowienia(models.Model):
    zamowienie = models.ForeignKey(Zamowienie, related_name='pozycje', on_delete=models.CASCADE)
    produkt = models.ForeignKey(Produkty, on_delete=models.CASCADE)
    ilosc = models.IntegerField(default=1)
    cena_jednostkowa = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f'{self.ilosc} x {self.produkt.nazwa} w zamowieniu {self.zamowienie}'

    @property
    def laczna_cena_pozycji(self):
        return self.ilosc * self.cena_jednostkowa
