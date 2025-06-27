class Book:

    def __init__(self, tytul, autor, cena):
        self.tytul = tytul
        self.autor = autor
        self.cena = cena

    def pokaz_info(self, dane=False):
        if dane:
            return f"Tytuł: {self.tytul}, Autor: {self.autor}, Cena: {self.cena} zł"
        else:
            return f"{self.tytul} - {self.autor}"

    ksiazka1 = Book("Lalka", "Bolesław Prus", 39.90)

    print(ksiazka1.pokaz_info())  # krótka forma
    print(ksiazka1.pokaz_info(True))  # szczegółowa forma