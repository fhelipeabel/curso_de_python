# Faça um algorítmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto.

valor = float(input("Digite o valor do produto: "))
desconto = 5
valor_promocional = valor * (0.01 * (100 - desconto))

print("O valor promocional com \33[1;33m{}%\33[m de desconto é R$ \33[1;33m{:.2f}\33[m.".format(desconto, valor_promocional))