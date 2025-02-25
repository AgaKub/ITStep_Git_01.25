while True:
    try:
        liczba = float(input("Podaj liczbę: "))
        print("Wartość bezwzględna:", abs(liczba))
        break
    except ValueError:
        print("Błąd: Podaj poprawną liczbę ")