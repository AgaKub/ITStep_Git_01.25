def fib(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def ciag_fib(n: int):
    lista = []
    for i in range(n):
        lista.append(fib(i))
    return lista

print(ciag_fib(10))
