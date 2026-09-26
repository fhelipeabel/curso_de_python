# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. (aproveitei para testar salvar em uma variável)
import math
import random
aleatorio = random.random()
inteiro = random.randint(1,10)

numero = aleatorio + inteiro

print("\nO número real é {}.".format(numero))
novo = math.floor(numero)
print("A parte inteira é {}".format(math.floor(novo)))
print("A soma deste número mais 1.5 é {}.\n".format(novo + 1.5))