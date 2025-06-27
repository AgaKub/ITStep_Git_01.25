import random

def generate_number():
    return str(random.randint(1000,9999))

def count_bulls_and_cows(PC_number, user_number):
    bulls = 0
    cows = 0

    for i in range(len(PC_number)):
        if PC_number[i] == user_number[i]:
            bulls += 1
        elif user_number[i] in PC_number:
            cows += 1

    return bulls, cows


def play_game(PC_number, attempts=0):
    user_number = input("Podaj czterocyfrową liczbę: ")

    if user_number.isdigit() == False or len(user_number) != 4:
        print("Nieprawidłowe dane. Podaj dokładnie czterocyfrową liczbę.")
        return play_game(PC_number, attempts)

    attempts += 1
    bulls, cows = count_bulls_and_cows(PC_number, user_number)

    if bulls == 4:
        print(f"Gratulacje! Odgadłeś /aś liczbę {PC_number} w {attempts} próbach.")
        return

    print(f"Bulls: {bulls}, Cows: {cows}")
    return play_game(PC_number, attempts)


if __name__ == "__main__":
    PC_number = generate_number()
    print("Witaj w grze Bulls i KCows!")
    play_game(PC_number)
