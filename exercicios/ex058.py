# Jogo da adivinhação v2.0

from random import randint
computador = randint(0, 5)
tentativa = ""
cont = 0

while tentativa != computador:
    print("-=-"*20)
    tentativa = int(input("Digite um número entre 0 e 10: "))
    print("-=-"*20)
    print(f"\33[32mAcertou! O número era o [{computador}]. Parabéns!\33[32m") if tentativa == computador else print(f"\33[31mErrou...\33[m")
    cont += 1
    if tentativa < computador:
        print("Para cima...")
    elif tentativa > computador:
        print("Para baixo...")
        

print(f"Você acertou após {cont} tentativas.\33[m")
    