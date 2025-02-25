try:
    print(10/0)
except zeroDivisionError:
    print("Divison by zero")
except TypeError:
    print("nie podałeś liczby")
finally:
    print()   # CO MA ZROBIĆ ZE ZNALEZIONYM BŁEEDEM

try:
    print(10/0)
except(zerodivisionerrot, typeError):

    try
        raise SyntaxError

