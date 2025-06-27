def pomnoz_liste(lista, liczba):
    wynik = []                  # Tworzymy pustą listę, do której będziemy dodawać wyniki
    for element in lista:       # Dla każdego elementu w podanej liście
        nowy_element = element * liczba   # Mnożymy element przez podaną liczbę
        wynik.append(nowy_element)        # Dodajemy wynik do listy wynik
    return wynik

lista= [4, 3, 6, 8, 1]
liczba = 3

wynik = pomnoz_liste(lista, liczba)

print(wynik)
