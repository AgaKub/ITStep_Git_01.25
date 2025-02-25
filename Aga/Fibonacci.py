
def fib(n):
    # n ostatni element ciągu liczb Fib
    a =0
    b = 1
    for i in range (0, n):
        c = a + b
        a = b
        b = c
        print(c)



def fib(lista,n):
    lista = [0,1]
    for i in range (0, n-2):
        fib = []
        fib[i] = lista[1]+(fib[])

        print(fib)

    
n = 7

print(fib(n))


def fib(n:int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)










