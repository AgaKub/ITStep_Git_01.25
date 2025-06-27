import time

def mierzenie_czasu(funkcja):
    def opakowanie(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        stop = time.time()
        print("Czas działania:", stop - start, "sekundy")
        return wynik
    return opakowanie

@mierzenie_czasu
def znajdz_parzyste(poczatek, koniec):
    lista = []
    for liczba in range(poczatek, koniec + 1):
        if liczba % 2 == 0:
            lista.append(liczba)
    return lista

wynik = znajdz_parzyste(0, 100000)
print(wynik)

