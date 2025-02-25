def sr_aryt(*args):
    if len(args) == 0:
        return 0
    return sum(args)/ len(args)

if __name__ == "__main__":
    wynik = sr_aryt(2,4,5,6,7)
    print(wynik)




def slownik(**kwargs):
    return kwargs

if __name__ == "__main__":
   dict = slownik(imie="Aga", nazwisko= "Kub")
   print(dict)



def print_info_products(nazwa, cena, **other_info):
    print(f"nazwa: {nazwa}")
    print(f"cena: {cena}")
    print(f"other_info:")
    for info, wartość in other_info.items():
        print(f" {info}: {wartość}")

if __name__ == "__main__":
