def poza_zakresem(lista, poczatek, koniec):
    for liczba in lista:
        if liczba < poczatek or liczba > koniec:
            yield liczba

liczby = [3, 7, 10, 15, 22, 30]
wynik = poza_zakresem(liczby, 10, 20)

for liczba in wynik:
    print(liczba)
