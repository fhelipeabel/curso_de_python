# Extraindo dados de uma lista

lista = []
soma = 0

while True:
    n = int(input("Digite um valor: "))
    if n == 0:
        break
    lista.append(n)

print(f"Foram digitados {len(lista)} números.")
lista.sort(reverse=True)
print(lista)
print("O valor 5 foi digitado!" if 5 in lista else "Não encontrei o valor 5 na lista...")