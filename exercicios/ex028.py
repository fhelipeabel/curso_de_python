# Jogo da adivinhação v1.0

from random import randint
computador = randint(0, 5)
print("-=-"*20)
n = int(input("Digite um número de 0 a 5: "))
print("-=-"*20)
print("Acertou! Parabéns!" if n == computador else "Errou feio. o número era \33[1;33m{}\33[m.\nO computador venceu.".format(computador))
print("-=-"*20)