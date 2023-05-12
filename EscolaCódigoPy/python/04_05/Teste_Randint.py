from random import randint
def lista(n):
    L = []
    for i  in range(n):
        L.append(randint(10,99))
    return L


def listasr(n):
    L = []
    while len(L) < n:
        x = randint(10,20)
        if x not in L:
            L.append(x)
    return L
