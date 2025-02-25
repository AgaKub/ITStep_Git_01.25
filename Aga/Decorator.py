def moj_dekorator(funkcja):

    def wrapper(*args, **kwargs):
        print(f"Wywołano funkcję: {funkcja.__name__}")
        wynik = funkcja(*args, **kwargs)
        print(f"Wynik: {wynik}")
        return wynik

    return wrapper

@moj_dekorator
def dodaj(a, b):
    return a + b

if __name__=="__main__":
    dodaj(3, 4)

 def my_decorator(func):
    def wrapper()
         return "DECORATED"--> +func() +" <--DECORATED"
    return wrapper

def helo_world():
    return "Hello, world"

if __name__ == "__main__":
    dodaj(3, 4)

    print(hello_world())
    print(my_decorator(hello_world)())

