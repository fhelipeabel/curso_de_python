# Sorteando um item na lista
from random import choice

n1 = input("\nPrimeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Terceiro aluno: ")
n4 = input("Quarto aluno: ")
opcoes = [n1, n2, n3, n4]

sorteado = choice(opcoes)

print("Quem foi escolhido para limpar o quadro hoje foi {}.".format(sorteado))