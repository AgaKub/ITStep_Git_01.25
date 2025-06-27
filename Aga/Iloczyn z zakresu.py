def iloczyn_zakresu(poczatek, koniec):
    if poczatek > koniec:
        poczatek, koniec = koniec, poczatek

    iloczyn = 1
    for liczba in range(poczatek, koniec + 1):
        iloczyn = iloczyn * liczba

    return iloczyn

wynik = iloczyn_zakresu(5, 2)
print(wynik)  # Wynik: 120 (czyli 2 * 3 * 4 * 5)
