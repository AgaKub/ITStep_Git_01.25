# Funkcja rysująca poziomą linię — uproszczona wersja bez pętli
def draw_horizontal(symbol):
    print(symbol * 10)  # wypisuje symbol 10 razy w jednym wierszu

# Funkcja rysująca pionową linię
def draw_vertical(symbol):
    for i in range(10):
        print(symbol)  # każdy symbol w nowej linii


def show_line(symbol, function_to_call):
    # Wywołuje przekazaną funkcję z przekazanym symbolem
    function_to_call(symbol)

# Pytamy użytkownika o symbol
symbol = input("Podaj symbol, którego chcesz użyć: ")

# Pytamy użytkownika o typ linii
typ_linii= input("Jaki typ linii chcesz narysować? (pozioma/pionowa): ")

# Wybór odpowiedniej funkcji i przekazanie jej do show_line
if typ_linii == "pozioma":
    show_line(symbol, draw_horizontal)
elif typ_linii == "pionowa":
    show_line(symbol, draw_vertical)
else:
    print("Nieprawidłowy typ linii. Wpisz 'pozioma' lub 'pionowa'.")