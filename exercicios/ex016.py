# Quebrando um número e exibindo apenas a parte inteira
import math
import random
aleatorio = random.random()
inteiro = random.randint(1,10)

numero = aleatorio + inteiro

print("\nO número real é {}.".format(numero))

#Transformando o número em inteiro
novo = math.floor(numero)
print("A parte inteira é {}".format(math.floor(novo)))

#Provando que a variável foi salva inteira com .floor
print("A soma deste número mais 1.5 é {}.\n".format(novo + 1.5))