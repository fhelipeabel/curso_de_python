# Funções para sortear e somar
from random import randint
from time import sleep

def sorteia(lista):
    print(f"Sorteando 5 valores:", end=" ")
    for i in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f"{n} ", end=" ", flush=True)
        sleep(0.3)
    print("PRONTO!")

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"A soma dos valores pares digitados é {soma}.")

numeros = list()
sorteia(numeros)
somaPar(numeros)