# tworzę katalog produktów z cenami
# moze 2 listy

produkty = ["marchew", "jabłko", "gruszka", "ziemniak", "pomidor"]
ceny = [2, 6, 7, 1, 10]


def pobierz_produkty():
    koszykzakupow = []
                     # tworzymy pustą liste na produkty uzytkownika, do której program bedzie wpisywał wybrane produkty

    print("wpisz nazwe produktu. po zakończeniu, wpisz 'koniec'")   #informacja dla użytkownika co ma robić
    produkt = ""                                #pobieramy dane od użytkownika i dodaje do listy koszykzakupów = []
    END = "koniec"
    while produkt != END:
        produkt = input("wpisz nazwę produktu:")
        if produkt != END:
            koszykzakupow.append(produkt)
    return koszykzakupow
#testowanie koszyka
#wywołanie funkcji
koszykzakupow = pobierz_produkty()
#wyświetlenie wyniku na ekranie
print("Twój koszyk:", koszykzakupow)


#zliczamy ilości produktów w koszyku; sprawdzmy czy produkt z listy produkty pojawił się w liscie koszykzakupów
# zaczynamy od 0 bo bedziemy dodawac do 0

def zliczamyilości(produkty, koszykzakupow):
    ilości = []                 # tworzymy pustą listę na ilości produktów w koszykuzakupow
    for produkt in produkty:    # sprawdzamy dla każdego produktu z listy produkty ile razy znalazł sie w koszykuzakupów"
        liczba = 0               #licznik domyślny dla każdego produktu
        for wpis in koszykzakupow: #sprawdzamy produkty w koszyku zakupów
            if wpis == produkt:
               liczba = liczba + 1
        ilości.append(liczba)
    return ilości
#tesujemy ilości
#wywołanie funkcji
ilości = zliczamyilości(produkty, koszykzakupow)
print("ilość produktów w koszyku:", ilości)


#obliczanie wartości brutto paragonu tj listy ilości
def obliczanie_wartości_brutto(ilości, ceny):
    wartościbrutto = []         #lista na wartości brutto wszystich produktow
    for i in range(len(ilości)):
        wartośćbrutto = ilości[i]*ceny[i]
        wartościbrutto.append(wartośćbrutto)
    return wartościbrutto
#testujemy wartościbrutto
#wywołujemy funkcję
wartościbrutto = obliczanie_wartości_brutto(ilości, ceny)
print ("wartość brutto produktów w koszyku:", wartościbrutto)

def suma_wartościbrutto(wartościbrutto):
    suma = 0
    for wartośćbrutto in wartościbrutto:
        suma = suma + wartośćbrutto
    return suma
suma = suma_wartościbrutto(wartościbrutto)
print("całkowita wartośc brutto koszyka:", suma)

#obliczanie wartości Vat
def obliczanie_wartości_VAT(wartościbrutto, stawka_VAT):
    Vat = []
    for i in wartościbrutto:
        vat_produktu = i * stawka_VAT
        Vat.append(vat_produktu)
    return Vat
stawka_VAT = 0.23
Vat = obliczanie_wartości_VAT(wartościbrutto, stawka_VAT)
print("kwoty VAT produktów w koszyku:", Vat)


def oblicanie_całk_VAT_paragonu(Vat):
    suma_Vat = 0
    for vat_produktu in Vat:
        suma_Vat = suma_Vat + vat_produktu
    return suma_Vat
suma_Vat = oblicanie_całk_VAT_paragonu(Vat)
print("Całkowita kwota VAT:", suma_Vat)


#tworzymy plik txt paragon
def stwórz_paragon(produkty, ilości, ceny, Vat):
    paragon = []
    for i in range(len(produkty)):
        if ilości[i]>0:  #tylko dla produktó wybranych do koszykazakupów
            linia = produkty[i] + "|" + str(ilości[i]) + "|" + str(ceny[i]) + "zł" + "|" + str(Vat[i]) + "zł"
            paragon.append(linia)
    return paragon
paragon = stwórz_paragon(produkty, ilości, ceny, Vat)
print(stwórz_paragon)

#wyświetlenie zawartości paragonu do sprawdzenia
def wyświetl_paragon(paragon, suma,  suma_Vat):
    if len(paragon) == 0:  #jesli koszyk jest pusty
        print("Koszyk jest pusty")
    else:
        for linia in paragon:
            print(linia)
        print("podsumowanie")
        print ("wartość brutto zakupów w koszyku:", suma, "zł")
        print( "wartość VAT:", suma_Vat, "zł")
        print("Dziękujęmy za zakupy w naszym sklepie")
wyświetl_paragon(paragon, suma, suma_Vat)
print(wyświetl_paragon(paragon, suma, suma_Vat))

def stwórz_plik_paragon():
    #otwieramy plik w trybie zapisu
    plik = open("paragon.txt", "w")
    #tworzymy nagłowki kolumn
    plik.write("Produkt | Ilość | Cena | VAT")
    #dane o produktach
    for i in range(len(produkty)):
        if ilości[i]>0: #tylko produkty z koszykazakupów
            linia = produkty[i] +  "|" + str(ilości[i]) + "|" + str(ceny[i]) + "|" + str(Vat[i]) + "zł"
            plik.write(linia)
    #podsumowanie kwot
    plik.write("suma brutto:" + str(suma) + "zł")
    plik.write("suma VAT:" + str(suma_Vat) + "zł")
    plik.close()
stwórz_plik_paragon()
print(stwórz_plik_paragon)





#zapisanie paragonu w postaci pliku txt
def zapisz_paragon(paragon, suma, suma_Vat):
    plik = open("paragon.txt", "w")
    plik.write("Produkt | Ilość | Cena Brutto | VAT")
    plik.write(paragon)
    plik.write("Podsumowanie")
    pli.write("Wartość brutto zakupów w koszyku:", suma, "zł")
    plik.write( "wartość VAT:", suma_Vat, "zł")
    plik.write("Dziękujemy za zakupy w naszym sklepie")
    plik.close()





