def nieparzyste_z_zakresu(poczatek, koniec):
    for liczba in range(poczatek, koniec + 1):
        if liczba % 2 != 0:
            yield liczba


for liczba in nieparzyste_z_zakresu(3, 15):
    print(liczba)
