def wyswietl_parzyste(a, b):
    for liczba in range(a + 1, b):
        if liczba % 2 == 0:
            print(liczba)


wyswietl_parzyste(3,10)
