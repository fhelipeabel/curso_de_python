# Soma dos pares

soma = 0
cont = 0

for c in range(0, 6):
    n = int(input("Número: "))
    if n % 2 == 0:
        soma = soma + n
        cont += 1

print(f"Você informou {cont} números pares e a soma é \33[33m{soma}\33[m.")