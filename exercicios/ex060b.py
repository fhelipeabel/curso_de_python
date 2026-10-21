# Calculo do fatorial (usando o for)

n = int(input("Digite o número: "))

if n < 0:
    print("Digite um número natural.")
else:
    fatorial = 1
    cont = 1

    for i in range(n, 1, -1):
        fatorial *= i

    print(f"{n}! resulta em {fatorial}")