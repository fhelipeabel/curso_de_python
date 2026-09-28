# Sorteando um item na lista
import random
opcoes = []

nome = input("\nDigite o primeiro nome: ")
opcoes.append(nome)
nome = input("Digite o segundo nome: ")
opcoes.append(nome)
nome = input("Digite o terceiro nome: ")
opcoes.append(nome)
nome = input("Digite o quarto nome: ")

sorteado = random.choice(opcoes)

print("Quem foi escolhido para limpar o quadro hoje foi {}.".format(sorteado))