import time

# Dekorator mierzący czas wykonania funkcji
def mierzenie_czasu(funkcja):
    def wrapper():
        start = time.time()  # zapamiętujemy czas przed uruchomieniem
        wynik = funkcja()    # uruchamiamy funkcję
        koniec = time.time() # zapamiętujemy czas po zakończeniu
        roznica = koniec - start
        print("Czas wykonania:", roznica, "sekundy")
        return wynik
    return wrapper

# Funkcja zwracająca liczby parzyste od 0 do 100000
@mierzenie_czasu
def znajdz_parzyste():
    parzyste = []
    for liczba in range(0, 100001):
        if liczba % 2 == 0:
            parzyste.append(liczba)
    return parzyste

# Wywołanie funkcji i wypisanie wyniku
lista = znajdz_parzyste()
print(lista)
