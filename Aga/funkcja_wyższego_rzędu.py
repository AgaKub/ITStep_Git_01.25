def filtruj(lista, funkcja_filtrująca):
    Lista1 = []
    for i in lista:
        if funkcja_filtrująca(i):
            Lista1.append(i)
    return Lista1

def czy_parzysta(liczba):
    reszta = liczba % 2
    if reszta == 0:
        return True
    else:
        return False
lista = [1,2,3,4,5,6,7,8,]
wynik = filtruj(lista, czy_parzysta)
print(wynik)