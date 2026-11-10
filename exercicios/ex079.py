# Valores únicos em uma lista
lista = []
while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        print(f"\33[32mNúmero {n} adicionado.\33[m")
    else:
        print(f"\33[31mNúmero {n} já existe na lista.\33[m")
    continuar = input("Quer continuar? [S/N]: ").upper()
    if continuar in "Nn":
        break
lista.sort()
print(f"Você digitou os valores {lista}")