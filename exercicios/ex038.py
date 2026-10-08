# Comparando números

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

if n1 > n2:
    print(f"O PRIMEIRO VALOR ({n1}) é maior.")
elif n1 < n2:
    print(f"O SEGUNDO VALOR ({n2}) é maior.")
else:
    print("AMBOS tem o MESMO VALOR, portanto não há um maior.")