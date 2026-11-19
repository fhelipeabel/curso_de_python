# Funções para sortear e somar
from random import sample
from time import sleep
numeros = []


def sorteia(listsort):
    listsort = list(sample(range(0,10),5))
    print(f"Sorteando 5 valores:", end=" ")
    for n in listsort:
        print(n, end=" ", flush=True)
        sleep(0.3)
    print("PRONTO!")
    return listsort


def somaPar(r):
    soma = 0
    epar = []
    for n in r:
        if n % 2 == 0:
            soma += n
            epar.append(n)
    print(f"A soma dos valores pares digitados {epar} é {soma}.")


result = sorteia(numeros)
somaPar(result)