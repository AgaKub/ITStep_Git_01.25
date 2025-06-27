def czy_palindrom(liczba):
    liczba_str = str(liczba)
    if liczba_str == liczba_str[::-1]:
        return True
    else:
        return False


print(czy_palindrom(123321))  # True