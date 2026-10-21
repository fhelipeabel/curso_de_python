# Tratando vários valores v1.0

n = 0
i = 0
soma = 0

while n != 999:
    n = int(input("Escolha um valor: "))
    if n != 999:
        i += 1
        soma += n

print(f"Foram digitados {i} valores, e o total foi de R$ {soma:.2f}")