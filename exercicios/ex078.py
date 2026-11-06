# Maior e menor valores na lista

lista = list()
maiores = list()
menores = list()

for i in range(0, 5):
    lista.append(input("Digite um número: "))

for i, v in enumerate(lista):
    if v == max(lista):
        maiores.append(i)
    elif v == min(lista):
        menores.append(i)

print(f"O maior digitado foi {max(lista)}, nas posições", end=" ")
for c in maiores:
    print(f"{c}", end=" ")

print(f"\nO menor digitado foi {min(lista)}, nas posições", end=" ")
for c in menores:
    print(f"{c}", end=" ")