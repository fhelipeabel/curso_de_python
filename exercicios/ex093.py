# Cadastro de jogador de futebol
jogador = {}
jogador["Nome"] = str(input("Nome do jogador: "))
jogador["Gols"] = []
for i in range(0,int(input(f"Quantas partidas {jogador["Nome"]} jogou? "))):
    jogador["Gols"].append(int(input(f"Quantos gols na partida {i+1}? ")))
jogador["Total"] = sum(jogador["Gols"])
print("-="*30)
print(jogador)
print("-="*30)
# ----------------------------------------------------------------------------------
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}.")
print("-="*30)
# ----------------------------------------------------------------------------------
print(f"O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.")
for i, p in enumerate(jogador["Gols"], 1):
    print(f"Na partida {i}, fez {p} gols.")
print(f"Foi um total de {jogador["Total"]} gols.")
print("-="*30)