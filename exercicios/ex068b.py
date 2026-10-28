# Jogo par ou ímpar

from random import randint

usuario_ganhou = True
vitorias = 0

while usuario_ganhou:
    escolha_usuario = input("[P]ar ou [I]mpar? ").upper().strip()
    while escolha_usuario not in "PI":
        escolha_usuario = input("Opção inválida. Escolha[P]ar ou [I]mpar: ").strip().upper()

    numero_usuario = int(input("Digite um número de 0 a 10: "))
    numero_computador = randint(1, 10)

    soma = numero_usuario + numero_computador
    soma_e_par = True if soma % 2 == 0 else False

    if (escolha_usuario == "P" and soma_e_par) or (escolha_usuario == "I" and not soma_e_par):
        print("Você venceu!")
        usuario_ganhou = True
        vitorias =+ 1
    else:
        print("Você perdeu.")
        usuario_ganhou = False

print(f"Vitórias consecutivas: {vitorias}")