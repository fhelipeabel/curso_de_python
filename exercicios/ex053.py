texto = str(input("Digite o texto: "))

inverso = texto[::-1].lower().replace(" ", "")

if texto.lower().replace(" ", "") == inverso:
    print("Este texto é um palíndromo!")
else:
    print("Não é...")