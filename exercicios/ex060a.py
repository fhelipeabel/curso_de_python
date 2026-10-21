# Cálculo do Fatorial (usando While)

n = int(input("Digite o número: "))
inicio = n
cont = n
fatorial = 1
invalid = False

if n == 0:
    fatorial = 1

elif n > 1:
    while cont >= 2:
        cont -= 1
        n = n * cont

    fatorial = n
elif n == 1:
    fatorial = 1

else:
    print("Digite um número natural inteiro.")
    invalid = True

if not invalid:
    print(f"{inicio}! ({inicio} fatorial) resulta em {fatorial}")
else:
    print(f"We coudn't continue, because the number {n} is invalid")