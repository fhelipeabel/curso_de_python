# Aprimorando os dicionários
jogadores = []
while True:
# ---------------------------------------------------------------------------------- Código antigo reaproveitado
    jogador = {}
    jogador["Nome"] = str(input("Nome do jogador: "))
    jogador["Gols"] = []
    for i in range(0,int(input(f"Quantas partidas {jogador["Nome"]} jogou? "))):
        jogador["Gols"].append(int(input(f"Quantos gols na partida {i+1}? ")))
    jogador["Total"] = sum(jogador["Gols"])
# ---------------------------------------------------------------------------------- Fim do código antigo reaproveitado
    jogadores.append(jogador)
    resp = str(input("Quer continuar? [S/N]: ")).upper()
    if resp == "N":
        break
print("-="*30)
print(f"cod", end=" ")
print(f"{"nome":<10}", end=" ")
print(f"{"gols"}", end=" ")
print(f"{"total":>16}")
print("-"*40)
for i, jogador in enumerate(jogadores):
    print(f"{i:>3}", end=" ")
    print(f"{jogador["Nome"]:<11}", end="")
    print(f"{str(jogador["Gols"]):<16}", end="")
    print(f"{jogador["Total"]:<25}")
choice = 