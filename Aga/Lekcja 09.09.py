#stwórz funkcję sprawdzająca czy palindrom
def czy_palindrom(słowo):
   user = input("podaj słowo: ")
   if user == user[::-1]:
       print(f"słowo '{user}' to palinfrom")
   else:
       print(f"słowo '{user} nie jest palindromem")


