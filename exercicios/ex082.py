# Dividindo valores em várias listas
lista = []
pares = []
impares = []
while True:
    lista.append(int(input("Digite um número: ")))
    continuar = str(input("Quer continuar? [S/N] "))
    if continuar in "Nn":
        break
for i, n in enumerate(lista):
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f"\nA lista completa é {lista}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {impares}")