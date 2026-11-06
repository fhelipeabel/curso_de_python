# Valores únicos em uma lista

from time import sleep

lista = []
n = 1
sistema_ativo = True

while sistema_ativo:
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        print(f"\33[32mNúmero {n} adicionado.\33[m")
    else:
        print(f"\33[31mNúmero {n} já existe na lista.\33[m")
    
    continuar = input("Quer continuar? [S/N]: ").upper()
    while continuar != "N" and continuar != "S":
        continuar = str(input("Digite corretamente se quer continuar (S/N): ")).strip().upper()
        if continuar == "S":
            sistema_ativo = True
        elif continuar == "N":
            print("Gerando lista em ordem...")
            sleep(0.5)
            sistema_ativo = False

lista.sort()
print(lista)