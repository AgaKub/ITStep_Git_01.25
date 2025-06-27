class Stadium:
    def __init__(self, nazwa_stadionu, data_otwarcia, kraj, miasto, liczba_miejsc_siedzacych):
        self.nazwa_stadionu = nazwa_stadionu
        self.data_otwarcia = data_otwarcia
        self.kraj = kraj
        self.miasto = miasto
        self.liczba_miejsc_siedzacych = liczba_miejsc_siedzacych

    def pokaz_dane(self):
        print("Nazwa stadionu:", self.nazwa_stadionu)
        print("Data otwarcia:", self.data_otwarcia)
        print("Kraj:", self.kraj)
        print("Miasto:", self.miasto)
        print("Liczba miejsc siedzących:", self.liczba_miejsc_siedzacych)

    # Getter kraju
    def podaj_kraj(self):
        return self.kraj

    # Setter kraju
    def zmien_kraj(self, nowy_kraj):
        self.kraj = nowy_kraj


# Tworzenie stadionu
stadion1 = Stadium("Amber", 1992, "Polska", "Gdańsk", 25000)

# Wyświetlenie danych
stadion1.pokaz_dane()

# Zmiana kraju
stadion1.zmien_kraj("Polska – Pomorze")

# Sprawdzenie zmiany
print("\nPo zmianie kraju:")
print("Nowy kraj:", stadion1.podaj_kraj())
