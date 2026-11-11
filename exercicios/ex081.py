# Extraindo dados de uma lista
lista = []
soma = 0
while True:
    lista.append(int(input("Digite um valor: ")))
    resp = str(input("Quer continuar? [S/N] ")).upper()
    if resp == "N":
        break
print(f"\nForam digitados {len(lista)} números.")
lista.sort(reverse=True)
print(lista)
print("O valor 5 foi digitado!" if 5 in lista else "Não encontrei o valor 5 na lista...")