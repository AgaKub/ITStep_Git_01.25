class Samochod:
    def __init__(self, model, rok, producent, pojemnosc, kolor, cena):
        self.__model = model
        self.__rok = rok
        self.__producent = producent
        self.__pojemnosc = pojemnosc
        self.__kolor = kolor
        self.__cena = cena

    # Metoda do wyświetlania danych
    def pokaz_dane(self):
        print("Model:", self.__model)
        print("Rok wydania:", self.__rok)
        print("Producent:", self.__producent)
        print("Pojemność silnika:", self.__pojemnosc, "l")
        print("Kolor:", self.__kolor)
        print("Cena:", self.__cena, "PLN")

    # Settery (modyfikatory)
    def ustaw_model(self, model):
        self.__model = model

    def ustaw_rok(self, rok):
        self.__rok = rok

    def ustaw_producenta(self, producent):
        self.__producent = producent

    def ustaw_pojemnosc(self, pojemnosc):
        self.__pojemnosc = pojemnosc

    def ustaw_kolor(self, kolor):
        self.__kolor = kolor

    def ustaw_cene(self, cena):
        self.__cena = cena

    # Gettery (dostęp do danych)
    def pobierz_model(self):
        return self.__model

    def pobierz_rok(self):
        return self.__rok

    def pobierz_producenta(self):
        return self.__producent

    def pobierz_pojemnosc(self):
        return self.__pojemnosc

    def pobierz_kolor(self):
        return self.__kolor

    def pobierz_cene(self):
        return self.__cena

auto1 = Samochod("Corolla", 2020, "Toyota", 1.8, "biały", 75000)
auto1.pokaz_dane()

# Modyfikacja danych
auto1.ustaw_kolor("czarny")
print("\nZmieniony kolor:", auto1.pobierz_kolor())