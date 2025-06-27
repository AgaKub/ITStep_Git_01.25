class Book:
    def __init__(self, tytul, rok_wydania, wydawca, gatunek, autor, cena):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.wydawca = wydawca
        self.gatunek = gatunek
        self.autor = autor
        self.cena = cena

    def pokaz_dane(self):
        print("Tytuł:", self.tytul)
        print("Autor:", self.autor)
        print("Gatunek:", self.gatunek)
        print("Cena:", self.cena, "PLN")
        print("Rok wydania:", self.rok_wydania)
        print("Wydawca:", self.wydawca)

    # Getter autora
    def pobierz_autora(self):
        return self.autor

    # Setter autora
    def ustaw_autora(self, nowy_autor):
        self.autor = nowy_autor

    # Getter ceny
    def pobierz_cene(self):
        return self.cena

    # Setter ceny
    def ustaw_cene(self, nowa_cena):
        self.cena = nowa_cena

moja_ksiazka = Book("Mały Książę", 1943, "Rebis", "Baśń", "Antoine de Saint-Exupéry", 19.90)
moja_ksiazka.pokaz_dane()

# Zmiana autora
moja_ksiazka.ustaw_autora("Nowy Autor")
print("Zmieniony autor:", moja_ksiazka.pobierz_autora())

# Zmiana ceny
moja_ksiazka.ustaw_cene(22.50)
print("Zmieniona cena:", moja_ksiazka.pobierz_cene(), "PLN")
