# Jogo de dados em Python
from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
for i in range(0,4):
    n = randint(1,6)
    jogo[f"Jogador{i+1}"] = n

ranking = list()
print("-"*25)
print(f"{"Valores sorteados":^25}")
print("-"*25)
for k, v in jogo.items():
    print(f"{k} jogou {v} no dado")
    sleep(0.3)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f"\n{"Ranking:":^20}")
for i, v in enumerate(ranking):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}.")