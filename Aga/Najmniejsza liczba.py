def najmniejsza_liczba(a, b, c, d, e):
    min_liczba = a
    if b < min_liczba:
        min_liczba = b
    if c < min_liczba:
        min_liczba = c
    if d < min_liczba:
        min_liczba = d
    if e < min_liczba:
        min_liczba = e
    return min_liczba
wynik = najmniejsza_liczba(8,3,10, -2,5)

print(wynik)
