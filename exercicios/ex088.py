# Palpites para a Mega Sena
from random import sample
from time import sleep
lista_jogos = []
qtd = int(input("Quantos jogos você quer que eu sorteie? "))
for jogo in range(qtd):
    sleep(0.3)
    lista_jogos.append(sorted(sample(range(1,61),6)))
    print(f"Jogo {jogo+1}: {lista_jogos[jogo]}")