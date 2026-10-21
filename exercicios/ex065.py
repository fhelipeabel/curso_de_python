# Maior e menor valores

continuar = ""
i = 0
soma = 0
maior = None
menor = None

while continuar.upper() != "N":
    n = int(input("Digite um número: "))
    if menor is None:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    i += 1
    soma += n
    continuar = input("Você deseja continuar (S/N)? ")
    if continuar.upper() == "N":
        print("Encerrando...")
        break

print(f"\nQuantidade de números digitados: {i}")
print(f"Média dos valores: {soma / i:.0f}")
print(f"O maior valor digitado foi o {maior}.")
print(f"O menor valor digitado foi o {menor}.")