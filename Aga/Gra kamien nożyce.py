

import random

wybor = ["kamień", "papier", "nożyce"]
user = input("wybierz i wpisz 1 element: kamień, papier, nożyce:")

komputer = random.choice(wybor)  #losowy wybór komputera
print(f"komputer wybrał: {komputer}")
if user == komputer:
        print("remis")
elif user == "kamień":
    if komputer == "nożyce":
        print ("wygrałeś z komputerem!")
    else:
        print("przegrałeś")
elif user == "papier":
    if komputer == "kamień":
        print("wygrałeś z komputerem!")
    else:
        print("przegrałeś")
elif user == "nożyce":
    if komputer == "papier":
        print("wygrałeś z komputerem!")
    else:
        print("przegrałeś")




