# Soma dos pares

soma = 0

for c in range(0, 6):
    n = int(input("Número: "))
    if n % 2 == 0:
        soma = soma + n

print(f"A soma dos pares é \33[33m{soma}\33[m")