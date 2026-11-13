# Jogo de dados em Python
from random import randint
players = {}
for i in range(0,4):
    p = input("Nome do jogador: ")
    players[p] = int(randint(1,6))
    print(f"O jogador {}")

print(players)