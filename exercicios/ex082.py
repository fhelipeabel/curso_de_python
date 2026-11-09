# Dividindo valores em várias listas

lista = []
pares = []
impares = []
continuar = ""

while continuar != "N":

    n = int(input("Digite um número: "))
    lista.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    continuar = str(input("Quer continuar? [S/N] ")).upper()
    while continuar != "N" and continuar != "S":
        continuar = str(input("Não entendi. Quer continuar? ")).upper()
    
    if continuar == "S":
        continue
    elif continuar == "N":
        break

print(f"\nA lista completa é {lista}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {impares}")