class Stadium:
    def __init__(self, nazwa, data_otwarcia, kraj, miasto, liczba_miejsc):
        self.nazwa = nazwa
        self.data_otwarcia = data_otwarcia
        self.kraj = kraj
        self.miasto = miasto
        self.liczba_miejsc = liczba_miejsc

    def pokaz_info(self, szczegoly=False):
        if szczegoly:
            return f"Nazwa: {self.nazwa}, Rok otwarcia: {self.data_otwarcia}, Kraj: {self.kraj}, Miasto: {self.miasto}, Miejsc: {self.liczba_miejsc}"
        else:
            return f"{self.nazwa} w {self.miasto}"


stadion1 = Stadium("Amber", 1992, "Polska", "Barcelona", 99354)

print(stadion1.pokaz_info())            # tylko nazwa i miasto
print(stadion1.pokaz_info(True))        # pełne informacje
