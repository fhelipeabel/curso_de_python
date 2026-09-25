# Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Dolar = R$ 3,27
carteira = int(input("Quanto você tem na carteira?\nDigite o número: "))

dolar_antes = 3.27
dolar_hoje = 5.21

convertido_antes = carteira * dolar_antes
convertido_hoje = carteira * dolar_hoje

def converter(a, b):
    conversao = a * b
    return conversao

print("O dolar no dia da aula custava R$ {}.".format(converter(carteira, dolar_antes)))
print("O dolar hoje custa R$ {}.".format(converter(carteira, dolar_hoje)))