# Game: Pedra, Papel ou Tesoura

from random import randint
from time import sleep

def escolhido(escolha):
    if escolha == 0:
        return "PEDRA"

    elif escolha == 1:
        return "PAPEL"
    
    elif escolha == 2:
        return "TESOURA"

    else:
        return "\33[31mERRO\33[m!!!!"

print("""
SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
""")

player = int(input("Qual é a sua jogada? "))
computer = int(randint(0, 2))

if (player < 0 or player > 2):
    print("Escolha uma jogada válida.")

else:
    jogada_player = escolhido(player)
    jogada_comp = escolhido(computer)
    
    sleep(0.7)
    print("\nJO...")
    sleep(0.5)
    print("KEN...")
    sleep(0.3)
    print("PO!")
    sleep(0.3)
    print("-="*20)
    print(f"Jogador: {jogada_player} | Computador: {jogada_comp}")
    print("-="*20)

    #Criando o motor

    if (jogada_player == "PEDRA" and jogada_comp == "TESOURA") or (jogada_player == "PAPEL" and jogada_comp == "PEDRA") or (jogada_player == "TESOURA" and jogada_comp == "PAPEL"):
        print("\33[32mJOGADOR VENCE\33[m")
        print("-="*10)

    elif ((jogada_comp == "PEDRA" and jogada_player == "TESOURA") or (jogada_comp == "PAPEL" and jogada_player == "PEDRA") or (jogada_comp == "TESOURA" and jogada_player == "PAPEL")):
        print("\33[31mCOMPUTADOR VENCE\33[m")
        print("-="*10)

    else:
        print("\33[33mEMPATE\33[m")
        print("-="*10)