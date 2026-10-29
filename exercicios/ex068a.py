# Jogo par ou ímpar

from random import randint

print("=== JOGO DO PAR OU ÍMPAR ===")
print("O jogo só termina quando você perder!")

usuario_ganhou = True
vitorias_consecutivas = 0

while usuario_ganhou:
    escolha_usuario = input("\nEscolha [P]ar ou [I]mpar: ").strip().upper()
    while escolha_usuario not in "PI":
        escolha_usuario = input("Opção inválida. Escolha[P]ar ou [I]mpar: ").strip().upper()
    
    numero_usuario = int(input("Digite um número (1 a 10): "))
    numero_computador = randint(0, 10)
    soma = numero_usuario + numero_computador
    resto_divisao = soma % 2

    soma_e_par = (resto_divisao == 0)

    print(f"Você jogou {numero_usuario} e o computador jogou {numero_computador}. Soma = {soma}.")

    if soma_e_par:
        print("-> A soma é PAR!")
    else:
        print("-> A soma é IMPAR!")

    if (escolha_usuario == "P" and soma_e_par) or (escolha_usuario == "I" and not soma_e_par):
        usuario_ganhou = True
        vitorias_consecutivas += 1
        print("Que sorte, você \33[32mganhou!\33[m")
    else:
        usuario_ganhou = False
        print("Que pena... você \33[31mperdeu\33[m.")

print("\n === FIM DE JOGO ===")
print(f"Você conseguiu um total de {vitorias_consecutivas} vitórias consecutivas!")