def zastosuj_na_kazdym(lista,funkcja):
    Lista_wynikow = []
    for element in lista:
        result = funkcja(element)
        lista_wynikow.append(result)
    return lista_wynikow

def podwoj(x):
    return x*2


if __name__ == "__main__":
    lista_liczb = [1, 2, 3, 4, 5]
    result = zastosuj_na_kazdym(lista_liczb, podwoj)

    print(podwoj(3))

