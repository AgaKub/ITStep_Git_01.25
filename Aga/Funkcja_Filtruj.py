def stw_profil(imie, nazwisko, **kwargs):
    profil = {"imie": imie, "nazwisko": nazwisko}
    profil.update(kwargs) #dodaje dodatkwe informacje do słownika
    return profil

if __name__ == "__main__":
    profil_osoby = stw_profil("Aga", "Kub", wiek = 18, miasto = "gdansk")
    print(profil_osoby)
