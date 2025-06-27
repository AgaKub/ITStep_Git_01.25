def ile_cyfr(liczba):
    liczba = abs(int(liczba))  # usuwamy minus, i w razie potrzeby część po przecinku
    return len(str(liczba))

wynik = ile_cyfr(-3456)
print(wynik)