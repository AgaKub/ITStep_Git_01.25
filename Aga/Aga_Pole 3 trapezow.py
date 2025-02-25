
def oblpoltr(a, b, h):
    pole = h*(a+b)/2
    return pole

def nowalista(lista):
    nowalista = []
    for i in range(0, len(lista), 3):
        nowalista.append(lista)
        print(nowalista)

lista = [2, 4, 6, 7, 8, 9 ,4 ,2 , 6]
