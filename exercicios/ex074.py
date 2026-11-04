# Maior e menor valores em Tupla

from random import randint

n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
print(f"Os números sorteados foram: {n1} {n2} {n3} {n4}")

lista = (n1, n2, n3, n4)
print(f"O maior valor sorteado foi o {max(lista)}")
print(f"O menor valor sorteado foi o {min(lista)}")